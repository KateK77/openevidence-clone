import {spawn} from 'node:child_process';
import {existsSync} from 'node:fs';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {Stop,read} from './core.mjs';
export const root=resolve(dirname(fileURLToPath(import.meta.url)),'../..');
export const evaldir=resolve(root,'evaluation');
export const appOriginal=resolve(root,'../../outputs/MedEvidence-AI');
export const python=process.env.EVAL_PYTHON||resolve(root,'../venv/Scripts/python.exe');
export const dist=process.env.EVAL_FRONTEND_DIST||resolve(appOriginal,'frontend/dist');
export const playwrightPath=process.env.EVAL_PLAYWRIGHT_MODULE||resolve(appOriginal,'frontend/node_modules/@playwright/test/index.mjs');
export async function prepare(folder,profile='offline',viewport={width:1280,height:768},testId=''){
 if(!['offline','pubmed'].includes(profile))throw new Stop('Prerequisite adapter not provisioned: '+profile,'BLOCKED');
 for(const p of [python,dist+'/index.html',playwrightPath])if(!existsSync(p))throw new Stop('Local dependency missing: '+p,'BLOCKED');
 const port=18483,origin='http://127.0.0.1:'+port;
 // Never attach to or kill another process already on our port.
 const net=await import('node:net');
 await new Promise((ok,bad)=>{const s=net.createServer();s.once('error',()=>bad(new Stop('Evaluation port occupied','BLOCKED')));s.listen(port,'127.0.0.1',()=>s.close(ok))});
 await mkdir(folder,{recursive:true});
 const env={...process.env,EVAL_FRONTEND_DIST:dist};
 delete env.OPENAI_API_KEY;delete env.LLM_API_KEY;delete env.GEMINI_API_KEY;
 const server=spawn(python,[resolve(evaldir,'harness/local_server.py'),folder,String(port),profile,testId],{cwd:root,env,windowsHide:true,stdio:['ignore','pipe','pipe']});
 let log='';server.stdout.on('data',x=>log+=x);server.stderr.on('data',x=>log+=x);
 let browser,context;
 const cleanup=async()=>{await browser?.close();server.kill();await writeFile(folder+'/server.log',log)};
 try{
  let ready=false;for(let n=0;n<80;n++){if(server.exitCode!==null)break;try{const r=await fetch(origin+'/api/health/',{signal:AbortSignal.timeout(1000)});if(r.ok){ready=true;break}}catch{}await new Promise(r=>setTimeout(r,250))}
  if(!ready)throw new Stop('Local server failed to start','BLOCKED');
  const {chromium}=await import(pathToFileURL(playwrightPath).href);browser=await chromium.launch({headless:true});
  context=await browser.newContext({viewport,deviceScaleFactor:1,acceptDownloads:true,permissions:['clipboard-read','clipboard-write']});
  const allowURL=value=>{try{const u=new URL(value);return u.origin===origin||(profile!=='offline'&&u.protocol==='https:'&&['pubmed.ncbi.nlm.nih.gov','doi.org'].includes(u.hostname))}catch{return false}};
  const blocked=[];await context.route('**/*',r=>allowURL(r.request().url())?r.continue():(blocked.push(r.request().url()),r.abort()));
  const driver={browser,context,page:await context.newPage(),allowURL,blocked,origin,cleanup,manifest:await read(folder+'/manifest.json')};
  context.on('page',p=>{driver.page=p;attachDownloads(p)});
  function attachDownloads(p){p.on('download',async d=>{await mkdir(folder+'/downloads',{recursive:true});await d.saveAs(folder+'/downloads/'+d.suggestedFilename().replace(/[^a-z0-9._-]/gi,'_'))})}
  attachDownloads(driver.page);await driver.page.goto(origin);return driver;
 }catch(e){await cleanup();throw e}
}
