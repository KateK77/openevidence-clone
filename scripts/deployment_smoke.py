"""Local-only container check with disposable PostgreSQL/Redis and synthetic accounts.

Requires the two test images built from deploy/Dockerfile.*. It never reads .env
or calls a model provider. Only resources created with a unique test prefix are removed.
"""
import json
import secrets
import subprocess
import time
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
prefix = 'medevidence-check-' + secrets.token_hex(4)
network = prefix + '-net'
names = []
checks = []


def run(*args, check=True):
    return subprocess.run(['docker', *args], check=check, capture_output=True, text=True)


def container(suffix, image, *args):
    name = prefix + '-' + suffix
    run('run', '-d', '--name', name, '--network', network,
        '--label', 'medevidence.test=' + prefix, *args, image)
    names.append(name)
    return name


def ready(name, *args):
    for _ in range(60):
        if run('exec', name, *args, check=False).returncode == 0:
            return
        time.sleep(.5)
    raise RuntimeError('Disposable test service did not become ready.')


try:
    run('network', 'create', '--label', 'medevidence.test=' + prefix, network)
    password = secrets.token_hex(24)
    db = container('db', 'postgres:17-alpine', '-e', 'POSTGRES_DB=medevidence',
                   '-e', 'POSTGRES_USER=medevidence', '-e', 'POSTGRES_PASSWORD=' + password)
    redis = container('redis', 'redis:7-alpine')
    ready(db, 'pg_isready', '-U', 'medevidence', '-d', 'medevidence')
    ready(redis, 'redis-cli', 'ping')
    api = container('api', 'medevidence-v3-api:test', '--network-alias', 'api',
        '-e', 'DJANGO_DEBUG=0', '-e', 'DJANGO_SECRET_KEY=' + secrets.token_hex(32),
        '-e', 'DJANGO_ALLOWED_HOSTS=localhost,testserver', '-e', 'TRUST_PROXY_HTTPS=1',
        '-e', f'DATABASE_URL=postgresql://medevidence:{password}@{db}:5432/medevidence',
        '-e', f'REDIS_URL=redis://{redis}:6379/0', '-e', 'LLM_API_KEY=', '-e', 'LLM_MODEL=')
    run('exec', api, 'python', 'manage.py', 'migrate', '--noinput')
    checks.append('Production database migrations completed on disposable PostgreSQL.')
    code = '''
import django
django.setup()
from django.test import Client
from django.core.cache import cache
from django.contrib.auth.models import User
cache.set('deployment-smoke', 'shared', 60)
assert cache.get('deployment-smoke') == 'shared'
User.objects.create_user('synthetic_deployment_test', password='Synthetic-test-password-42!')
client=Client(enforce_csrf_checks=True, HTTP_HOST='testserver', HTTP_X_FORWARDED_PROTO='https', HTTP_REFERER='https://testserver/')
token=client.get('/api/session/').json()['csrf']
response=client.post('/api/login/', data={'username':'synthetic_deployment_test','password':'Synthetic-test-password-42!'}, content_type='application/json', HTTP_X_CSRFTOKEN=token)
assert response.status_code == 200, (response.status_code, response.content)
assert client.cookies['medevidence_session_v2']['secure']
assert client.get('/api/session/').json()['user']['username'] == 'synthetic_deployment_test'
assert client.get('/api/health/').json()['version'] == '3.0.0'
print('Production PostgreSQL, Redis and secure session assertions passed.')
'''
    result = run('exec', '-e', 'DJANGO_SETTINGS_MODULE=evidence.settings', api, 'python', '-c', code, check=False)
    if result.returncode:
        raise RuntimeError('Production integration assertions failed: ' + result.stderr[-3000:])
    checks.append('Shared Redis cache, PostgreSQL account login and secure session cookie passed.')
    # Actual Gunicorn health, over the private Docker network; no host ports exposed.
    ready(api, 'python', '-c', "import requests; r=requests.get('http://localhost:8000/api/health/',headers={'X-Forwarded-Proto':'https'}); assert r.status_code==200")
    checks.append('Gunicorn served version 3.0.0 health successfully.')
    run('run', '--rm', '--network', network, '-e', 'SITE_DOMAIN=localhost',
        'medevidence-v3-web:test', 'caddy', 'validate', '--config', '/etc/caddy/Caddyfile')
    checks.append('Built frontend/Caddy configuration validated; public DNS and certificate issuance were not tested.')
    result = {'result': 'pass', 'scope': 'Isolated local container integration; no public deployment or model calls', 'checks': checks}
    print(json.dumps(result, indent=2))
    (repo / 'experiments/round-03/deployment-smoke.json').write_text(json.dumps(result, indent=2) + '\n')
finally:
    for name in reversed(names):
        label = run('inspect', '--format', '{{index .Config.Labels "medevidence.test"}}', name, check=False)
        if label.returncode == 0 and label.stdout.strip() == prefix:
            run('rm', '-f', '-v', name, check=False)
    label = run('network', 'inspect', '--format', '{{index .Labels "medevidence.test"}}', network, check=False)
    if label.returncode == 0 and label.stdout.strip() == prefix:
        run('network', 'rm', network, check=False)
