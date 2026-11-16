import test from 'node:test';import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {hash,assertPaidExecutionReady,validateApproval,reserveCost,canSpend,usageCost,orderTests,payload,executeAction} from './core.mjs';
const raw=await readFile(new URL('../config.json',import.meta.url));const c=JSON.parse(raw);
const approval={approved:true,user_statement:'TEST FIXTURE ONLY, NOT AUTHORIZATION',approved_at:'fixture',suite_sha256:'fixture',config_sha256:hash(raw),model:c.model,budget_usd:5,tool_pricing_confirmed:true,computer_call_usd:0};
test('approval absent fails closed',()=>assert.throws(()=>validateApproval({},c,'fixture',hash(raw))));
test('wrong frozen suite/config rejected',()=>{assert.throws(()=>validateApproval(approval,c,'changed',hash(raw)));assert.throws(()=>validateApproval(approval,c,'fixture','changed'))});
test('ceiling cannot exceed ten dollars',()=>assert.throws(()=>validateApproval({...approval,budget_usd:10.01},c,'fixture',hash(raw))));
test('unknown tool fees block paid execution',()=>assert.throws(()=>validateApproval({...approval,tool_pricing_confirmed:false},c,'fixture',hash(raw))));
test('unknown prior charge stops every further call',()=>assert.throws(()=>canSpend({spent_usd:0,unknown_usd:.01},.01,approval,c)));
test('reserve prevents crossing remaining budget',()=>assert.throws(()=>canSpend({spent_usd:4.88,unknown_usd:0},.03,approval,c)));
test('full output and fee reserve included',()=>{const d={...c,pricing:{...c.pricing,computer_call_usd:.01}};assert.equal(reserveCost(1000,d),.00275+.018+.08)});
test('cache and reasoning accounted without double counting',()=>{const u=usageCost({input_tokens:1000,output_tokens:200,input_tokens_details:{cached_tokens:400},output_tokens_details:{reasoning_tokens:100}},c,1);assert.equal(u.reasoning_tokens,100);assert.ok(Math.abs(u.token_usd-.0046)<1e-10)});
test('missing usage rejected rather than treated as free',()=>assert.throws(()=>usageCost(null,c,0)));
test('text transcript retained, only latest image sent',()=>{const t={task:'all original steps'},f={synthetic:true},history=[{action:'observed earlier'}];const p=payload(t,f,history,{image:'data:image/png;base64,NEW'},c);assert.equal(JSON.stringify(p).match(/base64/g).length,1);assert.ok(JSON.stringify(p).includes('observed earlier'));assert.deepEqual(p.tools,[{type:'computer'}]);assert.equal(p.parallel_tool_calls,false)});
test('native executor never turns unsupported action into JS',async()=>assert.rejects(()=>executeAction({page:{}},{type:'exec',code:'alert(1)'},{width:1280,height:768})));
test('off-screen coordinates refused',async()=>assert.rejects(()=>executeAction({page:{mouse:{click(){throw Error('should not execute')}}}},{type:'click',x:5000,y:2},{width:1280,height:768})));
test('budget order includes every difficulty in every ten tasks',()=>{const rows=['Easy','Medium','Hard','Expert'].flatMap((d,i)=>Array.from({length:[30,40,20,10][i]},(_,n)=>({id:d+n,difficulty:d})));const ordered=orderTests(rows);assert.equal(new Set(ordered.map(t=>t.id)).size,100);for(let i=0;i<100;i+=10)assert.deepEqual(ordered.slice(i,i+10).map(t=>t.difficulty),['Easy','Easy','Easy','Medium','Medium','Medium','Medium','Hard','Hard','Expert'])});

test('new approval and config flags cannot bypass actual invoice block',()=>{
 assert.doesNotThrow(()=>validateApproval({...approval,budget_usd:10},c,'fixture',hash(raw)));
 assert.throws(()=>assertPaidExecutionReady({...c,billing_enforcement:{actual_bill_cap_verified:true,paid_execution_enabled:true}},approval),/ACTUAL_BILL_CAP_UNVERIFIED/);
});
test('actual ten dollar local reservation boundary',()=>{
 const a={...approval,budget_usd:10};
 assert.doesNotThrow(()=>canSpend({spent_usd:9.87,unknown_usd:0},.03,a,c));
 assert.throws(()=>canSpend({spent_usd:9.870001,unknown_usd:0},.03,a,c));
});
test('invalid financial state and unknown fees fail closed',()=>{
 for(const spent_usd of [NaN,Infinity,-1])assert.throws(()=>canSpend({spent_usd,unknown_usd:0},.03,approval,c));
 assert.throws(()=>reserveCost(1000,{...c,pricing:{...c.pricing,computer_call_usd:null}}));
 assert.throws(()=>usageCost({input_tokens:100,output_tokens:10,input_tokens_details:{cached_tokens:1.5}},c,1));
});
test('prior metering discrepancy cannot be resumed',()=>assert.throws(()=>canSpend({spent_usd:0,unknown_usd:0,metering_stop:true},.01,approval,c)));
test('archive metadata excluded but action and observation preserved in context',()=>{
 const p=payload({task:'unchanged'},{},[{action:{type:'click',x:1,y:2},observation:'same',screenshot:'PRIVATE_FILE_PATH',at:'timestamp',response_id:'old-response'}],{image:'data:image/png;base64,NEW'},c);
 assert.ok(!JSON.stringify(p).includes('PRIVATE_FILE_PATH'));assert.ok(JSON.stringify(p).includes('same'));assert.ok(JSON.stringify(p).includes('click'));
});
