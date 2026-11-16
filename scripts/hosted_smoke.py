"""Check the free-hosting image on disposable local PostgreSQL, without secrets."""
import json
import secrets
import subprocess
import time
from pathlib import Path

prefix = 'medevidence-hosted-check-' + secrets.token_hex(4)
names = []


def docker(*args, check=True):
    return subprocess.run(['docker', *args], capture_output=True, text=True, check=check)


try:
    docker('network', 'create', '--label', 'medevidence.test=' + prefix, prefix)
    password = secrets.token_hex(24)
    db = prefix + '-db'
    docker('run', '-d', '--name', db, '--network', prefix, '--label', 'medevidence.test=' + prefix,
           '-e', 'POSTGRES_PASSWORD=' + password, '-e', 'POSTGRES_DB=medevidence', 'postgres:17-alpine')
    names.append(db)
    for _ in range(60):
        if docker('exec', db, 'pg_isready', '-U', 'postgres', check=False).returncode == 0:
            break
        time.sleep(.5)
    app = prefix + '-app'
    docker('run', '-d', '--name', app, '--network', prefix, '--label', 'medevidence.test=' + prefix,
           '-e', f'DATABASE_URL=postgresql://postgres:{password}@{db}:5432/medevidence',
           '-e', 'DJANGO_SECRET_KEY=' + secrets.token_hex(32), '-e', 'RENDER_EXTERNAL_HOSTNAME=localhost',
           'medevidence-v3-hosted:test')
    names.append(app)
    code = r'''
import requests, re
base='http://localhost:10000'
headers={'Host':'localhost','X-Forwarded-Proto':'https'}
health=requests.get(base+'/api/health/',headers=headers)
assert health.status_code==200 and health.json()['version']=='3.0.0'
for path in ['/', '/profile', '/answer/8', '/thread/1', '/settings']:
    response=requests.get(base+path,headers=headers)
    assert response.status_code==200 and '<div id="root">' in response.text, path
    assert response.headers['X-Frame-Options']=='DENY'
page=requests.get(base,headers=headers).text
asset=re.search(r'src="(/assets/[^\"]+\.js)"',page).group(1)
assert requests.get(base+asset,headers=headers).status_code==200
assert requests.get(base+'/assets/missing.js',headers=headers).status_code==404
assert requests.get(base+'/api/missing/',headers=headers).status_code==404
'''
    last = None
    for _ in range(60):
        last = docker('exec', app, 'python', '-c', code, check=False)
        if last.returncode == 0:
            break
        time.sleep(.5)
    else:
        raise RuntimeError('Hosted image check failed: ' + last.stderr[-2000:])
    result = {'result':'pass', 'scope':'Local single-service hosting image; no public deployment',
              'checks':['Automatic PostgreSQL migration and Gunicorn startup',
                        'Built SPA home and deep links served on the API origin',
                        'Compiled JavaScript served with static security headers',
                        'Missing API routes and assets remain 404 responses']}
    target = Path(__file__).resolve().parents[1] / 'experiments/round-03/hosted-image-smoke.json'
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
finally:
    for name in reversed(names):
        label=docker('inspect','--format','{{index .Config.Labels "medevidence.test"}}',name,check=False)
        if label.returncode==0 and label.stdout.strip()==prefix:
            docker('rm','-f','-v',name,check=False)
    label=docker('network','inspect','--format','{{index .Labels "medevidence.test"}}',prefix,check=False)
    if label.returncode==0 and label.stdout.strip()==prefix:
        docker('network','rm',prefix,check=False)
