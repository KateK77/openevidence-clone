import {useState,type ReactNode,type FormEvent} from 'react'
import {useQuery,useQueryClient,useMutation} from '@tanstack/react-query'
import {Link,NavLink,Route,Routes,useNavigate} from 'react-router-dom'
import {Activity,ArrowUp,ArrowRight,BookOpen,Bookmark,Clock3,FileText,FlaskConical,History,Menu,Microscope,Plus,Settings2,ShieldCheck,Sparkles,UserRound} from 'lucide-react'
import {api,date,type Session,type Answer,type Thread,type User,type Preferences} from './api'
import {Library,Settings,Profile} from './library'
import {Conversation,AnswerPage} from './answers'

const navigation=[
  ['/', 'Ask AI', Sparkles], ['/history','Research History',History], ['/saved','Saved Answers',Bookmark],
  ['/library','Evidence Library',BookOpen], ['/settings','Settings',Settings2], ['/profile','Profile',UserRound],
] as const
const topics=[
  ['GLP-1 receptor agonists','Weight management','What is the evidence for GLP-1 receptor agonists in obesity treatment?',Activity],
  ['SGLT2 inhibitors','Heart failure','What evidence supports SGLT2 inhibitors in heart failure?',FlaskConical],
  ['LLMs in clinical care','Clinical documentation','What studies investigate large language models in clinical documentation?',Microscope],
] as const

