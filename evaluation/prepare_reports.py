"""Prepare zero-execution result placeholders and an assumption-driven budget.
Never imports an OpenAI client, accesses keys, or overwrites executed results.
"""
import json,csv,io,hashlib
from pathlib import Path
root=Path('evaluation')
tasks=json.loads((root/'catalog-v1/tasks.json').read_text(encoding='utf-8'))
config=json.loads((root/'config.json').read_text())
def save(path,value): (root/path).write_bytes((json.dumps(value,indent=2,ensure_ascii=False)+'\n').encode())
if (root/'results.json').exists():
    assert all(r['status']=='NOT_RUN' and r['api_response_count']==0 for r in json.loads((root/'results.json').read_text())), 'Never overwrite an executed result'
rows=[]
for t in tasks:
    rows.append({'id':t['id'],'title':t['title'],'difficulty':t['difficulty'],'reporting_group':t['reporting_group'],
      'status':'NOT_RUN','reason':'Preparation only; paid execution not authorized','requested_model':'gpt-5.4','returned_models':[],
      'api_response_count':0,'response_ids':[],'request_ids':[],'native_computer_call_ids':[],'screenshots':[],'action_trace':None,
      'assertions':[{'id':a['id'],'statement':a['statement'],'verdict':'UNVERIFIED','evidence':[]} for a in t['assertions']],
      'input_tokens':0,'cached_input_tokens':0,'output_tokens':0,'estimated_cost_usd':0,'failure_reason':None})
save('results.json',rows)
fields=['id','title','difficulty','reporting_group','status','requested_model','api_response_count','input_tokens','cached_input_tokens','output_tokens','estimated_cost_usd','reason']
out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
(root/'results.csv').write_bytes(out.getvalue().encode('utf-8-sig'))
scenarios={
 'optimistic':([2,4,7,10,15],[2400,2800,3200,3800,4600],[45,60,90,120,160]),
 'central':([3,5,9,13,20],[2600,3100,3600,4400,5500],[50,70,110,150,200]),
 'conservative':([4,7,12,18,28],[3200,3800,4500,5500,7000],[80,100,150,220,300])}
budget={'model':'gpt-5.4','as_of':'2026-11-16','actual_paid_calls':0,'actual_estimated_spend_usd':0,'absolute_project_cap_usd':5,'prices_usd_per_million':config['prices'],
 'separate_native_tool_fee_usd_assumption':0,'app_provider_cost_assumption':'0 only with a verified no-paid/local application model; otherwise BLOCKED',
 'method':'Planning scenarios, not measured token counts. Full original tasks; no cache discount or successful-mock substitution.', 'scenarios':{}}
for name,(calls,inputs,outputs) in scenarios.items():
    data=[]
    for level,count in enumerate([10,20,30,25,15],1):
        idx=level-1;r=count*calls[idx];inp=r*inputs[idx];outp=r*outputs[idx]
        data.append({'difficulty':level,'tasks':count,'responses_per_task':calls[idx],'responses':r,'input_tokens_per_response':inputs[idx],'output_tokens_per_response':outputs[idx],'input_tokens':inp,'output_tokens':outp,'estimated_usd':round((inp*2.5+outp*15)/1e6,6)})
    budget['scenarios'][name]={'by_difficulty':data,'responses':sum(x['responses'] for x in data),'input_tokens':sum(x['input_tokens'] for x in data),'output_tokens':sum(x['output_tokens'] for x in data),'estimated_usd':round(sum(x['estimated_usd'] for x in data),6)}
lookup={t['id']:t for t in tasks};central=budget['scenarios']['central']['by_difficulty']
coverage={}
for ceiling in [3,4,5]:
    cost=0;complete=[]
    for task_id in config['execution_order']:
        t=lookup[task_id];row=central[t['difficulty']-1];next_cost=row['estimated_usd']/row['tasks']
        if cost+next_cost>ceiling-.01:break
        cost+=next_cost;complete.append(task_id)
    coverage[str(ceiling)]={'nominal_whole_tasks':len(complete),'estimated_usd':round(cost,6),'note':'Assumes all prerequisites ready. Per-call reserves may stop earlier or inside next task; not guaranteed. Prespecified stratified order, not easiest-first.'}
budget['central_partial_coverage']=coverage
save('budget.json',budget)
md='# Native CUA results — NOT RUN\n\nNo paid API calls have been authorized or made for this catalog. All 100 tasks are NOT_RUN. Native success rate is **not available**, not 0% or 100%. Offline checks are separate.\n\n| ID | Difficulty | Group | Status |\n|---|---:|---|---|\n'
md+=''.join(f"| {t['id']} | {t['difficulty']} | {t['reporting_group']} | NOT_RUN |\n" for t in tasks)
(root/'RESULTS.md').write_bytes(md.encode())
print(json.dumps({'central_budget':budget['scenarios']['central'],'partial_coverage':coverage},indent=2))
