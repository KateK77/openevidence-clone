#!/usr/bin/env python3
"""Validate MedEvidence independent frozen CUA suite and evidence-based results."""
import collections,csv,hashlib,json,pathlib,sys,datetime,re
ROOT=pathlib.Path(__file__).resolve().parent.parent
obj=json.loads((ROOT/'test_cases/all_tests.json').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'test_cases/suite_manifest.json').read_text(encoding='utf-8'))
tests=obj['tests']
canonical=json.dumps(tests,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')
actual_sha=hashlib.sha256(canonical).hexdigest()
assert actual_sha == manifest['frozen_suite_sha256'] == obj['frozen_suite_sha256'],'FROZEN SUITE CHANGED: STOP'
expected=[t['test_id'] for t in tests]
assert len(expected)==len(set(expected))==manifest['cua_executions'],'Missing/duplicate test IDs'
with (ROOT/'results/all_results.csv').open(newline='',encoding='utf-8-sig') as f: results=list(csv.DictReader(f))
assert len(results)==len(expected),'Result row count != frozen suite count'
byid={r['Test ID']:r for r in results}
assert len(byid)==len(results) and set(byid)==set(expected),'Result Test IDs differ from frozen suite'
valid={'PASS','FAIL','BLOCKED','NOT_RUN'}
for r in results:
 s=r['Status']
 assert s in valid,(r['Test ID'],s)
 if s in {'PASS','FAIL'}:
  assert r.get('Observed Result','').strip(),f'Missing observed result for {r["Test ID"]}'
  assert r.get('Evidence Paths','').strip(),f'Missing screenshot evidence paths for {r["Test ID"]}'
  for exact in (f'evidence/{r["Test ID"]}/before.png',f'evidence/{r["Test ID"]}/after.png'):
   assert exact in r['Evidence Paths'],f'Expected real screenshot reference {exact}'
   assert (ROOT/exact).is_file(),f'Missing real screenshot file {exact}'
  assert r.get('Action Trace Path','').strip(),f'Missing action trace for {r["Test ID"]}'
  assert (ROOT/r['Action Trace Path']).is_file(),f'Missing real action trace file for {r["Test ID"]}'
  assert r.get('Executed At (ISO8601)','').strip(),f'Missing execution time for {r["Test ID"]}'
  assert 'chrome' in r.get('Browser','').lower(),f'Result must identify real Google Chrome for {r["Test ID"]}'
  assert r.get('Tested Git SHA','').strip(),f'Missing tested SHA for {r["Test ID"]}'
 if s in {'FAIL','BLOCKED'}:assert r.get('Failure or Block Reason','').strip(),f'Missing reason for {r["Test ID"]}'
def summarize(cases):
 counts=collections.Counter(byid[t['test_id']]['Status'] for t in cases)
 n=len(cases); definitive=counts['PASS']+counts['FAIL']
 return dict(total=n,**{s:counts[s] for s in ('PASS','FAIL','BLOCKED','NOT_RUN')},overall_pass_rate_pct=round(100*counts['PASS']/n,2) if definitive else None,executed_pass_rate_pct=round(100*counts['PASS']/definitive,2) if definitive else None,definitive_coverage_pct=round(100*definitive/n,2) if n else None)
def group(key):return {v:summarize([t for t in tests if t[key]==v]) for v in sorted({t[key] for t in tests})}
unique=collections.defaultdict(list)
for t in tests:unique[t['core_scenario_id']].append(t)
report=dict(source_description_sha256=manifest['source_description_sha256'],frozen_suite_sha256=actual_sha,total=summarize(tests),by_difficulty=group('difficulty'),by_module=group('module'),by_environment=group('environment'),by_fixture_gate=group('fixture_gate'),unique_core_scenarios=len(unique),core_with_definitive_execution=sum(any(byid[t['test_id']]['Status'] in {'PASS','FAIL'} for t in group) for group in unique.values()),core_all_variants_passed=sum(all(byid[t['test_id']]['Status']=='PASS' for t in group) for group in unique.values()))
reports=ROOT/'reports';reports.mkdir(exist_ok=True)
(reports/'live_summary.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
lines=['# Real CUA results — no invented outcomes','', 'Results below are computed exclusively from recorded rows in `results/all_results.csv`. An unrun suite has no measured pass rate.', '', '## Overall', '', '| Metric | Value |','|---|---:|']
for k,v in report['total'].items():lines.append(f'| {k} | {v if v is not None else "N/A"} |')
for key in ['by_difficulty','by_module','by_environment','by_fixture_gate']:
 lines+=['',f'## {key.replace("by_", "").replace("_", " ").title()}','', '| Group | Total | PASS | FAIL | BLOCKED | NOT_RUN | Overall % | Executed % |','|---|---:|---:|---:|---:|---:|---:|---:|']
 for v,p in report[key].items():
  fmt=lambda x:'N/A' if x is None else x
  lines.append(f'| {v} | {p["total"]} | {p["PASS"]} | {p["FAIL"]} | {p["BLOCKED"]} | {p["NOT_RUN"]} | {fmt(p["overall_pass_rate_pct"])} | {fmt(p["executed_pass_rate_pct"])} |')
lines+=['','## Core scenarios','',f'- Unique core scenarios: {report["unique_core_scenarios"]}',f'- At least one definitive variant: {report["core_with_definitive_execution"]}',f'- All variants PASS: {report["core_all_variants_passed"]}']
(reports/'live_summary.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps(report['total'],ensure_ascii=False,indent=2))
