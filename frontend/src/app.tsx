import { useEffect, useRef, useState, type ReactNode } from 'react';
import { useQuery, useQueryClient, useMutation } from '@tanstack/react-query';
import { Link, NavLink, Route, Routes, useNavigate, useLocation } from 'react-router-dom';
import { Activity, ArrowUp, ArrowRight, BookOpen, Bookmark, Clock3, FileText, FlaskConical, History, Menu, Microscope, Plus, Settings2, ShieldCheck, Sparkles, UserRound, X, Search, LoaderCircle } from 'lucide-react';
import { api, announceSession, invalidateAuthRequests, date, type Session, type Answer, type Thread, type User, type Preferences } from './api';
import { Library, Settings, Profile } from './library';
import { Conversation, AnswerPage } from './answers';
import { Page, Problem, fields } from './ui';
import { ModeNotice } from './synthesis-mode';
export { Page, Problem, fields } from './ui';
const navigation = [['/', 'Ask AI', Sparkles], ['/history', 'Research history', History], ['/saved', 'Saved answers', Bookmark], ['/library', 'Search PubMed', Search], ['/publications', 'Saved publications', BookOpen], ['/settings', 'Settings', Settings2], ['/profile', 'Profile', UserRound]] as const;
const topics = [['Metabolic health', 'GLP-1 & weight management', 'What is the evidence for GLP-1 receptor agonists in obesity treatment?', Activity], ['Cardiovascular research', 'SGLT2 & heart failure', 'What evidence supports SGLT2 inhibitors in heart failure?', FlaskConical], ['Digital medicine', 'AI in clinical documentation', 'What studies investigate large language models in clinical documentation?', Microscope]] as const;
export function App() {
    const client = useQueryClient();
    const session = useQuery({ queryKey: ['session'], queryFn: ({ signal }) => api<Session>('session/', 'GET', undefined, signal) });
    const user = session.data?.user;
    const prefs = useQuery({ queryKey: ['preferences'], queryFn: ({ signal }) => api<Preferences>('settings/', 'GET', undefined, signal), enabled: !!user });
    const [open, setOpen] = useState(false);
    const location = useLocation();
    const menu = useRef<HTMLButtonElement>(null);
    const drawer = useRef<HTMLElement>(null);
    useEffect(() => {
        const check = () => void client.invalidateQueries({ queryKey: ['session'] });
        const storage = (e: StorageEvent) => { if (e.key === 'medevidence-auth-event') {
            invalidateAuthRequests();
            void client.cancelQueries();
            client.removeQueries({ predicate: q => q.queryKey[0] !== 'session' });
            check();
        } };
        window.addEventListener('session-check', check);
        window.addEventListener('storage', storage);
        return () => { window.removeEventListener('session-check', check); window.removeEventListener('storage', storage); };
    }, [client]);
    useEffect(() => { setOpen(false); }, [location.pathname]);
    useEffect(() => {
        if (!open)
            return;
        const savedOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';
        drawer.current?.querySelector<HTMLButtonElement>('.close-menu')?.focus();
        const key = (event: KeyboardEvent) => {
            if (event.key === 'Escape') {
                setOpen(false);
                menu.current?.focus();
            }
            if (event.key === 'Tab') {
                const items = drawer.current?.querySelectorAll<HTMLElement>('a,button');
                if (!items?.length)
                    return;
                const first = items[0], last = items[items.length - 1];
                if (event.shiftKey && document.activeElement === first) {
                    event.preventDefault();
                    last.focus();
                }
                else if (!event.shiftKey && document.activeElement === last) {
                    event.preventDefault();
                    first.focus();
                }
            }
        };
        window.addEventListener('keydown', key);
        return () => { document.body.style.overflow = savedOverflow; window.removeEventListener('keydown', key); queueMicrotask(() => menu.current?.focus()); };
    }, [open]);
    function protectedPage(content: ReactNode) {
        if (!session.data)
            return <Page title={session.error ? 'Workspace unavailable' : 'Loading workspace…'}><Problem error={session.error}/></Page>;
        return user ? content : <Page title="Your research, in one place"><p>Sign in to access your conversations and saved evidence.</p><Link className="button primary" to="/profile">Sign in or register <ArrowRight size={16}/></Link></Page>;
    }
    return <div className={'workspace' + (prefs.data?.display === 'Compact' ? ' compact' : '')}>
    <a className="skip-link" href="#content">Skip to content</a>
    {open && <button className="scrim" aria-label="Close navigation" onClick={() => { setOpen(false); menu.current?.focus(); }}/>}
    <aside ref={drawer} className={'sidebar' + (open ? ' open' : '')} aria-label="Main navigation">
      <button className="close-menu" aria-label="Close menu" onClick={() => { setOpen(false); menu.current?.focus(); }}><X size={20}/></button>
      <Link className="brand" to="/"><span className="mark"><Activity size={24}/></span><span>MedEvidence<small>RESEARCH WORKSPACE <b>3.0</b></small></span></Link>
      <Link className="new" to="/"><Plus size={18}/>New research</Link>
      <nav>{navigation.map(([path, label, Icon], i) => <div key={path}>{(i === 0 || i === 3 || i === 5) && <p className="nav-label">{i === 0 ? 'WORKSPACE' : i === 3 ? 'LITERATURE' : 'ACCOUNT'}</p>}<NavLink end to={path}><Icon size={18}/>{label}</NavLink></div>)}</nav>
      <div className="sidebar-foot"><span className="source-dot"/> PubMed literature source<small>Abstracts & publication metadata</small></div>
    </aside>
    <main inert={open}>
      <header className="topbar"><button ref={menu} className="menu" aria-label="Open menu" aria-expanded={open} onClick={() => setOpen(true)}><Menu size={22}/></button><span className="breadcrumb">Workspace <span>/</span> {navigation.find(n => n[0] === location.pathname)?.[1] || 'Research'}</span><Link className="account" to="/profile"><UserRound size={17}/><span>{user?.username || 'Sign in'}</span></Link></header>
      <div className="disclaimer"><ShieldCheck size={15}/><span>Research demonstration — not for clinical use.</span></div>
      <div id="content" tabIndex={-1}><Problem error={session.error}/><Routes>
        <Route path="/" element={<Home user={user} configured={session.data?.generation_configured}/>}/>
        <Route path="/profile" element={user ? <Profile key={user.username} user={user}/> : <Auth ready={!!session.data}/>}/>
        <Route path="/history" element={protectedPage(<HistoryPage />)}/><Route path="/saved" element={protectedPage(<Saved />)}/>
        <Route path="/library" element={protectedPage(<Library key="search"/>)}/><Route path="/publications" element={protectedPage(<Library key="saved" savedOnly/>)}/>
        <Route path="/settings" element={protectedPage(<Settings model={session.data?.model} configured={session.data?.generation_configured}/>)}/>
        <Route path="/thread/:id" element={protectedPage(<Conversation key={location.pathname}/>)}/><Route path="/answer/:id" element={protectedPage(<AnswerPage key={location.pathname}/>)}/>
        <Route path="*" element={<Page title="Page unavailable"><Link to="/">Return to your workspace</Link></Page>}/>
      </Routes></div>
    </main>
  </div>;
}
export function Composer({ question, change, submit, busy, follow = false, configured }: {
    question: string;
    change: (q: string) => void;
    submit: () => void;
    busy: boolean;
    follow?: boolean;
    configured?: boolean;
}) {
    const ready = question.trim().length > 0 && !busy;
    return <form className="composer" onSubmit={e => { e.preventDefault(); if (ready)
        submit(); }}>
    <label className="sr-only" htmlFor={follow ? 'followup' : 'question'}>{follow ? 'Follow-up question' : 'Research question'}</label>
    <textarea id={follow ? 'followup' : 'question'} value={question} onChange={e => change(e.target.value)} maxLength={2000} disabled={busy} placeholder={follow ? 'Ask a follow-up about this research…' : 'Ask a question. Start with the evidence.'} onKeyDown={e => { if (e.key === 'Enter' && !e.shiftKey && !e.nativeEvent.isComposing) {
        e.preventDefault();
        if (ready)
            submit();
    } }}/>
    <div className="composer-bottom"><span><BookOpen size={16}/>PubMed sources</span><button className="primary" disabled={!ready}>{busy ? <LoaderCircle size={17} className="spin"/> : <ArrowUp size={17}/>} {busy ? 'Working…' : configured === false ? 'Search literature' : 'Ask AI'}</button></div>
    <div className="composer-help">English or supported Chinese medical terms · Short keywords welcome · {question.length}/2,000</div>
  </form>;
}
export function useAsk() {
    const client = useQueryClient();
    return useMutation({ mutationFn: (body: {
            question: string;
            conversation?: number;
        }) => api<Answer>('ask/', 'POST', body), onSuccess: answer => {
            client.setQueryData(['answer', String(answer.id)], answer);
            void client.invalidateQueries({ queryKey: ['history'] });
            void client.invalidateQueries({ queryKey: ['thread', String(answer.conversation)] });
        } });
}
function Home({ user, configured }: {
    user?: User | null;
    configured?: boolean;
}) {
    const [question, change] = useState('');
    const [gate, setGate] = useState(false);
    const navigate = useNavigate();
    const ask = useAsk();
    const history = useQuery({ queryKey: ['history', '', 'newest'], queryFn: ({ signal }) => api<Thread[]>('conversations/', 'GET', undefined, signal), enabled: !!user });
    return <div className="home"><section className="hero"><div className="eyebrow"><span className="source-dot"/> LITERATURE INTO PERSPECTIVE</div><h1>Better questions.<br /><em>Grounded in evidence.</em></h1><p className="hero-subtitle">Explore biomedical literature, follow the sources,<br className="desktop"/> and build a research trail you can return to.</p>
    <ModeNotice/><Composer question={question} change={change} busy={ask.isPending} configured={configured} submit={() => { if (!user) {
        setGate(true);
        return;
    } ask.mutate({ question }, { onSuccess: a => navigate('/thread/' + a.conversation) }); }}/>
    {gate && !user && <div className="notice"><Link to="/profile">Sign in or create an account</Link> to start a research conversation.</div>}
    {ask.isPending && <p role="status">{configured ? 'Retrieving abstracts, generating your answer and checking claims. This can take a few minutes.' : 'Searching PubMed. Source publications will appear when retrieval completes.'}</p>}<Problem error={ask.error}/>
  </section><div className="section-top"><h2>A starting point for your research</h2><span className="muted">Explore a topic</span></div><div className="topics">{topics.map(([subtitle, title, prompt, Icon]) => <button className="topic" key={title} onClick={() => { change(prompt); document.querySelector('textarea')?.focus(); window.scrollTo({ top: 0, behavior: 'smooth' }); }}><Icon size={21}/><small>{subtitle}</small><strong>{title}</strong><ArrowRight className="topic-arrow" size={17}/></button>)}</div>
    <div className="section-top"><h2>Recent conversations</h2><Link to="/history">View all <ArrowRight size={15}/></Link></div><Problem error={history.error}/>
    {history.data?.length ? <ThreadList rows={history.data.slice(0, 4)}/> : <div className="empty"><Clock3 size={25}/><div><strong>Your next question starts here</strong><p>Research conversations will appear in this workspace.</p></div></div>}
    <footer><ShieldCheck size={15}/> Sources you can inspect. Claims you should review.</footer></div>;
}
function Auth({ ready }: {
    ready: boolean;
}) {
    const [create, setCreate] = useState(false);
    const client = useQueryClient();
    const navigate = useNavigate();
    const action = useMutation({ mutationFn: (body: unknown) => { invalidateAuthRequests(); return api<Session>(create ? 'register/' : 'login/', 'POST', body); }, onSuccess: async (data) => {
            await client.cancelQueries();
            client.removeQueries({ predicate: q => q.queryKey[0] !== 'session' });
            client.setQueryData<Session>(['session'], old => ({ ...old, ...data }));
            announceSession();
            navigate('/');
            void client.invalidateQueries({ queryKey: ['session'] });
        } });
    return <Page title={create ? 'Create your workspace' : 'Welcome back'} eyebrow="YOUR RESEARCH, ORGANIZED"><p className="page-intro">Use a research account. Keep patient information out of your questions.</p><form className="panel fields auth-form" onSubmit={e => { const data = fields(e); if (!action.isPending)
        action.mutate(data); }}><label>Username<input name="username" autoComplete="username" required maxLength={150}/></label><label>Password<input name="password" type="password" autoComplete={create ? 'new-password' : 'current-password'} required minLength={create ? 8 : 1} maxLength={128}/></label>{create && <p className="muted">Use at least 8 characters and a password that is not common or entirely numeric.</p>}<Problem error={action.error}/><button className="primary" disabled={!ready || action.isPending}>{action.isPending ? 'Please wait…' : create ? 'Create account' : 'Sign in'}</button><button type="button" disabled={action.isPending} onClick={() => { setCreate(!create); action.reset(); }}>{create ? 'Use an existing account' : 'Create a research account'}</button></form></Page>;
}
function ThreadList({ rows }: {
    rows: Thread[];
}) { return <div className="list">{rows.map(row => <Link className="list-row" key={row.id} to={'/thread/' + row.id}><FileText size={19}/><span>{row.title}</span><small>{date(row.updated)}</small><ArrowRight size={16}/></Link>)}</div>; }
function HistoryPage() {
    const [q, setQ] = useState('');
    const [sort, setSort] = useState('newest');
    const history = useQuery({ queryKey: ['history', q, sort], queryFn: ({ signal }) => api<Thread[]>('conversations/?' + new URLSearchParams({ q, sort }), 'GET', undefined, signal) });
    return <Page title="Research history"><p className="page-intro">Every question, follow-up, and source. All in one place.</p><form className="toolbar search-toolbar" onSubmit={e => setQ(String(fields(e).q))}><input name="q" aria-label="Search history" placeholder="Search conversations"/><button className="primary">Search</button><select value={sort} onChange={e => setSort(e.target.value)} aria-label="Sort history"><option value="newest">Newest first</option><option value="oldest">Oldest first</option></select></form><Problem error={history.error}/>{history.isPending && <p role="status">Loading conversations…</p>}{history.data?.length === 0 && <div className="empty">No conversations found. Start a new question or change your search.</div>}<ThreadList rows={history.data || []}/></Page>;
}
function Saved() {
    const saved = useQuery({ queryKey: ['saved-answers'], queryFn: ({ signal }) => api<Answer[]>('saved-answers/', 'GET', undefined, signal) });
    return <Page title="Saved answers"><p className="page-intro">Bookmarked research responses. Looking for papers? <Link to="/publications">Open saved publications →</Link></p><Problem error={saved.error}/>{saved.isPending && <p role="status">Loading saved answers…</p>}{saved.data?.length === 0 && <div className="empty"><Bookmark size={25}/><div><strong>No saved answers yet</strong><p>Use “Save answer” on a research response to keep it here.</p></div></div>}<div className="list">{saved.data?.map(x => <Link className="list-row" key={x.id} to={'/answer/' + x.id}><Bookmark size={18}/><span>{x.question}</span><small>{date(x.created)}</small><ArrowRight size={16}/></Link>)}</div></Page>;
}
