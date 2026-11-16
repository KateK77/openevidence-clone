"""No network. Reproducible planning scenarios, NOT observed usage or success rates."""
import json,math
from pathlib import Path
H=Path(__file__).resolve().parent
DIFF=['Easy','Medium','Hard','Expert'];N=[30,40,20,10]
SCENARIOS={
 'optimistic':{'requests':[2,4,7,11],'input':[2200,2700,3400,4200],'output':[120,180,250,350]},
 'central':{'requests':[3,6,10,16],'input':[2700,3300,4300,5500],'output':[180,250,350,450]},
 'conservative':{'requests':[5,9,15,24],'input':[3500,4500,6000,8000],'output':[300,450,600,800]},
}
def main():
 report={'model':'gpt-5.4-2026-03-05','unit_rates_per_million':{'input':2.5,'output':15,'cached_input':.25},
  'cache_discount_assumed':False,'native_tool_fee_assumption_usd':0,'native_tool_fee_status':'Not separately itemized in reviewed official price table; confirm applicable rate before paid approval. Unknown fee blocks execution.',
  'viewport_image_tokens':{'1280x768':math.ceil(40*24*1.2),'390x844':math.ceil(13*27*1.2)},
  'application_provider_fees':'Excluded from the CUA arithmetic only when independently confirmed zero. No Gemini calls in this preparation; paid provider usage must share the $10 ceiling or be blocked.',
  'target_usd':5,'absolute_maximum_usd':10,'paid_execution_blocked':True,'actual_bill_cap_verified':False,'scenarios':{}}
 lines=['# Budget scenarios — GPT-5.4 native CUA','',
 'Target budget: $5 USD. Absolute maximum actual charges: $10 USD. Paid dispatch is blocked because an actual-bill guarantee has not been established.', '', 'These are assumption-based forecasts, not measured usage, completed-test counts or pass rates. Every scenario retains all 100 frozen tasks. No caching discount, Batch discount, prepaid credits or automatic top-up is assumed.','']
 for name,s in SCENARIOS.items():
  rows=[]
  for d,n,q,i,o in zip(DIFF,N,s['requests'],s['input'],s['output']):
   cost=q*(i*2.5+o*15)/1e6
   rows.append({'difficulty':d,'tests':n,'expected_requests_per_test':q,'requests':n*q,'input_tokens_per_request':i,'output_tokens_per_request_including_reasoning':o,'input_tokens':n*q*i,'output_tokens':n*q*o,'cost_usd':n*cost,'cost_per_test_usd':cost})
  order=[0,0,0,1,1,1,1,2,2,3]*10;completion={}
  for b in [5,10]:
   spent=0;completed=0
   for j in order:
    # $0.10 cushion retained; actual pre-call maximum-output reservation may stop sooner.
    if spent+rows[j]['cost_per_test_usd']>b-.1:break
    spent+=rows[j]['cost_per_test_usd'];completed+=1
   completion[str(b)]={'forecast_full_task_attempts':completed,'not_completed':100-completed,'spent_forecast':spent,'note':'Not a guarantee of valid assessments; before per-call conservative reservations, prerequisites or CUA errors.'}
  total=sum(r['cost_usd'] for r in rows)
  report['scenarios'][name]={'rows':rows,'total_usd':total,'requests':sum(r['requests'] for r in rows),'token_count_requests':sum(r['requests'] for r in rows),'budget_completion_forecast':completion}
  lines += ['## '+name.title(),'','| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |','|---|---:|---:|---:|---:|---:|---:|']
  for r in rows:lines.append(f'| {r["difficulty"]} | {r["tests"]} | {r["expected_requests_per_test"]} | {r["requests"]} | {r["input_tokens"]:,} | {r["output_tokens"]:,} | ${r["cost_usd"]:.2f} |')
  lines+=['',f'**100-test forecast: ${total:.2f}.**','',*['- $'+b+': '+str(v['forecast_full_task_attempts'])+' full-task attempts forecast; not a predicted pass count.' for b,v in completion.items()],'']
 lines += ['## What explains the earlier estimates?','',
 'The $32.50–110 estimate was located in the different CareConnect-v3 project. It assumed 10–35 million cumulative input tokens and 0.5–1.5 million output tokens. At $2.50/$15 per million, these give exactly $32.50/$110. Its request caps were 30/50/80/120 per difficulty, and it appended the complete screenshot history to every request. Per-action local captures increase storage; only images actually submitted to the API affect tokens. Its desktop capture was up to 1440x1000.',
 '', 'No $3.38 CareFlow EHR usage ledger, model configuration or original estimator was found in the available CareFlow repository. The CareConnect framework is a related patient-portal reference, not proof that the original CareFlow framework has been recovered. A verified task-complexity/request/token/image/model comparison against $3.38 is therefore unavailable. That number must not be called an observed 100-test cost. It could reflect different assumptions, but no explanation is asserted without evidence.',
 '', 'MedEvidence adds live literature, cross-source audits, Chinese synthesis, regeneration and provider-failure prerequisites. This describes its frozen workload, not a proven complexity difference from the missing CareFlow run.',
 '', '## Optimization without changing tasks','',
 '- Exact GPT-5.4 snapshot; standard service tier, low reasoning; output usage includes reasoning tokens.',
 '- 1280x768 desktop and original-resolution 390x844 mobile, device scale 1; no unreadable thumbnail downsampling. Approximate screenshot input: 1,152 / 422 tokens under current 32px patch rules.',
 '- One latest screenshot in each request; retain full original task, criteria, native action transcript and recorded observations. Old screenshots remain in evidence, not in the billed prompt. No previous_response_id chain is claimed to be free.',
 '- Execute model-issued action batches; capture local evidence after each action, reuse the last capture as the batch response, deduplicate identical PNGs by hash. No scripted task solver, paid summarizer or paid judge.',
 '- Request caps 8/14/24/36; action caps 35/70/120/200; these are resource stops, never relaxed acceptance criteria. Exhaustion is an execution error, not an application FAIL.',
 '- Each group of ten scheduled tests contains 3 Easy, 4 Medium, 2 Hard and 1 Expert. Difficult tasks are not pushed to the end merely to maximize inexpensive completions.',
 '', '## Actual-bill ceiling: execution blocked','',
 'The $5 target is a planning target, not authorization. The absolute maximum is $10 of actual charges. The --execute entry point now unconditionally stops before approval/key loading, token counting or HTTP. A config flag or approval JSON cannot bypass it. A reviewed enforceable billing boundary and new explicit user approval are both required to unblock. See BILLING_SAFETY.md.',
 '', 'Local accounting remains defense in depth: reserve uncached counted input with 10% margin, full maximum output and applicable native tool charges before dispatch; retain $0.10 planning headroom; round liabilities upward to microdollars. Persist reservations before sending, allow one request in flight, retain unknown charges on timeout and stop on missing usage or metering discrepancy. Cached usage is settled at its actual cached rate; reasoning is included in output, not charged twice. None of these estimates independently guarantees the actual invoice.',
 '', 'The reviewed pricing table does not separately itemize a local computer-tool fee. Forecast additional tool fee is $0 conditional on confirmation; no hosted container, web search, file search or other billable tool is enabled. An unknown applicable tool rate blocks paid execution. Existing Render/Neon usage is not new CUA tool usage. Any paid application-side LLM cost must be reserved in the same ceiling; the current evaluator disables application LLM calls and blocks live profiles until zero-cost access or a metered allowance is established.',
 '', '## Feasibility','',
 'The central forecast is $10.2105 before any extra fees, already above the $10 absolute maximum; optimistic $5.3975 is above the $5 target, and conservative $23.3475 exceeds both. No valid completion count is guaranteed. The $5/$10 scenario counts assume all prerequisites resolved and represent full task attempts, not passes. Actual dispatch remains zero under the unresolved billing block. Never-executed cases remain NOT_RUN; no paid pilot is approved.',
 '', '## Request-count scope', '', 'Tables count generation requests. The current framework also makes one input-token-count request per generation request (470 / 690 / 1,050 additional requests by scenario); these are not generation retries. Their applicable pricing must be confirmed before execution; no fee is silently assumed away. Only the latest screenshot is submitted, with unchanged task/criteria and all semantic actions/observations. Redundant archive paths, duplicate IDs and timestamps are now omitted from model context. No unmeasured savings are subtracted from the scenario totals.', '', '## Official references checked November 16, 2026','',
 '- https://developers.openai.com/api/docs/models/gpt-5.4',
 '- https://developers.openai.com/api/docs/guides/spend-limits',
 '- https://developers.openai.com/api/docs/pricing',
 '- https://developers.openai.com/api/docs/guides/images-vision',
 '- https://developers.openai.com/api/docs/guides/conversation-state',
 '- https://developers.openai.com/api/docs/guides/tools-computer-use',
 ]
 (H/'budget-estimate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
 (H/'BUDGET_ESTIMATE.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps({k:{'total':v['total_usd'],'requests':v['requests'],'completion':v['budget_completion_forecast']} for k,v in report['scenarios'].items()},indent=2))
if __name__=='__main__':main()
