import {useState} from 'react'
import {useMutation,useQuery,useQueryClient} from '@tanstack/react-query'
import {Link,useNavigate,useParams} from 'react-router-dom'
import {api,date,type Answer,type Thread,type Article} from './api'
import {Composer,Page,Problem,fields,useAsk} from './app'

export function Conversation(){
  const {id}=useParams()
  const client=useQueryClient()
  const navigate=useNavigate()
  const thread=useQuery({queryKey:['thread',id],queryFn:()=>api<Thread>('conversations/'+id+'/')})
  const ask=useAsk()
  const [question,change]=useState('')
  const [mode,setMode]=useState('')
  const command=useMutation({mutationFn:({method,body}:{method:string;body?:unknown})=>api<Thread|undefined>('conversations/'+id+'/',method,body),onSuccess:data=>{
    void client.invalidateQueries({queryKey:['history']})
    if(data){client.setQueryData(['thread',id],data);setMode('')}
    else{
      client.removeQueries({queryKey:['answer']})
      client.removeQueries({queryKey:['saved-answers']})
      void client.invalidateQueries({queryKey:['thread',id],refetchType:'none'})
      navigate('/history')
    }
  }})
  return <Page title={thread.data?.title||'Conversation'}>
    <Link to="/history">← Research history</Link>
    <Problem error={thread.error||ask.error||command.error}/>
    {thread.isPending&&<p role="status">Loading conversation…</p>}
    {thread.data&&<>
      <div className="toolbar"><button onClick={()=>setMode(mode==='rename'?'':'rename')}>Rename</button><button onClick={()=>setMode(mode==='delete'?'':'delete')}>Delete</button></div>
      {mode==='rename'&&<form className="toolbar" onSubmit={e=>command.mutate({method:'PATCH',body:fields(e)})}><input name="title" aria-label="Conversation title" defaultValue={thread.data.title} required maxLength={180}/><button disabled={command.isPending}>Save title</button></form>}
      {mode==='delete'&&<p className="notice">Delete this conversation? <button disabled={command.isPending} onClick={()=>command.mutate({method:'DELETE'})}>Confirm delete</button></p>}
      {thread.data.turns?.map(answer=><article className="panel" key={answer.id}><small>{date(answer.created)}</small><h2>{answer.question}</h2><Synthesis answer={answer}/><Link to={'/answer/'+answer.id}>View answer and evidence →</Link></article>)}
      <Composer question={question} change={change} busy={ask.isPending} follow submit={()=>ask.mutate({question,conversation:Number(id)},{onSuccess:()=>change('')})}/>
    </>}
  </Page>
}
const statuses:Record<string,string>={complete:'Synthesis complete',retrieval_only:'Retrieval only',retrieval_error:'Retrieval unavailable',generation_error:'Generation unavailable',insufficient:'Insufficient evidence',demo:'Synthetic demo'}
function Synthesis({answer,quotes}:{answer:Answer;quotes?:boolean}){
  return <div className="synthesis"><span className="pill">{statuses[answer.status]||answer.status}</span> {answer.model&&<small>{answer.model}</small>}
    {answer.result.message&&<p>{answer.result.message}</p>}
    {answer.result.sections?.map((section,i)=><div className="finding" key={i}>
      <strong>{section.status==='supported'?'Supported finding':section.status==='tentative'?'Tentative or conflicting':'Evidence gap'}</strong>
      <p>{section.text}</p>{section.citations.map((citation,j)=><div className="citation" key={j}>
        <a href={'https://pubmed.ncbi.nlm.nih.gov/'+citation.pmid+'/'} target="_blank" rel="noreferrer">PMID {citation.pmid} ↗</a>
        {quotes&&<details><summary>Verified abstract excerpt</summary><blockquote>{citation.quote}</blockquote></details>}
      </div>)}
    </div>)}
    {!!answer.sources.length&&<p className="muted">{answer.sources.length} PubMed records · Abstracts and metadata</p>}
  </div>
}
export function Metadata({article}:{article:Article}){
  return <div className="metadata"><p>{article.authors.join(', ')||'Authors unavailable'}</p><p>{article.journal||'Journal unavailable'} · {article.date||'Publication date unavailable'}</p><p>{article.doi?'DOI '+article.doi:'DOI unavailable'}</p><p className="abstract">{article.abstract||'Abstract unavailable.'}</p></div>
}
export function AnswerPage(){
  const {id}=useParams()
  const client=useQueryClient()
  const query=useQuery({queryKey:['answer',id],queryFn:()=>api<Answer>('answers/'+id+'/')})
  const [note,setNote]=useState('')
  const save=useMutation({mutationFn:(saved:boolean)=>api<{saved:boolean}>('answers/'+id+'/save/',saved?'DELETE':'PUT'),onSuccess:result=>{
    client.setQueryData<Answer>(['answer',id],old=>old&&({...old,saved:result.saved}))
    void client.invalidateQueries({queryKey:['saved-answers']})
  }})
  const answer=query.data
  if(!answer) return <Page title="Answer details"><Problem error={query.error}/>{query.isPending&&<p role="status">Loading answer…</p>}</Page>
  async function copy(){
    try{
      const result=await fetch('/api/answers/'+id+'/export/md/')
      if(!result.ok) throw new Error()
      await navigator.clipboard.writeText(await result.text())
      setNote('Answer copied.')
    }catch{setNote('Clipboard unavailable. Download Markdown to copy the answer.')}
  }
  return <Page title={answer.question}>
    <Link to={'/thread/'+answer.conversation}>← Conversation</Link><p className="muted">{date(answer.created)}</p>
    <div className="toolbar"><button onClick={()=>void copy()}>Copy answer</button><button disabled={save.isPending} onClick={()=>save.mutate(answer.saved)}>{answer.saved?'Unsave answer':'Save answer'}</button>
      {Object.entries({md:'Markdown',pdf:'PDF',bib:'BibTeX',csv:'CSV'}).map(([kind,label])=><a className="button" key={kind} href={'/api/answers/'+answer.id+'/export/'+kind+'/'}>{label}</a>)}
    </div>
    {note&&<p role="status">{note}</p>}<Problem error={save.error}/>
    <div className="panel"><h2>Evidence synthesis</h2><Synthesis answer={answer} quotes/></div>
    <div className="panel"><h2>Retrieved publications</h2>{answer.sources.length===0?<p>No publications available.</p>:<div className="table"><table>
      <thead><tr>{['Study','Year','Study type','Relevant findings','Limitations','Source'].map(title=><th key={title} scope="col">{title}</th>)}</tr></thead>
      <tbody>{answer.sources.map(article=>{
        const relevant=answer.result.sections?.filter(section=>section.citations.some(c=>c.pmid===article.pmid))||[]
        return <tr key={article.pmid}><td><details><summary>{article.title||'Title unavailable'}</summary><Metadata article={article}/></details></td>
          <td>{article.year??'Unavailable'}</td><td>{article.types.join(', ')||'Unavailable'}</td>
          <td>{relevant.flatMap(x=>x.citations.filter(c=>c.pmid===article.pmid).map(c=>c.quote)).join(' ')||'Unavailable'}</td>
          <td>{relevant.filter(x=>x.status==='tentative').map(x=>x.text).join(' ')||'Unavailable'}</td>
          <td><a href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a></td></tr>
      })}</tbody>
    </table></div>}</div>
    {!!answer.provenance.searches?.length&&<details className="panel"><summary>Retrieval provenance</summary><p>Research intent: {answer.provenance.intent}</p><ul>{answer.provenance.searches.map(x=><li key={x.query}>{x.query} ({x.pmids.length} PMIDs)</li>)}</ul></details>}
  </Page>
}
