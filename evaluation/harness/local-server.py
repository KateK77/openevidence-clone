"""Fresh synthetic DB and pinned hosted WSGI. No task actions, no external network.

Scripted fixtures/session creation are evaluator setup, never native CUA evidence.
Provider-fault/live-model/legacy prerequisites are deliberately fail-closed.
"""
import os, sys, json, socket, secrets
from pathlib import Path
from datetime import timedelta
from socketserver import ThreadingMixIn
from wsgiref.simple_server import make_server, WSGIServer

ROOT=Path(__file__).resolve().parents[2]
folder=Path(sys.argv[1]).resolve(); port=int(sys.argv[2]); test_id=sys.argv[3]
folder.mkdir(parents=True,exist_ok=True)
db=folder/'test.sqlite3'
if db.exists(): raise RuntimeError('An existing evaluation DB cannot be reset/reused')
for key in list(os.environ):
    if any(x in key.upper() for x in ('API_KEY','DATABASE_URL','REDIS_URL','TOKEN','SECRET','PROXY')): os.environ.pop(key,None)
os.environ.update(PYTHON_DOTENV_DISABLED='1',DATABASE_URL='sqlite:///'+db.as_posix(),
    DJANGO_DEBUG='1',DJANGO_SECRET_KEY=secrets.token_hex(40),DJANGO_SETTINGS_MODULE='evidence.settings',
    DJANGO_ALLOWED_HOSTS='127.0.0.1,localhost',DJANGO_CSRF_TRUSTED_ORIGINS=f'http://127.0.0.1:{port}',
    LLM_API_KEY='',LLM_MODEL='',LLM_BASE_URL='http://127.0.0.1:9',LLM_PROVIDER='compatible',
    NCBI_API_KEY='',NCBI_EMAIL='',REDIS_URL='',FRONTEND_DIST=str(ROOT/'frontend'/'dist'))
original_connect=socket.socket.connect
original_connect_ex=socket.socket.connect_ex
def check(address):
    if address[0] not in ('127.0.0.1','::1','localhost'): raise OSError('Offline benchmark blocks external connections')
def connect(sock,address): check(address); return original_connect(sock,address)
def connect_ex(sock,address): check(address); return original_connect_ex(sock,address)
socket.socket.connect=connect; socket.socket.connect_ex=connect_ex
sys.path.insert(0,str(ROOT/'backend'))
import django
django.setup()
from django.core.management import call_command
call_command('migrate',interactive=False,verbosity=0)
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth import SESSION_KEY, BACKEND_SESSION_KEY, HASH_SESSION_KEY
from django.utils import timezone
from evidence.models import Conversation,Turn,Publication,Evidence,SavedPublication,Preferences
users={}; sessions={}
for suffix in ('a','b'):
    password=secrets.token_urlsafe(22)+'!9a'
    user=User.objects.create_user('eva_'+suffix,password=password)
    users[suffix]={'username':user.username,'password':password}; Preferences.objects.create(user=user)
    session=SessionStore(); session[SESSION_KEY]=str(user.pk)
    session[BACKEND_SESSION_KEY]='django.contrib.auth.backends.ModelBackend'
    session[HASH_SESSION_KEY]=user.get_session_auth_hash(); session.save(); sessions[suffix]=session.session_key
records=[]
for index in (1,2):
    record={'pmid':str(90000000+index),'title':f'SYNTHETIC benchmark source {index} (not a real paper)',
      'authors':['Synthetic Evaluator'],'journal':'SYNTHETIC Fixture Journal','year':'2020','date':'2020',
      'date_type':'Publication year only','doi':'','url':'','abstract':'SYNTHETIC fixture only. No clinical claims.',
      'types':['Journal Article'],'fixture_note':'Not retrieved from PubMed; not clinical evidence.'}
    records.append(Publication.objects.create(pmid=record['pmid'],record=record))
threads=[]
if test_id!='ME-010':
    for suffix in ('a','b'):
        owner=User.objects.get(username='eva_'+suffix)
        for index in range(3 if suffix=='a' else 1):
            conv=Conversation.objects.create(owner=owner,title=f'SYNTHETIC fixture {suffix} {index}')
            Conversation.objects.filter(pk=conv.pk).update(created=timezone.now()-timedelta(days=index),updated=timezone.now()-timedelta(days=index))
            turn=Turn.objects.create(conversation=conv,question='SYNTHETIC workflow fixture / 合成测试记录',
              status='complete',model='SYNTHETIC FIXTURE (not a provider)',result={'message':'SYNTHETIC fixture; not generated medical evidence. 合成测试。','language':'Chinese','sections':[{'text':'SYNTHETIC bilingual fixture / 合成测试内容，仅供导出与界面测试。','kind':'limitation','status':'insufficient','citations':[]}]},
              saved=suffix=='a' and index==0 and test_id not in ('ME-006','ME-038','ME-039'),
              provenance={'fixture':True,'pipeline_version':'round-03','searches':[],'previous_questions':[]})
            Evidence.objects.create(turn=turn,publication=records[0],rank=1,snapshot=records[0].record)
            threads.append({'owner':'eva_'+suffix,'conversation':conv.pk,'answer':turn.pk})
if test_id!='ME-007': SavedPublication.objects.create(owner=User.objects.get(username='eva_a'),publication=records[0],collection='SYNTHETIC collection')
(folder/'manifest.private.json').write_text(json.dumps({'accounts':users,'sessions':sessions,'threads':threads}),encoding='utf-8')
from evidence.hosted_wsgi import application as pinned_application
def application(environ,start_response):
    def tagged(status,headers,exc_info=None):
        return start_response(status,headers+[('X-Benchmark-Instance',folder.name)],exc_info)
    return pinned_application(environ,tagged)
class Threaded(ThreadingMixIn,WSGIServer): daemon_threads=True
with make_server('127.0.0.1',port,application,server_class=Threaded) as server: server.serve_forever()
