"""Hash public preparation artifacts; never sweep ignored private runtime evidence."""
import hashlib,json,sys
from pathlib import Path
root=Path('evaluation')
manifest=root/'EVIDENCE_MANIFEST.json'
if '--verify' in sys.argv:
    record=json.loads(manifest.read_text(encoding='utf-8'))
    for entry in record['files']:
        p=root/entry['path']
        assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],str(p)
    print(f"Verified {len(record['files'])} public preparation artifacts; native evidence count = 0")
else:
    files=[]
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if not p.is_file() or p==manifest or any(x in ('private','.runtime','__pycache__') for x in rel.parts): continue
        files.append({'path':rel.as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'kind':'preparation_or_offline_check'})
    manifest.write_bytes((json.dumps({'schema_version':1,'stage':'PREPARATION_ONLY','native_api_evidence_count':0,'hash_algorithm':'SHA-256','files':files},indent=2)+'\n').encode())
    print(f'Hashed {len(files)} preparation artifacts')
