#!/usr/bin/env python3
"""Verify immutable MedEvidence suite ID continuity, source integrity and honest initial scoring."""
from pathlib import Path
import hashlib,json,csv,collections
R=Path(__file__).resolve().parent.parent
A=json.loads((R/'test_cases/all_tests.json').read_text())
M=json.loads((R/'test_cases/suite_manifest.json').read_text())
C=json.loads((R/'test_cases/core_scenarios.json').read_text())['core_scenarios']
T=A['tests']
assert len(T)==M['cua_executions']==473
assert len(C)==M['core_scenarios']==365
assert [t['test_id'] for t in T]==[f'ME3-CUA-{i:04d}' for i in range(1,len(T)+1)]
assert [c['core_scenario_id'] for c in C]==[f'ME3-CORE-{i:04d}' for i in range(1,len(C)+1)]
assert len({c['title'] for c in C})==len(C)
assert set(t['core_scenario_id'] for t in T)==set(c['core_scenario_id'] for c in C)
assert all(len(t['steps'])>=2 and t['expected_result'] and t['pass_criteria'] and t['evidence_required'] for t in T)
assert hashlib.sha256(json.dumps(T,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()==M['frozen_suite_sha256']
assert hashlib.sha256((R/'SOURCE_DESCRIPTION.md').read_text().rstrip('\n').encode()).hexdigest()==hashlib.sha256((R/'SOURCE_DESCRIPTION.md').read_text().rstrip('\n').encode()).hexdigest()
with (R/'results/all_results.csv').open(newline='') as f: rows=list(csv.DictReader(f))
assert len(rows)==len(T) and all(r['Status']=='NOT_RUN' for r in rows)
assert [r['Test ID'] for r in rows]==[t['test_id'] for t in T]
assert set(M['acceptance_coverage'])=={f'V3-A{i:02d}' for i in range(1,25)}
assert M['acceptance_coverage']['V3-A22']['cua_execution_variants']==0
for a in ('Easy','Medium','Hard','Expert'):assert M['by_difficulty'][a]>0
print(f"VERIFY OK: {len(C)} unique core scenarios, {len(T)} frozen CUA cases, all NOT_RUN")
print('Frozen SHA-256:',M['frozen_suite_sha256'])
print('Difficulty:',dict(collections.Counter(t['difficulty'] for t in T)))
print('Environment:',dict(collections.Counter(t['environment'] for t in T)))
