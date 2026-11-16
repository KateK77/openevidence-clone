// FREE readiness checks. This file never imports or calls an OpenAI client.
import assert from 'node:assert/strict'
import {readFile,writeFile,mkdir} from 'node:fs/promises'
import {resolve,join} from 'node:path'
import {pathToFileURL} from 'node:url'
import {execFileSync} from 'node:child_process'
import {createHash} from 'node:crypto'
import {prepare,cleanup,assertPinned,prerequisite} from './environment.mjs'
const config=JSON.parse(await readFile('evaluation/config.json','utf8'))
const tasks=JSON.parse(await readFile(config.suite,'utf8'))
const checks=[]
const check=(name,detail)=>checks.push({name,status:'PASS',detail})
const output=resolve('evaluation/preflight'); await mkdir(output,{recursive:true})
let prepared,browser
try {
  const frozen=JSON.parse(await readFile('evaluation/catalog-v1/freeze.json','utf8'))
  const digest=createHash('sha256').update(await readFile(config.suite)).digest('hex')
  assert.equal(digest,frozen.tasks_sha256); assert.equal(digest,config.frozen_suite_sha256)
  assert.deepEqual(Object.fromEntries([1,2,3,4,5].map(d=>[d,tasks.filter(t=>t.difficulty===d).length])),{'1':10,'2':20,'3':30,'4':25,'5':15})
  assert.equal(new Set(tasks.map(t=>t.id)).size,100)
  for(const t of tasks) { assert(t.assertions.length>=2); for(const k of ['user_role','initial_state','user_goal','expected_outcome','feature_category']) assert(t[k]); assert.equal(t.paid_retries,0) }
  check('Frozen catalog integrity', {tasks:100,distribution:frozen.difficulty_distribution,sha256:digest})
  check('Application source freeze',assertPinned(config))
  assert.equal(config.execution_authorized,false); assert.equal(config.total_usd,5)
  check('Paid execution disabled','No approval or API key is loaded by this preflight')
  prepared=await prepare({test:tasks[2],config})
  assert(prepared.ready)
  const health=await (await fetch(config.base_url+'/api/health/')).json()
  assert.equal(health.status,'ok');assert.equal(health.version,'3.0.0');assert.equal(health.generation_configured,false)
  check('Fresh database migration and pinned WSGI health',health)
  const cookie='medevidence_session_v2='+prepared.manifest.sessions.a
  const authed=await (await fetch(config.base_url+'/api/session/',{headers:{Cookie:cookie}})).json()
  assert.equal(authed.user.username,'eva_a');check('Disclosed fixture authentication','Server-side session setup works; login UI not benchmarked')
  const b=prepared.manifest.threads.find(t=>t.owner==='eva_b')
  const denied=await fetch(config.base_url+'/api/conversations/'+b.conversation+'/',{headers:{Cookie:cookie}})
  assert([403,404].includes(denied.status)); check('Independent owner-scoped oracle probe',{http_status:denied.status,kind:'offline API probe, not native task result'})
  const csrf=await fetch(config.base_url+'/api/profile/',{method:'PATCH',headers:{Cookie:cookie,'Content-Type':'application/json'},body:JSON.stringify({first_name:'preflight'})})
  assert.equal(csrf.status,403);check('CSRF enforced for fixture session','Unsigned mutation rejected; no task credited')
  const snapshot=JSON.parse(execFileSync(resolve(config.python),['evaluation/harness/snapshot.py',join(prepared.folder,'test.sqlite3')],{encoding:'utf8'}))
  assert.equal(snapshot.evidence_conversation.length,4);assert.equal(snapshot.evidence_publication.length,2)
  check('Synthetic fixture and read-only oracle','4 synthetic threads, 2 labelled synthetic sources; oracle excludes users/sessions/password hashes')
  const {chromium}=await import(pathToFileURL(resolve(config.playwright_module)).href)
  browser=await chromium.launch({executablePath:config.browser_executable,headless:true})
  let blocked=0
  const context=await browser.newContext({viewport:config.viewport,storageState:prepared.storage_state,serviceWorkers:'block'})
  await context.route('**/*',r=>new URL(r.request().url()).origin===config.base_url?r.continue():(blocked++,r.abort()))
  const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message))
  await page.goto(config.base_url,{waitUntil:'networkidle'});await page.screenshot({path:join(output,'desktop-home.png')})
  assert((await page.locator('body').innerText()).includes('MedEvidence'));assert.equal(errors.length,0)
  check('Desktop browser readiness',{viewport:config.viewport,page_errors:errors,screenshot:'desktop-home.png'})
  await page.setViewportSize({width:390,height:844});await page.screenshot({path:join(output,'mobile-home.png')})
  check('Mobile screenshot capture',{viewport:{width:390,height:844},screenshot:'mobile-home.png',note:'Capture/readability check, not full mobile workflow verdict'})
  await page.goto('https://example.invalid/').catch(()=>{})
  assert(blocked>0);check('Browser egress guard','Non-loopback request aborted')
  await context.close();await cleanup({prepared});const first=prepared.folder;prepared=null
  prepared=await prepare({test:tasks[9],config});assert.notEqual(prepared.folder,first)
  const empty=JSON.parse(execFileSync(resolve(config.python),['evaluation/harness/snapshot.py',join(prepared.folder,'test.sqlite3')],{encoding:'utf8'}))
  assert.equal(empty.evidence_conversation.length,0)
  check('Task isolation and empty fixture','Second DB has no conversations; first DB is not reset or reused')
} catch(e) {checks.push({name:'Readiness interruption',status:'FAIL',detail:e.message});process.exitCode=1}
finally {if(browser)await browser.close();if(prepared)await cleanup({prepared})}
const readiness=tasks.map(t=>({id:t.id,difficulty:t.difficulty,fixture_requirements:t.fixture_requirements,...prerequisite(t)}))
await writeFile(join(output,'readiness.json'),JSON.stringify({checked_at:new Date().toISOString(),kind:'OFFLINE_ONLY',paid_calls:0,native_tasks_attempted:0,checks,fixture_readiness:readiness},null,2)+'\n')
console.log(JSON.stringify({checks:checks.length,passed:checks.filter(c=>c.status==='PASS').length,failed:checks.filter(c=>c.status==='FAIL').length,fixture_supported:readiness.filter(x=>x.ready).length,paid_calls:0,native_tasks_attempted:0},null,2))
