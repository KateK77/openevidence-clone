import { readFile, writeFile, mkdir, open } from 'node:fs/promises'
import { dirname } from 'node:path'

// One non-resettable ledger per PROJECT, outside run directories. Unknown charges
// retain their full reservation and prevent continuation until invoice review.
export class BudgetLedger {
  constructor(path, ceiling=5) { if (!(ceiling>0 && ceiling<=5)) throw Error('Project cap must be <= $5'); this.path=path; this.ceiling=ceiling }
  async acquire() {
    await mkdir(dirname(this.path),{recursive:true})
    this.lock=await open(this.path+'.lock','wx')
    try { this.state=JSON.parse(await readFile(this.path,'utf8')) }
    catch(e) { if(e.code!=='ENOENT') throw e; this.state={project:'KateK77/openevidence-clone',entries:[]} }
    if(this.state.project!=='KateK77/openevidence-clone'||!Array.isArray(this.state.entries)) throw Error('Wrong or invalid project ledger')
    if(this.state.entries.some(e=>e.status!=='settled')) throw Error('Unreconciled request reservation: billing review required')
    return this
  }
  total() { return this.state.entries.reduce((s,e)=>s+e.charged_upper_usd,0) }
  async save() { await writeFile(this.path,JSON.stringify(this.state,null,2)+'\n') }
  async reserve(id,usd) {
    if(!Number.isFinite(usd)||usd<0||this.total()+usd>this.ceiling-0.01) throw Error('Project dollar budget reserve would exceed cap (including $0.01 cushion)')
    if(this.state.entries.some(e=>e.id===id)) throw Error('Duplicate request; paid retries disabled')
    this.state.entries.push({id,status:'pending',charged_upper_usd:usd,reserved_usd:usd,time:new Date().toISOString()}); await this.save()
  }
  async settle(id,usd,metadata) {
    const item=this.state.entries.find(e=>e.id===id)
    if(!item||item.status!=='pending'||!Number.isFinite(usd)||usd<0) throw Error('Invalid charge reconciliation')
    if(usd>item.reserved_usd) throw Error('Provider exceeded reserved cost; billing review required')
    Object.assign(item,{status:'settled',charged_upper_usd:usd,...metadata}); await this.save()
  }
  async release() { if(this.lock) { await this.lock.close(); this.lock=null; const {unlink}=await import('node:fs/promises'); await unlink(this.path+'.lock') } }
}
