import { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Link, useNavigate } from 'react-router-dom';
import { BookOpen, Check, Search, Trash2 } from 'lucide-react';
import { api, announceSession, invalidateAuthRequests, type User, type Session, type Preferences, type Article, type SavedSearch } from './api';
import { Page, Problem, fields, SaveForm } from './ui';
import { Metadata } from './answers';
import { ModeNotice, ModelConnection } from './synthesis-mode';
const articleTypes = ['Clinical Trial', 'Randomized Controlled Trial', 'Review', 'Systematic Review', 'Meta-Analysis'];
export function Library({ savedOnly = false }: {
    savedOnly?: boolean;
}) {
    const [params, setParams] = useState('');
    const [filter, setFilter] = useState('');
    const [formKey, setFormKey] = useState(0);
    const [defaults, setDefaults] = useState<Record<string, string>>({});
    const [notice, setNotice] = useState('');
    const client = useQueryClient();
    const live = useQuery({ queryKey: ['literature', params], queryFn: ({ signal }) => api<Article[]>('articles/?' + params, 'GET', undefined, signal), enabled: !!params && !savedOnly });
    const saved = useQuery({ queryKey: ['saved-articles'], queryFn: ({ signal }) => api<Article[]>('saved-articles/', 'GET', undefined, signal) });
    const searches = useQuery({ queryKey: ['saved-searches'], queryFn: ({ signal }) => api<SavedSearch[]>('saved-searches/', 'GET', undefined, signal), enabled: !savedOnly });
    const saveSearch = useMutation({ mutationFn: () => api('saved-searches/', 'POST', Object.fromEntries(new URLSearchParams(params))), onSuccess: () => { void client.invalidateQueries({ queryKey: ['saved-searches'] }); setNotice('Search saved. Run it again from Saved searches.'); } });
    const removeSearch = useMutation({ mutationFn: (id: number) => api('saved-searches/' + id + '/', 'DELETE'), onSuccess: () => client.invalidateQueries({ queryKey: ['saved-searches'] }) });
    const articles = savedOnly ? saved.data?.filter(a => [a.title, a.journal, a.pmid, a.collection, ...a.authors].join(' ').toLowerCase().includes(filter.toLowerCase())) : live.data;
    const searchSaved = searches.data?.some(s => {
        const current = Object.fromEntries(new URLSearchParams(params));
        return Object.keys(s.filters).length === Object.keys(current).length && Object.entries(s.filters).every(([k, v]) => String(v) === current[k]);
    });
    return <Page title={savedOnly ? 'Saved publications' : 'Evidence library'} eyebrow="LITERATURE">
    <p className="page-intro">{savedOnly ? 'Your reading list, organized into collections.' : 'Search PubMed by medical keywords, PMID, or DOI. Inspect the original sources.'}</p>
    <div className="tabs"><Link className={!savedOnly ? 'selected' : ''} to="/library"><Search size={16}/>Search PubMed</Link><Link className={savedOnly ? 'selected' : ''} to="/publications"><BookOpen size={16}/>Saved publications {saved.data && <span className="count">{saved.data.length}</span>}</Link></div>
    {!savedOnly ? <><form key={formKey} className="panel filters" onSubmit={e => {
                const entries = Object.entries(fields(e)).map(([k, v]) => [k, String(v).trim()]).filter(([, v]) => v);
                const query = new URLSearchParams(entries).toString();
                setNotice('');
                if (query === params)
                    void live.refetch();
                else
                    setParams(query);
            }}>
      <label className="wide">Keywords, PMID or DOI<input name="q" defaultValue={defaults.q} placeholder="e.g. diabetes, semaglutide, or 33567185" maxLength={400} required/></label><button className="primary search-submit" disabled={live.isFetching}>{live.isFetching ? 'Searching…' : 'Search PubMed'}</button>
      <label>Year<input name="year" defaultValue={defaults.year} type="number" min="1800" max="2100" placeholder="Any year"/></label>
      <label>Journal<input name="journal" defaultValue={defaults.journal} maxLength={100} placeholder="Any journal"/></label>
      <label>Article type<select name="article_type" defaultValue={defaults.article_type || ''}><option value="">Any type</option>{articleTypes.map(t => <option key={t}>{t}</option>)}</select></label>
      <label>Sort<select name="sort" defaultValue={defaults.sort || 'relevance'}><option value="relevance">Relevance</option><option value="pub date">Publication date</option></select></label>
      <label className="check"><input type="checkbox" name="free" value="true" defaultChecked={defaults.free === 'true'}/>Free full text</label>
    </form>
    {!!searches.data?.length && <details className="saved-searches"><summary>Saved searches ({searches.data.length})</summary>{searches.data.map(s => <div className="saved-search-row" key={s.id}><button onClick={() => { const values = Object.fromEntries(Object.entries(s.filters).map(([k, v]) => [k, String(v)])); setDefaults(values); setFormKey(k => k + 1); setParams(new URLSearchParams(values).toString()); setNotice('Saved search loaded.'); }}>{String(s.filters.q)}<small>{Object.entries(s.filters).filter(([k]) => k !== 'q').map(([k, v]) => k + ': ' + v).join(' · ')}</small></button><button aria-label={'Remove saved search ' + s.filters.q} disabled={removeSearch.isPending} onClick={() => removeSearch.mutate(s.id)}><Trash2 size={16}/></button></div>)}</details>}
    {params && <div className="section-top"><h2>{live.isFetching ? 'Searching literature…' : (live.data?.length ?? 0) + ' publications'}</h2><button disabled={saveSearch.isPending || searchSaved || !searches.data} onClick={() => saveSearch.mutate()}>{saveSearch.isPending ? 'Saving…' : searchSaved ? <><Check size={16}/>Search saved</> : 'Save this search'}</button></div>}
    {notice && <p className="notice success" role="status">{notice}</p>}</> : <input className="saved-filter" aria-label="Search saved publications" placeholder="Search by title, author, PMID, or collection" value={filter} onChange={e => setFilter(e.target.value)}/>}
    <Problem error={(savedOnly ? saved.error : live.error) || saveSearch.error || removeSearch.error || searches.error}/>
    {(savedOnly ? saved.isPending : live.isFetching) && <p role="status">Loading publications…</p>}
    {!params && !savedOnly && <div className="empty"><Search size={27}/><div><strong>Start with a paper or a topic</strong><p>Use filters to narrow the evidence. Short keywords are welcome.</p></div></div>}
    {articles?.length === 0 && <div className="empty"><BookOpen size={26}/><div><strong>{savedOnly ? 'No saved publications found' : 'No publications matched this search'}</strong><p>{savedOnly ? 'Save a paper from Search PubMed, or clear your filter.' : 'Try English medical terms, a PMID, or fewer filters. This does not establish an absence of evidence.'}</p></div></div>}
    {articles?.map(article => <PublicationCard key={article.pmid} article={article} savedOnly={savedOnly} stored={saved.data?.some(r => r.pmid === article.pmid)} ready={!!saved.data}/>)}
  </Page>;
}
function PublicationCard({ article, savedOnly, stored, ready }: {
    article: Article;
    savedOnly: boolean;
    stored?: boolean;
    ready: boolean;
}) {
    const client = useQueryClient();
    const [note, setNote] = useState('');
    const change = useMutation({ mutationFn: ({ remove, collection }: {
            remove?: boolean;
            collection?: string;
        }) => api('articles/' + article.pmid + '/save/', remove ? 'DELETE' : 'PUT', remove ? undefined : { collection: collection ?? '' }), onSuccess: async (_, variables) => {
            setNote(variables.remove ? 'Publication removed.' : 'Publication saved to your library.');
            await client.invalidateQueries({ queryKey: ['saved-articles'] });
        } });
    return <article className="panel publication"><div className="publication-meta"><span>{article.journal || 'Journal unavailable'}</span><span>{article.year ?? 'Year unavailable'}</span></div><h2>{article.title || 'Title unavailable'}</h2><div className="tags">{article.types.map(t => <span key={t}>{t}</span>)}</div>
    <details><summary>Abstract & publication details</summary><Metadata article={article}/></details>
    <div className="toolbar"><a className="source-link" href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a><button className={stored ? 'saved-button' : ''} disabled={change.isPending || stored || !ready} onClick={() => change.mutate({})}>{change.isPending ? 'Saving…' : stored ? <><Check size={16}/>Saved</> : 'Save publication'}</button>{stored && <button className="text-button" disabled={change.isPending} onClick={() => change.mutate({ remove: true })}>Remove from library</button>}</div>
    <Problem error={change.error}/>{note && !savedOnly && <p className="success-text" role="status">{note} <Link to="/publications">View saved publications →</Link></p>}
    {savedOnly && <div className="collection"><SaveForm initial={{ collection: article.collection || '' }} label="Update collection" submit={body => change.mutateAsync({ collection: String(body.collection) })}><label>Collection<input name="collection" placeholder="e.g. Metabolic health" maxLength={80} defaultValue={article.collection}/></label></SaveForm></div>}
  </article>;
}
export function Profile({ user }: {
    user: User;
}) {
    const client = useQueryClient();
    const navigate = useNavigate();
    const logout = useMutation({ mutationFn: async () => {
            invalidateAuthRequests();
            await client.cancelQueries();
            // Refresh the CSRF token first: another tab may have rotated it at sign-in.
            await api<Session>('session/');
            return api<Session>('logout/', 'POST');
        }, onSuccess: async (result) => {
            await client.cancelQueries();
            client.removeQueries({ predicate: q => q.queryKey[0] !== 'session' });
            client.setQueryData<Session>(['session'], old => ({ ...old, ...result }));
            announceSession();
            navigate('/profile');
        } });
    return <Page title="Your profile" eyebrow="ACCOUNT"><p className="page-intro">Manage your research identity.</p><div className="panel account-panel"><div className="identity"><span className="avatar">{user.username.slice(0, 1).toUpperCase()}</span><div><strong>{user.username}</strong><small>Research account</small></div></div>
    <SaveForm initial={{ first_name: user.first_name, last_name: user.last_name }} label="Save profile" submit={async (body) => { const result = await api<User>('profile/', 'PATCH', body); client.setQueryData<Session>(['session'], old => old && ({ ...old, user: result })); }}><label>First name<input name="first_name" defaultValue={user.first_name} maxLength={150}/></label><label>Last name<input name="last_name" defaultValue={user.last_name} maxLength={150}/></label></SaveForm>
  </div><div className="panel account-panel"><h2>Session</h2><p className="muted">Sign out of this browser. Your saved research stays in your account.</p><button disabled={logout.isPending} onClick={() => logout.mutate()}>{logout.isPending ? 'Signing out…' : 'Sign out'}</button><Problem error={logout.error}/></div></Page>;
}
export function Settings({ model, configured }: {
    model?: string;
    configured?: boolean;
}) {
    const [confirm, setConfirm] = useState(false);
    const client = useQueryClient();
    const settings = useQuery({ queryKey: ['preferences'], queryFn: ({ signal }) => api<Preferences>('settings/', 'GET', undefined, signal) });
    const clear = useMutation({ mutationFn: () => api('conversations/', 'DELETE'), onSuccess: () => {
            for (const key of ['history', 'thread', 'answer', 'saved-answers'])
                client.removeQueries({ queryKey: [key] });
            setConfirm(false);
        } });
    return <Page title="Workspace settings" eyebrow="ACCOUNT"><p className="page-intro">Make this workspace work for you.</p><Problem error={settings.error || clear.error}/>{settings.isPending && <p role="status">Loading preferences…</p>}
    {settings.data && <div className="panel account-panel"><h2>Research preferences</h2><ModeNotice settings/><p className="muted">Language and detail apply to new AI-generated responses. Existing answers are unchanged; use Generate new answer to apply new preferences. Source abstracts and quotations retain their original language.</p>{!configured && <p className="language-warning">Chinese is a saved preference, not an active translation service. 中文偏好已保存不代表已有中文回答；请先完成下方模型配置。</p>}<SaveForm initial={{ ...settings.data }} label="Save preferences" submit={async (body) => { const result = await api<Preferences>('settings/', 'PATCH', body); client.setQueryData(['preferences'], result); }}>
      <label>Answer language<select name="language" defaultValue={settings.data.language}>{['English', 'Chinese', 'Spanish', 'French'].map(v => <option key={v}>{v}</option>)}</select></label><label>Response detail<select name="detail" defaultValue={settings.data.detail}>{['Concise', 'Standard', 'Detailed'].map(v => <option key={v}>{v}</option>)}</select></label><label>Display density<select name="display" defaultValue={settings.data.display}>{['Comfortable', 'Compact'].map(v => <option key={v}>{v}</option>)}</select></label>
    </SaveForm></div>}
    <ModelConnection/>
    <div className="panel account-panel danger-panel"><h2>Research history</h2><p className="muted">Deleting history removes your conversations and saved answers. Saved publications and searches remain.</p><button onClick={() => setConfirm(!confirm)}>{confirm ? 'Cancel' : 'Delete all conversations'}</button>{confirm && <div className="notice error">This cannot be undone. <button className="danger" disabled={clear.isPending} onClick={() => clear.mutate()}>Confirm delete all</button></div>}{clear.isSuccess && <p role="status">Research history deleted.</p>}</div>
  </Page>;
}