export function App(){
  const session=useQuery({queryKey:['session'],queryFn:()=>api<Session>('session/')})
  const user=session.data?.user
  const prefs=useQuery({queryKey:['preferences'],queryFn:()=>api<Preferences>('settings/'),enabled:!!user})
  const [open,setOpen]=useState(false)
  function protectedPage(content:ReactNode){
    if(!session.data) return <Page title={session.error?'Workspace unavailable':'Loading workspace'} />
    return user ? content : <Page title="Sign in to your workspace"><p>Access your conversations and saved evidence.</p><Link className="button primary" to="/profile">Sign in or register</Link></Page>
  }
  return <div className={prefs.data?.display==='Compact'?'workspace compact':'workspace'}>
    {open&&<button className="scrim" aria-label="Close menu" onClick={()=>setOpen(false)}/>}
    <aside className={open?'sidebar open':'sidebar'}>
      <Link className="brand" to="/" onClick={()=>setOpen(false)}><span className="mark"><Activity size={22}/></span><span>MedEvidence <em>AI</em><small>RESEARCH WORKSPACE</small></span></Link>
      <Link className="new" to="/" onClick={()=>setOpen(false)}><Plus size={17}/>New research</Link>
      <nav aria-label="Workspace">
        {navigation.map(([path,label,Icon],index)=><div key={path}>
          {(index===0||index===4)&&<p>{index===0?'WORKSPACE':'ACCOUNT'}</p>}
          <NavLink end to={path} onClick={()=>setOpen(false)}><Icon size={17}/>{label}</NavLink>
        </div>)}
      </nav>
      <div className="sidebar-foot"><i/>PubMed literature source</div>
    </aside>
    <main>
      <header className="topbar"><button className="menu" aria-label="Open menu" onClick={()=>setOpen(true)}><Menu size={22}/></button><span>Clinical research workspace</span><Link to="/profile"><UserRound size={16}/>{user?.username||'Sign in'}</Link></header>
      <div className="disclaimer"><ShieldCheck size={15}/> RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.</div>
      <Problem error={session.error}/>
      <Routes>
        <Route path="/" element={<Home user={user}/>}/>
        <Route path="/profile" element={user?<Profile user={user}/>:<Auth ready={!!session.data}/>}/>
        <Route path="/history" element={protectedPage(<HistoryPage/>)}/>
        <Route path="/saved" element={protectedPage(<Saved/>)}/>
        <Route path="/library" element={protectedPage(<Library/>)}/>
        <Route path="/settings" element={protectedPage(<Settings model={session.data?.model}/>)}/>
        <Route path="/thread/:id" element={protectedPage(<Conversation/>)}/>
        <Route path="/answer/:id" element={protectedPage(<AnswerPage/>)}/>
        <Route path="*" element={<Page title="Page unavailable"><Link to="/">Return to Ask AI</Link></Page>}/>
      </Routes>
    </main>
  </div>
}
export function Problem({error}:{error?:Error|null}){
  return error?<p role="alert" className="notice error">{error.message}</p>:null
}
export function Page({title,children}:{title:string;children?:ReactNode}){
  return <section className="page"><h1>{title}</h1>{children}</section>
}
export function fields(event:FormEvent<HTMLFormElement>){
  event.preventDefault()
  return Object.fromEntries(new FormData(event.currentTarget))
}
export function Composer({question,change,submit,busy,follow=false}:{
  question:string;change:(q:string)=>void;submit:()=>void;busy:boolean;follow?:boolean
}){
  const ready=question.trim().length>=5&&!busy
  return <form className="composer" onSubmit={event=>{event.preventDefault();if(ready) submit()}}>
    <textarea value={question} onChange={e=>change(e.target.value)} maxLength={2000}
      aria-label={follow?'Follow-up question':'Research question'} placeholder={follow?'Ask a follow-up question…':'Enter a clinical or biomedical research question…'}
      onKeyDown={e=>{if(e.key==='Enter'&&!e.shiftKey&&!e.nativeEvent.isComposing){e.preventDefault();if(ready) submit()}}}/>
    <div><span><BookOpen size={15}/> PubMed literature</span><button className="primary" disabled={!ready}>{busy?'Retrieving evidence…':'Ask AI'} <ArrowUp size={16}/></button></div>
  </form>
}
export function useAsk(){
  const client=useQueryClient()
  return useMutation({mutationFn:(body:{question:string;conversation?:number})=>api<Answer>('ask/','POST',body),
    onSuccess:answer=>{
      client.setQueryData(['answer',String(answer.id)],answer)
      void client.invalidateQueries({queryKey:['history']})
      void client.invalidateQueries({queryKey:['thread',String(answer.conversation)]})
    }})
}
function Home({user}:{user?:User|null}){
  const [question,change]=useState('')
  const [gate,setGate]=useState(false)
  const navigate=useNavigate()
  const ask=useAsk()
  const history=useQuery({queryKey:['history','','newest'],queryFn:()=>api<Thread[]>('conversations/'),enabled:!!user})
  return <div className="home">
    <section className="hero">
      <div className="hero-icon"><Sparkles size={28}/></div>
      <h1>Ask a clinical research question</h1>
      <p>Search biomedical literature and explore AI synthesis<br className="desktop"/> linked to the publications it draws from.</p>
      <Composer question={question} change={change} busy={ask.isPending} submit={()=>{
        if(!user){setGate(true);return}
        ask.mutate({question},{onSuccess:answer=>navigate('/thread/'+answer.conversation)})
      }}/>
      {ask.isPending&&<p role="status">Searching PubMed and evaluating available evidence.</p>}
      {gate&&!user&&<p className="notice"><Link to="/profile">Sign in or register</Link> to submit and save your question.</p>}
      <Problem error={ask.error}/>
    </section>
    <h2>Explore research topics</h2>
    <div className="topics">{topics.map(([title,subtitle,prompt,Icon])=><button key={title} className="topic" onClick={()=>{change(prompt);document.querySelector('textarea')?.focus()}}>
      <span className="topic-icon"><Icon size={18}/></span><span><strong>{title}</strong><small>{subtitle}</small></span><ArrowRight className="topic-arrow" size={16}/>
    </button>)}</div>
    <div className="section-top"><h2>Recent conversations</h2><Link to="/history">View history <ArrowRight size={15}/></Link></div>
    <Problem error={history.error}/>
    {history.data?.length?<ThreadList rows={history.data.slice(0,4)}/>:<div className="empty"><Clock3 size={21}/><div><strong>No recent conversations</strong><p>Your research questions will appear here.</p></div></div>}
    <footer>Evidence synthesis uses available abstracts and publication metadata.</footer>
  </div>
}
function Auth({ready}:{ready:boolean}){
  const [create,setCreate]=useState(false)
  const client=useQueryClient()
  const navigate=useNavigate()
  const action=useMutation({mutationFn:(body:unknown)=>api<Session>(create?'register/':'login/','POST',body),onSuccess:data=>{
    client.setQueryData<Session>(['session'],old=>({...old,...data}))
    navigate('/')
  }})
  return <Page title={create?'Create an account':'Sign in'}>
    <p className="muted">Use a research account. Keep patient information out of your questions.</p>
    <form className="panel fields" onSubmit={e=>action.mutate(fields(e))}>
      <label>Username<input name="username" autoComplete="username" required maxLength={150}/></label>
      <label>Password<input name="password" type="password" autoComplete={create?'new-password':'current-password'} required minLength={create?8:1} maxLength={128}/></label>
      <Problem error={action.error}/><button className="primary" disabled={!ready||action.isPending}>{create?'Create account':'Sign in'}</button>
      <button type="button" onClick={()=>{setCreate(!create);action.reset()}}>{create?'Use an existing account':'Create a research account'}</button>
    </form>
  </Page>
}
function ThreadList({rows}:{rows:Thread[]}){
  return <div className="list">{rows.map(row=><Link className="list-row" key={row.id} to={'/thread/'+row.id}><FileText size={18}/><span>{row.title}</span><small>{date(row.updated)}</small><ArrowRight size={15}/></Link>)}</div>
}
function HistoryPage(){
  const [q,setQ]=useState('')
  const [sort,setSort]=useState('newest')
  const history=useQuery({queryKey:['history',q,sort],queryFn:()=>api<Thread[]>('conversations/?'+new URLSearchParams({q,sort}))})
  return <Page title="Research history"><form className="toolbar" onSubmit={e=>setQ(String(fields(e).q))}>
    <input name="q" aria-label="Search history" placeholder="Search conversations"/><button>Search</button>
    <select value={sort} onChange={e=>setSort(e.target.value)} aria-label="Sort history"><option value="newest">Newest first</option><option value="oldest">Oldest first</option></select>
    </form><Problem error={history.error}/>{history.isPending&&<p role="status">Loading conversations…</p>}
    {history.data?.length===0&&<p className="empty">No conversations found.</p>}<ThreadList rows={history.data||[]}/>
  </Page>
}
function Saved(){
  const saved=useQuery({queryKey:['saved-answers'],queryFn:()=>api<Answer[]>('saved-answers/')})
  return <Page title="Saved answers"><Problem error={saved.error}/>{saved.isPending&&<p role="status">Loading answers…</p>}
    {saved.data?.length===0&&<p className="empty">No saved answers yet.</p>}
    <div className="list">{saved.data?.map(x=><Link className="list-row" key={x.id} to={'/answer/'+x.id}><Bookmark size={17}/><span>{x.question}</span><small>{date(x.created)}</small></Link>)}</div>
  </Page>
}
