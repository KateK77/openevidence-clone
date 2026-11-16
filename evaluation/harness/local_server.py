"""Isolated evaluator infrastructure, not application changes or a task solver.

Default: no provider credentials, loopback-only network, new SQLite DB per start.
Only an explicitly selected pubmed profile permits official NCBI retrieval.
"""
import os, sys, json, socket, secrets, mimetypes
from pathlib import Path
from datetime import timedelta
from wsgiref.simple_server import make_server
from socketserver import ThreadingMixIn
from wsgiref.simple_server import WSGIServer

ROOT=Path(__file__).resolve().parents[2]
folder=Path(sys.argv[1]).resolve(); port=int(sys.argv[2]); profile=sys.argv[3]; test_id=sys.argv[4] if len(sys.argv)>4 else ''
folder.mkdir(parents=True,exist_ok=True)
db=folder/'test.sqlite3'
if db.exists():raise RuntimeError('Refusing to reset or reuse an existing evaluation database')
if profile not in ('offline','pubmed'):raise RuntimeError('Live/fault prerequisites require separately reviewed adapters; do not substitute mocks')
os.environ.update(PYTHON_DOTENV_DISABLED='1',DATABASE_URL='sqlite:///'+db.as_posix(),
    DJANGO_DEBUG='1',DJANGO_SECRET_KEY=secrets.token_hex(40),DJANGO_SETTINGS_MODULE='evidence.settings',
    DJANGO_ALLOWED_HOSTS='127.0.0.1,localhost',DJANGO_CSRF_TRUSTED_ORIGINS=f'http://127.0.0.1:{port}',
    LLM_API_KEY='',LLM_MODEL='',LLM_BASE_URL='http://127.0.0.1:9',LLM_PROVIDER='compatible',NCBI_API_KEY='',NCBI_EMAIL='',REDIS_URL='')
native_connect=socket.socket.connect
def guarded_connect(sock,address):
    host=address[0]
    if host not in ('127.0.0.1','::1','localhost'):
        if profile=='offline':raise OSError('Offline evaluator blocks external network')
    return native_connect(sock,address)
socket.socket.connect=guarded_connect
sys.path.insert(0,str(ROOT/'backend'))
import django
django.setup()
from django.core.management import call_command
call_command('migrate',interactive=False,verbosity=0)
from django.contrib.auth.models import User
from django.utils import timezone
from evidence.models import Conversation,Turn,Publication,Evidence,SavedPublication,Preferences
users={}
for name in ('a','b'):
    password=secrets.token_urlsafe(22)+'!9a'
    user=User.objects.create_user('evaluation_'+name,password=password)
    users[name]={'username':user.username,'password':password}
    Preferences.objects.create(user=user)
record={'pmid':'33567185','title':'Once-Weekly Semaglutide in Adults with Overweight or Obesity.',
 'authors':['John P H Wilding','Rachel L Batterham','STEP 1 Study Group'],
 'journal':'The New England journal of medicine','year':'2021','date':'2021 02 10',
 'date_type':'Electronic publication','doi':'10.1056/NEJMoa2032183','url':'https://pubmed.ncbi.nlm.nih.gov/33567185/',
 'abstract':'','types':['Randomized Controlled Trial'],'fixture_note':'Historical user-supplied metadata subset, not a live retrieval; full abstract deliberately unavailable.'}
p=Publication.objects.create(pmid=record['pmid'],record=record)
threads=[]
for username in ('evaluation_a','evaluation_b'):
    owner=User.objects.get(username=username)
    for i in range(3 if username.endswith('_a') else 1):
        c=Conversation.objects.create(owner=owner,title=f'SYNTHETIC Acceptance fixture {username} {i}')
        Conversation.objects.filter(pk=c.pk).update(created=timezone.now()-timedelta(days=i),updated=timezone.now()-timedelta(days=i))
        t=Turn.objects.create(conversation=c,question='SYNTHETIC workflow fixture: GLP-1 obesity research',status='retrieval_only',
            result={'message':'Synthetic evaluation history fixture; no generated medical answer.'},saved=username.endswith('_a') and i==0,
            provenance={'fixture':True,'pipeline_version':'round-03','searches':[],'previous_questions':[]})
        Evidence.objects.create(turn=t,publication=p,rank=1,snapshot=record)
        threads.append({'owner':username,'conversation':c.pk,'answer':t.pk})
if test_id not in ('T039','T040'):
    SavedPublication.objects.create(owner=User.objects.get(username='evaluation_a'),publication=p,collection='Initial research' if test_id=='T042' else 'Obesity research')
(folder/'manifest.json').write_text(json.dumps({'accounts':users,'threads':threads,'fixture':'Synthetic account/history data; source metadata subset; not live clinical evidence.'}),encoding='utf-8')
from django.core.wsgi import get_wsgi_application
django_app=get_wsgi_application()
dist=Path(os.environ['EVAL_FRONTEND_DIST']).resolve()
def application(env,start):
    uri=env.get('PATH_INFO','/')
    if uri=='/__evaluation_scratch':
        start('200 OK',[('Content-Type','text/html; charset=utf-8')]);return [b'<h1>Evaluation scratchpad (not application UI)</h1><textarea aria-label="Clipboard verification"></textarea>']
    if uri.startswith('/api/'):
        return django_app(env,start)
    file=(dist/uri.lstrip('/')).resolve()
    if not file.is_relative_to(dist):start('403 Forbidden',[]);return [b'Forbidden']
    if not file.is_file():file=dist/'index.html'
    start('200 OK',[('Content-Type',mimetypes.guess_type(file.name)[0] or 'application/octet-stream')]);return [file.read_bytes()]
class Threaded(ThreadingMixIn,WSGIServer):daemon_threads=True
with make_server('127.0.0.1',port,application,server_class=Threaded) as server:server.serve_forever()
