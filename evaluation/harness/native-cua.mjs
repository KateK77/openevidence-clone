/** Paid entry point. Never invoked by preflight. No application UI task scripting. */
import {readFile,mkdir,writeFile,open,unlink} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {resolve} from 'node:path';
import {hash,read,write,Stop,validateApproval,reserveCost,canSpend,usageCost,orderTests,payload,executeAction,capture} from './core.mjs';
import {root,evaldir,prepare} from './environment.mjs';
export async function verifyFreeze(){
 const f=await read(evaldir+'/freeze.json');
 for(const [p,h] of Object.entries(f.files))if(hash(await readFile(evaldir+'/'+p))!==h)throw new Stop('Frozen file changed: '+p,'BLOCKED');
 execFileSync('git',['diff','--exit-code',f.application_commit,'--','backend','frontend','experiments/round-03/consolidated-prompt.md'],{cwd:root,stdio:'pipe'});
 return f;
}
async function main(){
 if(!process.argv.includes('--execute')){console.log('CHECK ONLY: no paid execution. Use preflight.mjs. Explicit approval is required.');return;}
 const f=await verifyFreeze(),configRaw=await readFile(evaldir+'/config.json'),c=JSON.parse(configRaw),a=await read(evaldir+'/approval.local.json');
 validateApproval(a,c,f.files['final_test_cases_100.json'],hash(configRaw));
 if(!process.env.OPENAI_API_KEY)throw new Stop('OPENAI_API_KEY must be supplied privately','BLOCKED');
 const priv=evaldir+'/.private';await mkdir(priv,{recursive:true});
 const lock=await open(priv+'/paid.lock','wx');await lock.close();
 // Persistent ledger cannot be reset via CLI. Ambiguous charge or existing lock stops resumption.
 const lp=priv+'/ledger.json';let ledger;
 try{ledger=await read(lp)}catch(e){if(e.code!=='ENOENT')throw e;ledger={spent_usd:0,unknown_usd:0,requests:0,attempts:[],events:[]};await write(lp,ledger)}
 let results;try{results=await read(priv+'/execution-results.json')}catch(e){if(e.code!=='ENOENT')throw e;results=await read(evaldir+'/final_results_100.json')}
 const tests=orderTests((await read(evaldir+'/final_test_cases_100.json')).tests);
 const save=async()=>{results.paid_requests=ledger.requests;results.estimated_api_cost_usd=ledger.spent_usd;results.unknown_reserved_usd=ledger.unknown_usd;await write(priv+'/execution-results.json',results);await write(lp,ledger)};
 async function api(path,body){
   const r=await fetch('https://api.openai.com/v1/'+path,{method:'POST',headers:{Authorization:'Bearer '+process.env.OPENAI_API_KEY,'Content-Type':'application/json'},body:JSON.stringify(body),signal:AbortSignal.timeout(c.api_timeout_ms)});
   if(!r.ok)throw new Stop('OpenAI HTTP '+r.status+'; no automatic retry');return r.json();
 }
 try{
  for(const test of tests){
   if(ledger.attempts.includes(test.id))continue; // Never silently rerun an attempted task.
   canSpend(ledger,reserveCost(1,c),a,c);
   const r=results.tests.find(x=>x.id===test.id),limits=c.limits[test.difficulty],folder=priv+'/'+test.id;
   if(!['offline','pubmed'].includes(test.preconditions.profile)){r.status='BLOCKED';r.reason='Required live/fault/hosted prerequisite adapter not provisioned; no CUA call made.';await save();continue;}
   let driver;const start=Date.now();
   try{
    driver=await prepare(folder,test.preconditions.profile,/Mobile/.test(test.title)?c.mobile_viewport:c.viewport,test.id);
    const viewport=driver.page.viewportSize(),fixture={...driver.manifest,origin:driver.origin,scratch:driver.origin+'/__evaluation_scratch'};
    let shot=await capture(driver,folder+'/screenshots'),last={image:shot.image},transcript=[];
    r.evidence.push(shot.file);ledger.attempts.push(test.id);results.execution_started=true;await save();
    while(true){
     if(r.model_requests>=limits.requests||r.actions>=limits.actions||Date.now()-start>limits.seconds*1000)throw new Stop('Execution limit reached; criterion not automatically failed');
     const body=payload(test,fixture,transcript,last,c);
     await write(folder+'/request-'+(r.model_requests+1)+'.json',body);
     const counted=await api('responses/input_tokens',body);r.token_count_requests=(r.token_count_requests||0)+1;
     await write(folder+'/count-'+(r.model_requests+1)+'.json',counted);
     const reserve=reserveCost(counted.input_tokens,c);canSpend(ledger,reserve,a,c);
     ledger.unknown_usd+=reserve;ledger.requests++;r.model_requests++;await save();
     const started=new Date().toISOString();
     const response=await api('responses',{...body,store:false,include:['reasoning.encrypted_content'],service_tier:'default',max_output_tokens:c.max_output_tokens});
     await write(folder+'/response-'+r.model_requests+'.json',response);
     const calls=response.output.filter(x=>x.type==='computer_call');
     const u=usageCost(response.usage,c,calls.length);ledger.spent_usd+=u.token_usd+u.tool_usd;ledger.unknown_usd-=reserve;
     r.input_tokens+=u.input_tokens;r.output_tokens+=u.output_tokens;r.estimated_cost_usd+=u.token_usd+u.tool_usd;
     ledger.events.push({test:test.id,response_id:response.id,started,...u});await save();
     if(ledger.spent_usd+c.billing_cushion_usd>a.budget_usd||u.token_usd+u.tool_usd>reserve){ledger.metering_stop=true;await save();throw new Stop('Unexpected metering exceeded reserved amount; stop all paid work','BLOCKED');}
     if(response.status!=='completed')throw new Stop('Incomplete response; no paid retry');
     if(calls.length>1)throw new Stop('Unexpected parallel native calls; stop for protocol review');
     if(!calls.length){r.status='ERROR';r.reason='PENDING_INDEPENDENT_REVIEW: agent stopped; no automatic PASS.';break;}
     const call=calls[0];if(call.pending_safety_checks?.length)throw new Stop('Native safety check requires review','BLOCKED');
     if(!Array.isArray(call.actions)||!call.actions.length)throw new Stop('Missing native actions; no fallback to scripted solver');
     for(const action of call.actions){
      if(r.actions>=limits.actions||Date.now()-start>limits.seconds*1000)throw new Stop('Action/runtime cap');
      await executeAction(driver,action,viewport);r.actions++;
      shot=await capture(driver,folder+'/screenshots');
      const event={response_id:response.id,call_id:call.call_id,action,screenshot:shot.file,at:new Date().toISOString()};
      transcript.push(event);await write(folder+'/actions.json',transcript);r.evidence.push(shot.file);
     }
     // Full text action/observation history retained, but old image payloads are not rebilled.
     const messages=response.output.filter(x=>x.type==='message');for(const m of messages)transcript.push({observation:m});
     last={call,output:response.output,image:shot.image};await save();
    }
   }catch(e){r.status=r.model_requests&&e.status==='NOT_RUN'?'ERROR':e.status||'ERROR';r.reason=e.message;if(ledger.unknown_usd>0||ledger.metering_stop||e.status==='NOT_RUN')throw e;}
   finally{r.execution_seconds=(Date.now()-start)/1000;if(driver){await capture(driver,folder+'/screenshots');await driver.cleanup()}await save()}
  }
 }finally{await save();await unlink(priv+'/paid.lock')}
 console.log('Stopped. Raw evidence remains private pending redaction and independent review.');
}
main().catch(e=>{console.error(e.message);process.exitCode=1});
