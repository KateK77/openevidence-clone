"""Render reviewed results only. Preflight checks never become CUA verdicts."""
import json,csv,html
from pathlib import Path
from collections import Counter
H=Path(__file__).resolve().parent
def main():
    load=lambda p:json.loads((H/p).read_text(encoding='utf-8'))
    tests=load('final_test_cases_100.json')['tests'];results=load('final_results_100.json');by={r['id']:r for r in results['tests']}
    assert set(by)=={t['id'] for t in tests}
    counts=Counter(r['status'] for r in by.values());valid=counts['PASS']+counts['FAIL']
    for r in by.values():
        if r['status'] in ('PASS','FAIL') and not (r.get('independent_review') and r.get('evidence')):
            raise RuntimeError('Reviewed criterion evidence required for '+r['id'])
    freeze=load('freeze.json');pre=load('logs/offline-preflight.json');budget=load('budget-estimate.json')
    lines=['# MedEvidence final evaluation — NOT EXECUTED','',
      '**Preparation report; no paid native CUA evaluation has started.**' if not results['execution_started'] else '**Execution report — inspect completeness below.**','',
      f'Application baseline: `{freeze["application_commit"]}`. Model planned: `gpt-5.4-2026-03-05`.',
      f'Paid native requests: {results["paid_requests"]}. Estimated API spending recorded: ${results["estimated_api_cost_usd"]:.2f}.',
      '', '| Status | Count |','|---|---:|',*[f'| {s} | {counts[s]} |' for s in ['PASS','FAIL','BLOCKED','ERROR','NOT_RUN']],
      '',f'Primary scheduled ratio: {counts["PASS"]}/100 = {counts["PASS"]}%. This is **not a measured success rate** while all cases remain unexecuted.',
      f'Validly evaluated pass rate: {counts["PASS"]/valid*100:.2f}%.' if valid else 'Validly evaluated pass rate: **N/A (no validly evaluated tests)**.',
      '', '## Difficulty summary','', '| Difficulty | Total | PASS | FAIL | BLOCKED | ERROR | NOT_RUN | Scheduled pass ratio |', '|---|---:|---:|---:|---:|---:|---:|---:|']
    for d in ['Easy','Medium','Hard','Expert']:
        rows=[by[t['id']] for t in tests if t['difficulty']==d];n=Counter(r['status'] for r in rows)
        lines.append(f'| {d} | {len(rows)} | {n["PASS"]} | {n["FAIL"]} | {n["BLOCKED"]} | {n["ERROR"]} | {n["NOT_RUN"]} | {100*n["PASS"]/len(rows):.0f}% (unexecuted) |')
    lines+=['','## Functional categories','','| Category | Total | PASS | FAIL | BLOCKED | ERROR | NOT_RUN |','|---|---:|---:|---:|---:|---:|---:|']
    for cat in dict.fromkeys(t['functional_category'] for t in tests):
        subset=[by[t['id']] for t in tests if t['functional_category']==cat];n=Counter(r['status'] for r in subset)
        lines.append('| '+cat+' | '+str(len(subset))+' | '+' | '.join(str(n[s]) for s in ['PASS','FAIL','BLOCKED','ERROR','NOT_RUN'])+' |')
    lines+=['','## Free preflight and limitations','',
      f'Offline infrastructure: {pre["result"]}; {len(pre["checks"])} checks recorded. Harness unit tests: see logs/harness-unit-tests.tap. Browser/SQLite checks used fresh synthetic data with application LLM credentials removed and external networking blocked.',
      'The first restricted-environment server start did not become ready; rerunning the same offline preflight with local process permission passed. This was an infrastructure rerun with zero API requests, not a paid test retry.',
      'No live PubMed, Gemini, OpenAI model entitlement, native paid compatibility, provider-fault fixture or hosted restart was validated in this offline run. See PREREQUISITE_READINESS.md for all 26 explicitly blocked prerequisites and BILLING_SAFETY.md for the global paid-execution block.',
      '', '## Budget','',
      'Central estimate: $10.21 for 100 tasks; optimistic $5.40; conservative $23.35. These are forecasts, not actual charges. $5 and $10 central scenarios forecast 49 and 99 full task attempts before conservative call reservations/prerequisite failures. Neither is a promised valid completion count. Full assumptions and per-difficulty token totals are in BUDGET_ESTIMATE.md.',
      'Local computer-tool surcharge is not separately itemized in reviewed pricing; $0 is conditional, and unconfirmed applicable fees block paid execution. No other billable tools are enabled. Paid application-side provider costs must also fit the shared $10 ceiling.',
      '', 'Actual invoice cap is unverified. The runner blocks --execute before any HTTP even with an approval file. All 26 additional prerequisite cases are individually documented; none has been silently downgraded or removed. See BILLING_SAFETY.md and PREREQUISITE_READINESS.md.', '', '## Findings','',
      'No benchmark application defects or passes are asserted before execution. The previously observed Gemini verification failure is historical development evidence, not a result for any frozen case. Live and fault-profile prerequisites remain incomplete. Native API trace files do not exist yet because generating them would require unapproved paid calls.',
      '', '## Per-case results','']
    with (H/'summary.csv').open('w',encoding='utf-8',newline='') as stream:
        writer=csv.writer(stream);writer.writerow(['id','difficulty','category','status','reason','requests','actions','input_tokens','output_tokens','estimated_cost_usd'])
        for t in tests:
            r=by[t['id']];writer.writerow([t['id'],t['difficulty'],t['functional_category'],r['status'],r['reason'],r['model_requests'],r['actions'],r['input_tokens'],r['output_tokens'],r['estimated_cost_usd']])
            lines += [f'### {t["id"]} — {t["title"]}', '',f'Difficulty: **{t["difficulty"]}**. Status: **{r["status"]}**.', '', 'Expected: '+t['expected_result'], '', 'Actual: '+r.get('actual_outcome','No native CUA attempt.'), '', 'Reason: '+r['reason'], '', 'Evidence: '+(', '.join(r['evidence']) or 'None — not executed.'), '']
    (H/'FINAL_EVALUATION_REPORT.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    esc=html.escape
    rows=''.join('<tr><td>'+t['id']+'</td><td>'+t['difficulty']+'</td><td><details><summary>'+esc(t['title'])+'</summary><ol>'+''.join('<li>'+esc(s)+'</li>' for s in t['expected_workflow'])+'</ol><p>'+esc(t['expected_result'])+'</p></details></td><td>'+by[t['id']]['status']+'</td></tr>' for t in tests)
    page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MedEvidence — Frozen CUA Evaluation</title><style>body{font:16px/1.6 system-ui;margin:0;background:#f4f8f7;color:#173537}main{max-width:1100px;margin:auto;padding:32px}h1{font-size:36px;line-height:1.15}.banner{padding:20px;background:#e3eee8;border-left:5px solid #176b61}table{width:100%;border-collapse:collapse;background:white}td,th{padding:12px;border-bottom:1px solid #dde6e2;text-align:left;vertical-align:top}a{color:#086c62}input{padding:12px;width:min(90%,500px);margin:18px 0}summary{cursor:pointer}img{max-width:100%;border:1px solid #ccd}small{color:#567}</style><main><h1>MedEvidence<br>Frozen native CUA evaluation</h1><div class="banner"><strong>PREPARATION ONLY — 100 NOT_RUN</strong><br>Paid requests: 0 · API spending: $0.00 · No measured benchmark pass rate</div><p>GPT-5.4 · 30 Easy / 40 Medium / 20 Hard / 10 Expert. Original requirements and acceptance criteria are frozen. No application code was changed.</p><p><a href="FINAL_TEST_CASES.md">Full test specification</a> · <a href="FINAL_EVALUATION_REPORT.md">Status report</a> · <a href="BUDGET_ESTIMATE.md">Budget assumptions</a> · <a href="logs/offline-preflight.json">Offline evidence</a></p><h2>Budget, not a completion promise</h2><p>100-task forecast: <strong>$10.21 central</strong> ($5.40 optimistic; $23.35 conservative). Target $5; absolute actual-charge ceiling $10. Paid dispatch is blocked: an enforceable actual-bill bound is unverified. New explicit approval alone cannot bypass this block.</p><p>Free infrastructure preflight passed. Live model/fault/hosted prerequisites remain unverified. Unexecuted tests are not failures.</p><p><a href="BILLING_SAFETY.md">Actual billing block</a> · <a href="PREREQUISITE_READINESS.md">26-case prerequisite assessment</a></p><h2>100 frozen cases</h2><label>Filter cases <input id="q" placeholder="ID, difficulty, or workflow"></label><table><thead><tr><th>ID</th><th>Difficulty</th><th>Workflow and criteria</th><th>Status</th></tr></thead><tbody>'''+rows+'''</tbody></table><h2>Offline screenshots — not native CUA evidence</h2>'''
    for name in ['screenshot','mobile_screenshot']:
        if pre.get(name):page+='<p><img loading="lazy" src="'+esc(pre[name])+'" alt="Offline infrastructure screenshot"></p>'
    page+='''<p><small>Private repository artifact. No public Pages deployment or full 100-test evaluation is claimed.</small></p></main><script>document.querySelector('#q').addEventListener('input',e=>{for(const r of document.querySelectorAll('tbody tr'))r.hidden=!r.textContent.toLowerCase().includes(e.target.value.toLowerCase())})</script></html>'''
    (H/'index.html').write_text(page,encoding='utf-8')
if __name__=='__main__':main()
