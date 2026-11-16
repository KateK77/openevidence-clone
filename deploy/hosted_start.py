"""Free Render startup: persistent external database and exactly one worker."""
import os
import re
import subprocess

if not os.environ.get('DATABASE_URL', '').startswith(('postgres://', 'postgresql://')):
    raise RuntimeError('Hosted startup requires persistent PostgreSQL; SQLite is not permitted.')
if not os.environ.get('DJANGO_SECRET_KEY'):
    raise RuntimeError('Set the server secret in the hosting environment.')
hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME', '')
if hostname:
    if not re.fullmatch(r'[a-zA-Z0-9.-]+', hostname):
        raise RuntimeError('Invalid hosting hostname.')
    os.environ.setdefault('DJANGO_ALLOWED_HOSTS', hostname)
    os.environ.setdefault('DJANGO_CSRF_TRUSTED_ORIGINS', 'https://' + hostname)
os.environ['DJANGO_DEBUG'] = '0'
os.environ['TRUST_PROXY_HTTPS'] = '1'
port = int(os.environ.get('PORT', '10000'))
if not 1 <= port <= 65535:
    raise RuntimeError('Invalid server port.')
subprocess.run(['python', 'manage.py', 'migrate', '--noinput'], check=True, timeout=180)
if os.environ.get('PUBLIC_DEMO') == '1':
    subprocess.run(['python', 'manage.py', 'seed_public_demo'], check=True, timeout=60)
os.execvp('gunicorn', ['gunicorn', 'evidence.hosted_wsgi:application', '--bind', f'0.0.0.0:{port}',
                     '--workers', '1', '--threads', '4', '--timeout', '300', '--access-logfile', '-'])
