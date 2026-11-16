import {readFileSync} from 'node:fs'
import { spawn, execFileSync } from 'node:child_process'
import { readFile, mkdir, writeFile, readdir } from 'node:fs/promises'
import { resolve, join } from 'node:path'
import { randomUUID, createHash } from 'node:crypto'

export const supported = [...Array.from({length:18},(_,i)=>i+1),29,30,33,34,35,36,37,38,39,40,41,42,49,50,53,60,61,62,66].map(n=>'ME-'+String(n).padStart(3,'0'))
export function prerequisite(test) {
  if(!supported.includes(test.id)) return {ready:false,reason:'Prepaid prerequisite gate: '+test.fixture_requirements.join(',')+' needs a reviewed live PubMed, no-paid application model, controlled fault or legacy adapter. No substitute success fixture is allowed.'}
  return {ready:true}
}
export function assertPinned(config) {
  const frozen=JSON.parse(readFileSync('evaluation/catalog-v1/freeze.json','utf8'))
  const changed=execFileSync('git',['diff',frozen.application_commit,'--','backend','frontend',':(exclude)frontend/dist'],{encoding:'utf8',maxBuffer:1024*1024})
  if(changed.trim()) throw Error('Application differs from frozen commit')
  const untracked=execFileSync('git',['ls-files','--others','--exclude-standard','backend','frontend'],{encoding:'utf8'})
  if(untracked.trim()) throw Error('Untracked application source invalidates freeze')
  const build=JSON.parse(readFileSync('evaluation/preflight/build.json','utf8'));if(build.application_commit!==frozen.application_commit)throw Error('Wrong application build receipt');for(const asset of build.files){if(createHash('sha256').update(readFileSync(asset.path)).digest('hex')!==asset.sha256)throw Error('Built asset differs from frozen receipt')}
  return frozen.application_commit
}
export async function prepare({test,config}) {
  const gate=prerequisite(test); if(!gate.ready) return gate
  assertPinned(config)
  const folder=resolve('evaluation/.runtime',test.id+'-'+randomUUID()); await mkdir(folder,{recursive:true})
  const port=new URL(config.base_url).port
  const env={...process.env}; for(const key of Object.keys(env)) if(/api.?key|token|secret|database_url|redis_url|proxy/i.test(key)) delete env[key]
  const child=spawn(resolve(config.python),[resolve('evaluation/harness/local-server.py'),folder,port,test.id],{env,windowsHide:true,stdio:['ignore','pipe','pipe']})
  let startup=''; child.stdout.on('data',d=>startup+=d); child.stderr.on('data',d=>startup+=d)
  let spawnError; child.on('error',e=>spawnError=e)
  try {
    let manifest
    for(let n=0;n<100;n++) {
      if(spawnError) throw spawnError
      if(child.exitCode!==null) throw Error('Local server exited: '+startup.slice(-1200))
      try {manifest=JSON.parse(await readFile(join(folder,'manifest.private.json'),'utf8')); const r=await fetch(config.base_url+'/api/health/'); if(r.ok&&r.headers.get('x-benchmark-instance')===folder.split(/[\\/]/).pop()) break; manifest=null} catch {manifest=null}
      await new Promise(r=>setTimeout(r,200))
    }
    if(!manifest) throw Error('Offline local server did not become healthy')
    const anonymous=test.user_role.startsWith('Anonymous'), cookie={name:'medevidence_session_v2',value:manifest.sessions.a,domain:'127.0.0.1',path:'/',httpOnly:true,secure:false,sameSite:'Lax'}
    return {ready:true,folder,child,manifest,configPython:config.python,viewport:test.fixture_requirements.includes('M')?{width:390,height:844}:config.viewport,
      storage_state:{cookies:anonymous?[]:[cookie],origins:[]},
      secrets:Object.values(manifest.accounts).map(a=>a.password).concat(Object.values(manifest.sessions)),
      instructions:'SCRIPTED SETUP ONLY: fresh synthetic DB, '+(anonymous?'anonymous browser':'session prepared for eva_a')+'. All tasks start at home. Two accounts: '+JSON.stringify(manifest.accounts)+'. Register a different unique username when registration is under test. Existing fixture identifiers: '+JSON.stringify(manifest.threads)+'. Synthetic source/answer fixtures are labelled and are not live retrieval or model generation. Browser chrome is outside screenshots; Ctrl+L/type URL/Enter and Ctrl+T/W are explicitly emulated shortcuts, with only model-chosen allowed URLs. Do all required task actions yourself.'}
  } catch(e) { child.kill(); throw e }
}
export async function verify({test,prepared,config}) {
  // Preserve a separate read-only database snapshot for a human assertion reviewer.
  // Never provide this oracle state to the screenshot-only actor.
  const args=[resolve('evaluation/harness/snapshot.py'),join(prepared.folder,'test.sqlite3')]
  const snapshot=execFileSync(resolve(prepared.configPython||'../venv/Scripts/python.exe'),args,{encoding:'utf8',windowsHide:true})
  await writeFile(join(prepared.folder,'oracle-snapshot.json'),snapshot)
  await writeFile(resolve(config.output_dir,'logs',test.id+'-oracle.json'),snapshot)
  return null // Human review checks EVERY assertion; no model self-grading.
}
export async function cleanup({prepared}) { if(prepared.child) { const exited=new Promise(r=>prepared.child.once('exit',r)); prepared.child.kill(); await Promise.race([exited,new Promise(r=>setTimeout(r,3000))]) } }
