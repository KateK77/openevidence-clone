import { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { Check, ArrowLeft, Download, Bookmark, FileText } from 'lucide-react';
import { api, date, downloadAnswer, type Answer, type Thread, type Article } from './api';
import { Composer, useAsk } from './app';
import { Page, Problem, SaveForm } from './ui';
import { ModeNotice, useResearchMode } from './synthesis-mode';
export function Conversation() {
    const { configured } = useResearchMode();
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
      <div className="followup"><h2>Continue this research</h2><p className="muted">Ask about limitations, compare findings, or explore a related question.</p><ModeNotice/><Composer question={question} change={change} busy={ask.isPending} configured={configured} follow submit={() => ask.mutate({ question, conversation: Number(id) }, { onSuccess: () => change('') })}/>{ask.isPending && <p role="status">{configured ? 'Retrieving evidence, generating and checking claims…' : 'Retrieving source publications…'}</p>}</div>
    </>}
  </Page>;
}
const statuses: Record<string, string> = { complete: 'Synthesis complete', retrieval_only: 'Literature only', retrieval_error: 'Retrieval unavailable', generation_error: 'Generation unavailable', insufficient: 'Evidence gap', demo: 'Synthetic demo' };
function Synthesis({ answer, quotes }: {
    answer: Answer;
    quotes?: boolean;
}) {
    const chinese = (answer.result.language || answer.provenance.generation_preferences?.language) === 'Chinese';
    return <div className="synthesis"><div className="toolbar"><span className={'pill ' + (answer.status === 'complete' ? 'complete' : '')}>{statuses[answer.status] || answer.status}</span>{answer.model && <small>Model: {answer.model}</small>}<small>{answer.sources.length} PubMed records</small></div>
    {answer.result.language && <p className="answer-language">{answer.result.sections?.length ? 'Generated answer language' : 'Requested answer language'}: {answer.result.language}{answer.result.language_check === 'passed' ? ' · Chinese prose check passed' : ''}</p>}
    {answer.provenance.revision_of && <p className="scope-note">New generation from <Link to={'/answer/' + answer.provenance.revision_of}>answer #{answer.provenance.revision_of}</Link> using the same source snapshot. Literature was not searched again.</p>}
    {answer.result.message && <p className="synthesis-message">{answer.result.message}</p>}
    {answer.result.sections?.map((section, i) => <div className={'finding ' + section.status} key={i}><strong>{section.status === 'insufficient' ? (chinese ? '证据不足' : 'Evidence gap') : section.kind === 'limitation' ? (chinese ? '研究局限' : 'Study limitation') : section.status === 'tentative' ? (chinese ? '初步解释' : 'Tentative interpretation') : (chinese ? '有来源的研究发现' : 'Source-linked finding')}</strong><p lang={chinese ? 'zh-CN' : undefined}>{section.text}</p>{section.verification === 'automated_checks_passed' && <small className="verification-label">{chinese ? '已通过自动来源与结论检查 · 非临床验证' : 'Automated source & claim checks passed · not clinical validation'}</small>}{section.citations.map((citation, j) => <div className="citation" key={j}><a href={'https://pubmed.ncbi.nlm.nih.gov/' + citation.pmid + '/'} target="_blank" rel="noreferrer">PMID {citation.pmid} ↗</a>{quotes && <details><summary>{chinese ? '查看支持原文（保留来源语言）' : 'Supporting excerpt · original language'}</summary><blockquote>{citation.quote}</blockquote></details>}</div>)}</div>)}
    {quotes && !!answer.result.sections?.length && <p className="scope-note">{answer.result.verification ? 'Source IDs, exact quotations and numerical consistency were checked. A separate model pass reviewed claim support. Automated review can miss errors and is not independent clinical validation.' : 'Legacy answer: source membership and excerpt matching do not establish clinical claim support. This snapshot has no Round 3 claim-review record.'}</p>}
  </div>;
}
export function Metadata({ article }: {
    article: Article;
}) {
    return <div className="metadata"><p>{article.authors.join(', ') || 'Authors unavailable'}</p><dl><dt>Journal</dt><dd>{article.journal || 'Unavailable'}</dd>{article.electronic_date && <><dt>Electronic publication</dt><dd>{article.electronic_date}</dd></>}{article.issue_date && <><dt>Journal issue</dt><dd>{article.issue_date}</dd></>}{!article.electronic_date && !article.issue_date && <><dt>Publication date (type unavailable)</dt><dd>{article.date || 'Unavailable'}</dd></>}<dt>DOI</dt><dd>{article.doi ? <a href={'https://doi.org/' + encodeURIComponent(article.doi)} target="_blank" rel="noreferrer">{article.doi} ↗</a> : 'Unavailable'}</dd></dl><h3>Source abstract</h3><p className="abstract">{article.abstract || 'No abstract is available for this record.'}</p></div>;
}
export function AnswerPage() {
    const { configured, preferences } = useResearchMode();
    const navigate = useNavigate();
    const [view, setView] = useState('cards');
    const { id } = useParams();
    const client = useQueryClient();
    const [note, setNote] = useState('');
    const [exporting, setExporting] = useState(false);
    const [exportError, setExportError] = useState<Error | null>(null);
    const query = useQuery({ queryKey: ['answer', id], queryFn: ({ signal }) => api<Answer>('answers/' + id + '/', 'GET', undefined, signal) });
    const regenerate = useMutation({ mutationFn: () => api<Answer>('answers/' + id + '/regenerate/', 'POST', {}), onSuccess: fresh => {
        client.setQueryData(['answer', String(fresh.id)], fresh);
        void client.invalidateQueries({ queryKey: ['history'] });
        void client.invalidateQueries({ queryKey: ['thread', String(fresh.conversation)] });
        navigate('/answer/' + fresh.id);
    } });
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
    <div className="panel synthesis-panel"><div className="section-top"><h2>Evidence synthesis</h2><FileText size={20}/></div><Synthesis answer={answer} quotes/>
      <div className="regenerate-panel"><ModeNotice/><p>Generate a new answer in <strong>{preferences?.language || 'your saved language'}</strong> with your current preferences. This reuses these abstracts and preserves the original answer.</p><button className="primary" disabled={!configured || regenerate.isPending || !answer.sources.length} onClick={() => regenerate.mutate()}>{regenerate.isPending ? 'Generating and checking…' : 'Generate new answer'}</button><Problem error={regenerate.error}/>{regenerate.isPending && <p role="status">The model is generating a new response and reviewing claim support. Your original answer remains unchanged.</p>}</div>
    </div>
    <div className="section-top"><h2>Retrieved publications <span className="count">{answer.sources.length}</span></h2><div className="view-toggle"><button aria-pressed={view === 'cards'} onClick={() => setView('cards')}>Cards</button><button aria-pressed={view === 'table'} onClick={() => setView('table')}>Evidence table</button></div></div>
    {view === 'table' && !!answer.sources.length && <div className="table-wrap" tabIndex={0} role="region" aria-label="Evidence table; scroll horizontally on small screens"><table><thead><tr>{['Study', 'Year', 'Study type', 'Relevant findings', 'Limitations', 'Source'].map(x => <th scope="col" key={x}>{x}</th>)}</tr></thead><tbody>{answer.sources.map(article => <tr key={article.pmid}><td>{article.title}</td><td>{article.year ?? 'Unavailable'}</td><td>{article.types.join(', ') || 'Unavailable'}</td><td>{answer.result.sections?.filter(s => s.kind !== 'limitation' && s.citations.some(c => c.pmid === article.pmid)).map(s => s.text).join(' ') || 'Unavailable: not synthesized'}</td><td>{answer.result.sections?.filter(s => s.kind === 'limitation' && s.citations.some(c => c.pmid === article.pmid)).map(s => s.text).join(' ') || 'Unavailable: not extracted from the supplied abstracts'}</td><td><a href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a></td></tr>)}</tbody></table></div>}
    <div hidden={view === 'table' && !!answer.sources.length}>
    {answer.sources.length === 0 ? <div className="empty">No publications available. Review the query mapping below, then try another search.</div> : <div className="evidence-grid">{answer.sources.map((article, index) => {
                const relevant = answer.result.sections?.filter(s => s.kind !== 'limitation' && s.citations.some(c => c.pmid === article.pmid)) || [];
                return <article className="panel evidence-card" key={article.pmid}><div className="publication-meta"><span className="source-number">{String(index + 1).padStart(2, '0')}</span><span>{article.journal} · {article.year ?? 'Year unavailable'}</span></div><h3>{article.title}</h3><div className="tags">{article.types.map(t => <span key={t}>{t}</span>)}</div><dl className="evidence-facts"><dt>Relevant findings</dt><dd>{relevant.length ? relevant.map(s => s.text).join(' ') : 'Not synthesized. Review the source abstract.'}</dd><dt>Limitations</dt><dd>{answer.result.sections?.filter(s => s.kind === 'limitation' && s.citations.some(c => c.pmid === article.pmid)).map(s => s.text).join(' ') || 'Not extracted. Review the study population, design, and available abstract.'}</dd></dl><details><summary>Abstract & publication details</summary><Metadata article={article}/></details><a className="source-link" href={article.url} target="_blank" rel="noreferrer">PMID {article.pmid} ↗</a></article>;
            })}</div>}</div>
    <details className="panel provenance"><summary>Retrieval provenance</summary>
      <dl><dt>Research intent</dt><dd>{answer.provenance.intent || 'Unavailable'}</dd><dt>Pipeline</dt><dd>{answer.provenance.pipeline_version || 'Legacy snapshot'}</dd><dt>Retrieved at</dt><dd>{answer.provenance.retrieved_at ? new Date(answer.provenance.retrieved_at).toLocaleString() : 'Unavailable'}</dd></dl>
      {answer.provenance.normalization && <><h3>1. Original question</h3><p>{answer.provenance.normalization.original}</p><h3>2. Normalized question · before conversation context</h3><p>{answer.provenance.normalization.normalized || 'No reliable mapping'}</p><p className="muted">Mapping method: {answer.provenance.normalization.method}. This is preprocessing, not the final PubMed query.</p>{answer.provenance.normalization.notice && <p className="notice">{answer.provenance.normalization.notice}</p>}</>}
      <h3>3. Previous questions available for context</h3>{answer.provenance.previous_questions?.length ? <ol>{answer.provenance.previous_questions.map((question, index) => <li key={index}>{question}</li>)}</ol> : <p>No previous questions recorded.</p>}
      <h3>4. Executed PubMed queries</h3><p className="muted">These are the actual queries after topic selection and any context expansion. Each PMID count is per query; results can overlap.</p>
      {answer.provenance.searches?.length ? <ul>{answer.provenance.searches.map(x => <li key={x.query}><code>{x.query}</code><span> · {x.pmids.length} PMIDs</span></li>)}</ul> : <p>No executed queries recorded.</p>}
    </details>
  </Page>;
}
