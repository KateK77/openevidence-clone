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
           '-e', 'PUBLIC_DEMO=1', '-e', 'PUBLIC_DEMO_DAILY_CALLS=2', '-e', 'PUBLIC_DEMO_TOTAL_CALLS=3',
           '-e', 'DJANGO_SECRET_KEY=' + secrets.token_hex(32), '-e', 'RENDER_EXTERNAL_HOSTNAME=localhost',
           'medevidence-portfolio:test')
    names.append(app)
    code = r'''
import requests, re
base='http://localhost:10000'
headers={'Host':'localhost','X-Forwarded-Proto':'https'}
health=requests.get(base+'/api/health/',headers=headers)
assert health.status_code==200 and health.json()['database']=='postgresql'
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
    quota_check = r"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','evidence.settings')
import django;django.setup()
from concurrent.futures import ThreadPoolExecutor
from django.db import close_old_connections
from evidence.llm import reserve_demo_call, ModelError
from evidence.models import ModelCallBudget
from django.contrib.auth.models import User
from django.core.management import call_command
u=User.objects.get(username='portfolio_researcher');original=u.password
call_command('seed_public_demo');u.refresh_from_db();assert u.password==original
assert u.check_password('MedEvidence-Demo-2026!') and not u.is_staff
assert User.objects.filter(username='portfolio_reader').exists()
def take(_):
 close_old_connections()
 try: reserve_demo_call();return True
 except ModelError: return False
 finally: close_old_connections()
with ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(take,range(6)))
assert sum(results)==2,results
assert ModelCallBudget.objects.get().total_calls==2
print('Protected seeding and concurrent PostgreSQL allowance passed')
"""
    checked=docker('exec',app,'python','-c',quota_check)
    print(checked.stdout.strip())
    result = {'result':'pass', 'scope':'Local single-service hosting image; no public deployment',
              'checks':['Automatic PostgreSQL migration and Gunicorn startup',
                        'Built SPA home and deep links served on the API origin',
                        'Compiled JavaScript served with static security headers',
                        'Missing API routes and assets remain 404 responses',
                        'Opt-in synthetic seeding is idempotent and nonprivileged',
                        'Six concurrent PostgreSQL quota reservations admit exactly two calls']}
    target = Path(__file__).resolve().parents[1] / 'experiments/portfolio-release/hosted-image-smoke.json'
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
