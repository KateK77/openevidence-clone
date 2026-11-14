import {useState} from 'react'
import {useMutation,useQuery,useQueryClient} from '@tanstack/react-query'
import {useNavigate} from 'react-router-dom'
import {api,type User,type Session,type Preferences,type Article} from './api'
import {Page,Problem,fields} from './app'
import {Metadata} from './answers'

const articleTypes=['Clinical Trial','Randomized Controlled Trial','Review','Systematic Review','Meta-Analysis']
export function Library(){
  const [params,setParams]=useState('')
  const [search,setSearch]=useState(true)
  const [filter,setFilter]=useState('')
  const client=useQueryClient()
  const live=useQuery({queryKey:['literature',params],queryFn:()=>api<Article[]>('articles/?'+params),enabled:!!params&&search})
  const saved=useQuery({queryKey:['saved-articles'],queryFn:()=>api<Article[]>('saved-articles/')})
  const change=useMutation({mutationFn:({pmid,collection}:{pmid:string;collection?:string})=>api('articles/'+pmid+'/save/',collection===undefined?'DELETE':'PUT',collection===undefined?undefined:{collection}),
    onSuccess:()=>client.invalidateQueries({queryKey:['saved-articles']})})
  const articles=search?live.data:saved.data?.filter(a=>[a.title,a.journal,a.pmid,a.collection,...a.authors].join(' ').toLowerCase().includes(filter.toLowerCase()))
  return <Page title="Evidence library">
    <p className="muted">Search PubMed and organize saved publications into collections.</p>
    <div className="toolbar"><button aria-pressed={search} onClick={()=>setSearch(true)}>Search PubMed</button><button aria-pressed={!search} onClick={()=>setSearch(false)}>Saved publications</button></div>
    {search?<form className="panel filters" onSubmit={e=>{
      const entries=Object.entries(fields(e)).map(([k,v])=>[k,String(v)]).filter(([,v])=>v.trim())
      const query=new URLSearchParams(entries).toString()
      if(query===params) void live.refetch()
      else setParams(query)
    }}>
      <label className="wide">Keywords, PMID or DOI<input name="q" placeholder="e.g. heart failure randomized trial" maxLength={400} required/></label>
      <button className="primary">Search</button>
      <label>Year<input name="year" type="number" min="1800" max="2100"/></label>
      <label>Journal<input name="journal" maxLength={100}/></label>
      <label>Article type<select name="article_type"><option value="">Any</option>{articleTypes.map(t=><option key={t}>{t}</option>)}</select></label>
      <label>Sort<select name="sort"><option value="relevance">Relevance</option><option value="pub date">Publication date</option></select></label>
      <label className="check"><input type="checkbox" name="free" value="true"/> Free full text</label>
    </form>:<input aria-label="Search saved publications" placeholder="Search saved publications" value={filter} onChange={e=>setFilter(e.target.value)}/>}
    <Problem error={change.error||(search?live.error:saved.error)}/>
    {(search?live.isFetching:saved.isPending)&&<p role="status">Loading publications…</p>}
    {articles?.length===0&&<p className="empty">No publications found.</p>}
    {articles?.map(article=>{
      const stored=saved.data?.some(row=>row.pmid===article.pmid)
      return <article className="panel" key={article.pmid}>
        <small className="muted">{article.journal||'Journal unavailable'} · {article.year??'Year unavailable'}</small>
        <h2>{article.title||'Title unavailable'}</h2>
        <details><summary>Publication details</summary><Metadata article={article}/></details>
        <div className="toolbar"><a href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a>
          <button disabled={change.isPending||!saved.data} onClick={()=>change.mutate({pmid:article.pmid,collection:stored?undefined:''})}>{stored?'Remove from library':'Save publication'}</button>
        </div>
        {!search&&<form className="toolbar" onSubmit={e=>change.mutate({pmid:article.pmid,collection:String(fields(e).collection)})}><input name="collection" aria-label="Collection name" placeholder="Collection name" maxLength={80} defaultValue={article.collection}/><button disabled={change.isPending}>Update collection</button></form>}
      </article>
    })}
  </Page>
}
export function Profile({user}:{user:User}){
  const client=useQueryClient()
  const navigate=useNavigate()
  const update=useMutation({mutationFn:(body:unknown)=>api<User>('profile/','PATCH',body),
    onSuccess:result=>client.setQueryData<Session>(['session'],old=>old&&({...old,user:result}))})
  const logout=useMutation({mutationFn:()=>api<Session>('logout/','POST'),onSuccess:result=>{
    client.clear()
    client.setQueryData(['session'],result)
    navigate('/')
  }})
  return <Page title="Profile"><form className="panel fields" onSubmit={e=>update.mutate(fields(e))}>
    <label>Username<input readOnly value={user.username}/></label>
    <label>First name<input name="first_name" defaultValue={user.first_name} maxLength={150}/></label>
    <label>Last name<input name="last_name" defaultValue={user.last_name} maxLength={150}/></label>
    <button className="primary" disabled={update.isPending||logout.isPending}>Save profile</button>
    <button type="button" disabled={update.isPending||logout.isPending} onClick={()=>logout.mutate()}>Sign out</button>
    <Problem error={update.error||logout.error}/>{update.isSuccess&&<p role="status">Profile saved.</p>}
  </form></Page>
}

export function Settings({model}:{model?:string}){
  const [confirm,setConfirm]=useState(false)
  const client=useQueryClient()
  const settings=useQuery({queryKey:['preferences'],queryFn:()=>api<Preferences>('settings/')})
  const update=useMutation({mutationFn:(body:unknown)=>api<Preferences>('settings/','PATCH',body),
    onSuccess:data=>client.setQueryData(['preferences'],data)})
  const clear=useMutation({mutationFn:()=>api('conversations/','DELETE'),onSuccess:()=>{
    for(const key of ['history','thread','answer','saved-answers']) client.removeQueries({queryKey:[key]})
    setConfirm(false)
  }})
  return <Page title="Settings">
    <Problem error={settings.error||update.error||clear.error}/>
    {settings.isPending&&<p role="status">Loading preferences…</p>}
    {settings.data&&<form className="panel fields" onSubmit={e=>update.mutate(fields(e))}>
      <label>Answer language<select name="language" defaultValue={settings.data.language}>{['English','Chinese','Spanish','French'].map(v=><option key={v}>{v}</option>)}</select></label>
      <label>Response detail<select name="detail" defaultValue={settings.data.detail}>{['Concise','Standard','Detailed'].map(v=><option key={v}>{v}</option>)}</select></label>
      <label>Display density<select name="display" defaultValue={settings.data.display}>{['Comfortable','Compact'].map(v=><option key={v}>{v}</option>)}</select></label>
      <p className="muted">Server model · {model||'Unconfigured'}</p>
      <button className="primary" disabled={update.isPending}>Save preferences</button>
      {update.isSuccess&&<p role="status">Preferences saved.</p>}
    </form>}
    <div className="panel"><h2>Research history</h2><button onClick={()=>setConfirm(!confirm)}>{confirm?'Cancel':'Delete all conversations'}</button>
      {confirm&&<p className="notice">Delete all conversations and their saved answers? <button disabled={clear.isPending} onClick={()=>clear.mutate()}>Confirm delete all</button></p>}
      {clear.isSuccess&&<p role="status">Research history deleted.</p>}
    </div>
  </Page>
}
