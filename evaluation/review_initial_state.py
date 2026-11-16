import hashlib,json
from pathlib import Path
root=Path('evaluation/catalog-v1');p=root/'tasks.json';tasks=json.loads(p.read_text(encoding='utf-8'));f=json.loads((root/'freeze.json').read_text(encoding='utf-8'))
if (root/'AUTHORING_REVIEW.json').exists(): raise SystemExit('Authoring correction already recorded; frozen catalog must not be overwritten')
old=f.copy()
for t in tasks:
 t['initial_state']['authentication']='Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.'
 t['initial_state']['data']='Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.'
 if t['id']=='ME-086': t['user_role']='Anonymous, becoming a new synthetic researcher'
p.write_bytes((json.dumps(tasks,ensure_ascii=False,indent=2)+'\n').encode())
md=(root/'TASKS.md').read_text(encoding='utf-8')
md=md.replace('none for login/registration/logout-under-test; preauthenticated synthetic session only where sign-in is not the task',tasks[0]['initial_state']['authentication'])
md=md.replace('global fixture contract plus named task fixtures; no previous benchmark task dependency',tasks[0]['initial_state']['data'])
section=md.index('## ME-086:');end=md.index('## ME-087:',section)
md=md[:section]+md[section:end].replace('Role: Researcher A','Role: Anonymous, becoming a new synthetic researcher')+md[end:]
(root/'TASKS.md').write_bytes(md.encode())
f.update(catalog_version='1.0.1',tasks_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),task_markdown_sha256=hashlib.sha256((root/'TASKS.md').read_bytes()).hexdigest(),authoring_correction='Clarified login/logout initial state and prospective researcher role before any benchmark execution; no goals, levels or assertions changed.')
(root/'freeze.json').write_text(json.dumps(f,indent=2)+'\n',encoding='utf-8')
(root/'AUTHORING_REVIEW.json').write_text(json.dumps({'prior_freeze':old,'new_catalog_version':'1.0.1','change':'Initial-state clarification only; login anonymous, logout authenticated, new-account journey starts anonymous; fixtures explicitly labelled.','paid_calls_before_change':0,'native_results_seen':False,'goals_difficulty_and_assertions_changed':False},indent=2)+'\n',encoding='utf-8')
print(f['tasks_sha256'])
