/** No OpenAI/Gemini requests; local infrastructure checks only, never 100-test scores. */
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
import {resolve,relative} from 'node:path';
import {root,evaldir,prepare,python,dist,appOriginal} from './environment.mjs';
import {read,hash,write,capture} from './core.mjs';
const report={kind:'OFFLINE INFRASTRUCTURE ONLY',checked_at:new Date().toISOString(),paid_api_calls:0,external_api_calls:0,scored_tests:0,checks:[]};
const ok=name=>{report.checks.push({name,status:'PASS'});console.log('PASS '+name)};
let driver;
try{
 const f=await read(evaldir+'/freeze.json'),suite=await read(evaldir+'/final_test_cases_100.json');
 for(const [p,h]of Object.entries(f.files))if(hash(await readFile(evaldir+'/'+p))!==h)throw Error('Frozen hash mismatch '+p);
 if(suite.tests.length!==100||new Set(suite.tests.map(t=>t.id)).size!==100)throw Error('Suite count/IDs');
 const counts={};for(const t of suite.tests)counts[t.difficulty]=(counts[t.difficulty]||0)+1;
 if(JSON.stringify(counts)!==JSON.stringify({Easy:30,Medium:40,Hard:20,Expert:10}))throw Error('Difficulty distribution');
 ok('Frozen Description, suite hashes, unique IDs and 30/40/20/10 distribution');
 execFileSync('git',['diff','--exit-code',f.application_commit,'--','backend','frontend','experiments/round-03/consolidated-prompt.md'],{cwd:root,stdio:'pipe'});
 execFileSync('git',['diff','--exit-code',f.application_commit,'--','frontend'],{cwd:appOriginal,stdio:'pipe'});
 report.frontend_build={source:'Existing locally built frontend matching unchanged source baseline',index_sha256:hash(await readFile(dist+'/index.html'))};
 ok('Application and final Description source unchanged; frontend source matches build origin');
 const unit=execFileSync('node',['--test','evaluation/harness/test_core.mjs'],{cwd:root,encoding:'utf8'});
 await writeFile(evaldir+'/logs/harness-unit-tests.tap',unit);ok('Budget, approval, protocol and coordinate guard unit checks');
 const denied=execFileSync('node',['evaluation/harness/native-cua.mjs'],{cwd:root,encoding:'utf8'});
 if(!denied.includes('CHECK ONLY'))throw Error('Paid entry point unexpectedly active');ok('Paid runner defaults to no execution');
 const folder=evaldir+'/.private/preflight-'+Date.now();driver=await prepare(folder);
 const errors=[];driver.page.on('pageerror',e=>errors.push(e.message));
 await driver.page.getByRole('heading',{name:/Better questions/}).waitFor();ok('Isolated Django + compiled React browser loads');
 const session=await (await driver.page.request.get(driver.origin+'/api/session/')).json();
 if(session.generation_configured)throw Error('Model credentials were not disabled');ok('Application AI disabled and offline backend network guard active');
 await driver.page.goto(driver.origin+'/profile');
 await driver.page.getByLabel('Username',{exact:true}).fill(driver.manifest.accounts.a.username);
 await driver.page.getByLabel('Password',{exact:true}).fill(driver.manifest.accounts.a.password);
 await driver.page.getByRole('button',{name:'Sign in',exact:true}).click();
 await driver.page.locator('.account').getByText('evaluation_a').waitFor();await driver.page.reload();
 await driver.page.locator('.account').getByText('evaluation_a').waitFor();ok('Synthetic credentials, session and database round-trip');
 await driver.page.goto(driver.origin+'/history');await driver.page.getByText('SYNTHETIC Acceptance fixture evaluation_a 0',{exact:true}).waitFor();
 const shot=await capture(driver,evaldir+'/screenshots');report.screenshot=relative(evaldir,shot.file).replaceAll('\\','/');ok('Screenshot capture at 1280x768 with device scale 1');
 await driver.page.setViewportSize({width:390,height:844});await driver.page.goto(driver.origin);await driver.page.locator('.mode-banner').waitFor();
 const mobile=await capture(driver,evaldir+'/screenshots');report.mobile_screenshot=relative(evaldir,mobile.file).replaceAll('\\','/');ok('Mobile screenshot at 390x844');
 const db=execFileSync(python,['-c',"import sqlite3,json,sys; c=sqlite3.connect('file:'+sys.argv[1]+'?mode=ro',uri=True); print(json.dumps({'integrity':c.execute('pragma integrity_check').fetchone()[0],'users':c.execute('select count(*) from auth_user').fetchone()[0],'conversations':c.execute('select count(*) from evidence_conversation').fetchone()[0]}))",folder+'/test.sqlite3'],{encoding:'utf8'});
 report.database=JSON.parse(db);if(report.database.integrity!=='ok'||report.database.users!==2)throw Error('Isolated DB integrity');ok('Fresh isolated SQLite integrity and synthetic fixture counts');
 if(errors.length)throw Error('Uncaught browser exceptions');if(driver.blocked.length)throw Error('Browser attempted external resource');ok('No uncaught browser exceptions or external browser resources');
 report.result='PASS';report.prerequisites='Live PubMed/model/fault injection and hosted restart profiles remain separately unverified. No native paid task was executed.';
}catch(e){report.result='ERROR';report.error=e.message;process.exitCode=1}
finally{if(driver)await driver.cleanup();await mkdir(evaldir+'/logs',{recursive:true});await write(evaldir+'/logs/offline-preflight.json',report);console.log(JSON.stringify(report,null,2))}
