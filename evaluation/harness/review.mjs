// Local, no-model assertion review. Input is a separately authored human review.
import {readFile,writeFile} from 'node:fs/promises'
import {resolve,join,relative} from 'node:path'
import {createHash} from 'node:crypto'
const hash=b=>createHash('sha256').update(b).digest('hex')
export async function validateReview(task,result,review,run) {
  if(!['PASS','FAIL','BLOCKED'].includes(review.status)||!review.reviewed_by||!review.reason) throw Error('Review must state status, reviewer and reason')
  if(!Array.isArray(review.assertions)||review.assertions.length!==task.assertions.length) throw Error('Review every frozen assertion')
  const ids=new Set(review.assertions.map(a=>a.id))
  if(ids.size!==task.assertions.length||task.assertions.some(a=>!ids.has(a.id))) throw Error('Frozen assertion ID mismatch')
  for(const a of review.assertions) {
    if(!['PASS','FAIL','UNVERIFIED'].includes(a.verdict)) throw Error('Invalid assertion verdict')
    if(a.verdict==='UNVERIFIED') continue
    if(!a.evidence?.length) throw Error('Independent assertion evidence required')
    for(const e of a.evidence) {
      const path=resolve(run,e.path),rel=relative(run,path)
      if(rel.startsWith('..')||!rel) throw Error('Evidence must belong to this run')
      if(hash(await readFile(path))!==e.sha256) throw Error('Evidence hash mismatch')
    }
  }
  if(review.status==='PASS'&&review.assertions.some(a=>a.verdict!=='PASS')) throw Error('PASS requires every assertion')
  if(['PASS','FAIL'].includes(review.status)) {
    if(!result.usage?.model_requests) throw Error('No paid native attempt; cannot report native PASS/FAIL')
    const lines=(await readFile(join(run,'logs',task.id+'.jsonl'),'utf8')).trim().split('\n').map(JSON.parse)
    const responses=lines.filter(e=>e.kind==='model_response')
    if(!responses.some(e=>e.response_id&&e.native_calls?.some(c=>c.call_id))) throw Error('Native API call evidence missing')
    if(review.status==='FAIL'&&!review.assertions.some(a=>a.verdict==='FAIL')) throw Error('FAIL requires an objective failed assertion')
  }
  return {...result,status:review.status,reason:review.reason,independent_review:review,execution_state:'independently_reviewed'}
}
if(process.argv[1]?.endsWith('review.mjs')&&process.argv.includes('--run')) {
  const arg=n=>process.argv[process.argv.indexOf(n)+1],run=resolve(arg('--run'))
  const tasks=JSON.parse(await readFile('evaluation/catalog-v1/tasks.json','utf8'))
  const results=JSON.parse(await readFile(join(run,'native_results.json'),'utf8'))
  const reviews=JSON.parse(await readFile(resolve(arg('--reviews')),'utf8'))
  for(const review of reviews) {const i=results.findIndex(r=>r.id===review.id);if(i<0)throw Error('Unknown task');results[i]=await validateReview(tasks.find(t=>t.id===review.id),results[i],review,run)}
  await writeFile(join(run,'reviewed_results.json'),JSON.stringify(results,null,2)+'\n',{flag:'wx'})
}
