import { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Check, ArrowLeft, Download, Bookmark, FileText } from 'lucide-react';
import { api, date, downloadAnswer, type Answer, type Thread, type Article } from './api';
import { Composer, useAsk } from './app';
import { Page, Problem, SaveForm } from './ui';
export function Conversation() {
    const { id } = useParams();
    const client = useQueryClient();
    const navigate = useNavigate();
    const thread = useQuery({ queryKey: ['thread', id], queryFn: ({ signal }) => api<Thread>('conversations/' + id + '/', 'GET', undefined, signal) });
    const ask = useAsk();
    const [question, change] = useState('');
    const [mode, setMode] = useState('');
    const [note, setNote] = useState('');
    const command = useMutation({ mutationFn: ({ method, body }: {
            method: string;
            body?: unknown;
        }) => api<Thread | undefined>('conversations/' + id + '/', method, body), onSuccess: data => {
            void client.invalidateQueries({ queryKey: ['history'] });
            if (data) {
                client.setQueryData(['thread', id], data);
                setNote('Conversation title saved.');
            }
            else {
                for (const key of ['answer', 'saved-answers', 'thread'])
                    client.removeQueries({ queryKey: [key] });
                navigate('/history');
            }
        } });
    return <Page title={thread.data?.title || 'Conversation'} eyebrow="RESEARCH CONVERSATION"><Link className="back-link" to="/history"><ArrowLeft size={16}/>Research history</Link><Problem error={thread.error || ask.error || command.error}/>{thread.isPending && <p role="status">Loading conversation…</p>}
    {thread.data && <><div className="toolbar"><button onClick={() => setMode(mode === 'rename' ? '' : 'rename')}>Rename</button><button onClick={() => setMode(mode === 'delete' ? '' : 'delete')}>Delete conversation</button></div>
      {mode === 'rename' && <div className="panel"><SaveForm initial={{ title: thread.data.title }} label="Save title" submit={body => command.mutateAsync({ method: 'PATCH', body })}><label>Conversation title<input name="title" defaultValue={thread.data.title} required maxLength={180}/></label></SaveForm></div>}
      {mode === 'delete' && <div className="notice error">Delete this conversation and its saved answers? This cannot be undone. <button className="danger" disabled={command.isPending} onClick={() => command.mutate({ method: 'DELETE' })}>Confirm delete</button><button onClick={() => setMode('')}>Cancel</button></div>}
      {note && mode !== 'rename' && <p role="status">{note}</p>}
      <div className="conversation-timeline">{thread.data.turns?.map((answer, i) => <article className="panel turn" key={answer.id}><div className="turn-meta"><span className="turn-number">{String(i + 1).padStart(2, '0')}</span><small>{date(answer.created)}</small></div><h2>{answer.question}</h2><Synthesis answer={answer}/><Link className="answer-link" to={'/answer/' + answer.id}>View answer and evidence →</Link></article>)}</div>
      <div className="followup"><h2>Continue this research</h2><p className="muted">Ask about limitations, compare findings, or explore a related question.</p><Composer question={question} change={change} busy={ask.isPending} follow submit={() => ask.mutate({ question, conversation: Number(id) }, { onSuccess: () => change('') })}/></div>
    </>}
  </Page>;
}
const statuses: Record<string, string> = { complete: 'Synthesis complete', retrieval_only: 'Literature only', retrieval_error: 'Retrieval unavailable', generation_error: 'Generation unavailable', insufficient: 'Evidence gap', demo: 'Synthetic demo' };
function Synthesis({ answer, quotes }: {
    answer: Answer;
    quotes?: boolean;
}) {
    return <div className="synthesis"><div className="toolbar"><span className={'pill ' + (answer.status === 'complete' ? 'complete' : '')}>{statuses[answer.status] || answer.status}</span>{answer.model && <small>Model: {answer.model}</small>}<small>{answer.sources.length} PubMed records</small></div>
    {answer.result.message && <p className="synthesis-message">{answer.result.message}</p>}
    {answer.result.sections?.map((section, i) => <div className={'finding ' + section.status} key={i}><strong>{section.status === 'supported' ? 'Source-linked finding' : section.status === 'tentative' ? 'Tentative interpretation' : 'Evidence gap'}</strong><p>{section.text}</p>{section.citations.map((citation, j) => <div className="citation" key={j}><a href={'https://pubmed.ncbi.nlm.nih.gov/' + citation.pmid + '/'} target="_blank" rel="noreferrer">PMID {citation.pmid} ↗</a>{quotes && <details><summary>Matched abstract excerpt</summary><blockquote>{citation.quote}</blockquote></details>}</div>)}</div>)}
    {quotes && !!answer.result.sections?.length && <p className="scope-note">Citation checks confirm that IDs were retrieved and quotations match the supplied abstracts. They do not independently establish that an interpretation is correct.</p>}
  </div>;
}
export function Metadata({ article }: {
    article: Article;
}) {
    return <div className="metadata"><p>{article.authors.join(', ') || 'Authors unavailable'}</p><dl><dt>Journal</dt><dd>{article.journal || 'Unavailable'}</dd>{article.electronic_date && <><dt>Electronic publication</dt><dd>{article.electronic_date}</dd></>}{article.issue_date && <><dt>Journal issue</dt><dd>{article.issue_date}</dd></>}{!article.electronic_date && !article.issue_date && <><dt>Publication date (type unavailable)</dt><dd>{article.date || 'Unavailable'}</dd></>}<dt>DOI</dt><dd>{article.doi ? <a href={'https://doi.org/' + encodeURIComponent(article.doi)} target="_blank" rel="noreferrer">{article.doi} ↗</a> : 'Unavailable'}</dd></dl><h3>Source abstract</h3><p className="abstract">{article.abstract || 'No abstract is available for this record.'}</p></div>;
}
export function AnswerPage() {
    const [view, setView] = useState('cards');
    const { id } = useParams();
    const client = useQueryClient();
    const [note, setNote] = useState('');
    const [exporting, setExporting] = useState(false);
    const [exportError, setExportError] = useState<Error | null>(null);
    const query = useQuery({ queryKey: ['answer', id], queryFn: ({ signal }) => api<Answer>('answers/' + id + '/', 'GET', undefined, signal) });
    const save = useMutation({ mutationFn: (remove: boolean) => api<{
            saved: boolean;
        }>('answers/' + id + '/save/', remove ? 'DELETE' : 'PUT'), onSuccess: result => {
            client.setQueryData<Answer>(['answer', id], old => old && ({ ...old, saved: result.saved }));
            void client.invalidateQueries({ queryKey: ['saved-answers'] });
            setNote(result.saved ? 'Answer saved. Find it in Saved answers.' : 'Answer removed from Saved answers.');
        } });
    const answer = query.data;
    if (!answer)
        return <Page title="Answer details"><Problem error={query.error}/>{query.isPending && <p role="status">Loading answer…</p>}</Page>;
    async function copy() {
        try {
            const result = await fetch('/api/answers/' + id + '/export/md/');
            if (!result.ok)
                throw new Error();
            await navigator.clipboard.writeText(await result.text());
            setNote('Answer copied as Markdown.');
        }
        catch {
            setNote('Clipboard unavailable. Download Markdown to copy the answer.');
        }
    }
    return <Page title={answer.question} eyebrow="ANSWER & EVIDENCE"><Link className="back-link" to={'/thread/' + answer.conversation}><ArrowLeft size={16}/>Conversation</Link><div className="answer-meta"><span>{date(answer.created)}</span><span>PubMed abstracts & metadata</span></div>
    <div className="answer-actions"><div className="toolbar"><button className={answer.saved ? 'saved-button' : 'primary'} disabled={save.isPending || answer.saved} onClick={() => save.mutate(false)}>{answer.saved ? <Check size={16}/> : <Bookmark size={16}/>} {save.isPending ? 'Saving…' : answer.saved ? 'Saved' : 'Save answer'}</button>{answer.saved && <button disabled={save.isPending} onClick={() => save.mutate(true)}>Unsave answer</button>}<button onClick={() => void copy()}>Copy answer</button></div><details className="export-menu"><summary><Download size={16}/>Export</summary><div className="export-options">{Object.entries({ md: 'Markdown', pdf: 'PDF', bib: 'BibTeX', csv: 'CSV' }).map(([kind, label]) => <button disabled={exporting} key={kind} onClick={async () => { setExporting(true); setExportError(null); try {
        await downloadAnswer(answer.id, kind);
        setNote(label + ' export downloaded.');
    }
    catch (error) {
        setExportError(error as Error);
    }
    finally {
        setExporting(false);
    } }}>{label}</button>)}</div></details></div>
    {note && <p className="notice success" role="status">{note}</p>}<Problem error={save.error || exportError}/>
    <div className="panel synthesis-panel"><div className="section-top"><h2>Evidence synthesis</h2><FileText size={20}/></div><Synthesis answer={answer} quotes/></div>
    <div className="section-top"><h2>Retrieved publications <span className="count">{answer.sources.length}</span></h2><div className="view-toggle"><button aria-pressed={view === 'cards'} onClick={() => setView('cards')}>Cards</button><button aria-pressed={view === 'table'} onClick={() => setView('table')}>Evidence table</button></div></div>
    {view === 'table' && !!answer.sources.length && <div className="table-wrap" tabIndex={0} role="region" aria-label="Evidence table; scroll horizontally on small screens"><table><thead><tr>{['Study', 'Year', 'Study type', 'Relevant findings', 'Limitations', 'Source'].map(x => <th scope="col" key={x}>{x}</th>)}</tr></thead><tbody>{answer.sources.map(article => <tr key={article.pmid}><td>{article.title}</td><td>{article.year ?? 'Unavailable'}</td><td>{article.types.join(', ') || 'Unavailable'}</td><td>{answer.result.sections?.filter(s => s.citations.some(c => c.pmid === article.pmid)).map(s => s.text).join(' ') || 'Unavailable: not synthesized'}</td><td>Unavailable: not independently extracted</td><td><a href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a></td></tr>)}</tbody></table></div>}
    <div hidden={view === 'table' && !!answer.sources.length}>
    {answer.sources.length === 0 ? <div className="empty">No publications available. Review the query mapping below, then try another search.</div> : <div className="evidence-grid">{answer.sources.map((article, index) => {
                const relevant = answer.result.sections?.filter(s => s.citations.some(c => c.pmid === article.pmid)) || [];
                return <article className="panel evidence-card" key={article.pmid}><div className="publication-meta"><span className="source-number">{String(index + 1).padStart(2, '0')}</span><span>{article.journal} · {article.year ?? 'Year unavailable'}</span></div><h3>{article.title}</h3><div className="tags">{article.types.map(t => <span key={t}>{t}</span>)}</div><dl className="evidence-facts"><dt>Relevant findings</dt><dd>{relevant.length ? relevant.map(s => s.text).join(' ') : 'Not synthesized. Review the source abstract.'}</dd><dt>Limitations</dt><dd>Not independently extracted. Review the study population, design, and available abstract.</dd></dl><details><summary>Abstract & publication details</summary><Metadata article={article}/></details><a className="source-link" href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a></article>;
            })}</div>}</div>
    <details className="panel provenance"><summary>Retrieval provenance</summary><dl><dt>Research intent</dt><dd>{answer.provenance.intent || 'Unavailable'}</dd><dt>Pipeline</dt><dd>{answer.provenance.pipeline_version || 'Legacy snapshot'}</dd></dl>{answer.provenance.normalization && <><p><strong>Original question:</strong> {answer.provenance.normalization.original}</p><p><strong>Query mapping:</strong> {answer.provenance.normalization.method}</p><p><strong>Search terms:</strong> {answer.provenance.normalization.normalized || 'No reliable mapping'}</p>{answer.provenance.normalization.notice && <p className="notice">{answer.provenance.normalization.notice}</p>}</>}<ul>{answer.provenance.searches?.map(x => <li key={x.query}><code>{x.query}</code><span> · {x.pmids.length} PMIDs</span></li>)}</ul></details>
  </Page>;
}
