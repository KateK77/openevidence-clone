import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Link } from 'react-router-dom';
import { BookOpen, CheckCircle2, Settings2 } from 'lucide-react';
import { api, type Session, type Preferences, type SynthesisCapability } from './api';
import { Problem } from './ui';

export function useResearchMode() {
    const session = useQuery({ queryKey: ['session'], queryFn: ({ signal }) => api<Session>('session/', 'GET', undefined, signal) });
    const preferences = useQuery({ queryKey: ['preferences'], queryFn: ({ signal }) => api<Preferences>('settings/', 'GET', undefined, signal), enabled: !!session.data?.user });
    return { session: session.data, preferences: preferences.data,
        configured: session.data?.generation_configured, chinese: preferences.data?.language === 'Chinese' };
}

export function ModeNotice({ settings = false }: { settings?: boolean }) {
    const { session, configured, chinese, preferences } = useResearchMode();
    if (configured === undefined) return null;
    return <div className={'mode-banner ' + (configured ? 'configured' : 'limited')}>
        {configured ? <CheckCircle2 size={19}/> : <BookOpen size={19}/>}
        <div><strong>{configured ? (chinese ? 'AI 综合回答已配置' : 'AI synthesis configured') : (chinese ? '当前仅文献检索 · 尚无中文 AI 回答' : 'Literature search only · AI answers unavailable')}</strong>
        <p>{configured
            ? (chinese ? '新回答将按中文偏好生成，并经过来源与结论检查。原始文献与引文保留原文；模型已配置不代表每次请求都能成功。' : `New AI answers use your saved ${preferences?.language || 'English'} preference and undergo source and claim checks. Configuration does not guarantee a successful request.`)
            : (chinese ? '中文偏好可以保存，但模型连接完成前不会生成中文医学回答，也不会翻译文献摘要。下方状态说明不是 AI 回答。' : 'Language and detail preferences are saved for future AI answers. Until a model is connected, results contain source publications only, without a generated answer or translated abstracts.')}</p>
        {session?.synthesis?.state === 'error' && <p className="error-text">{session.synthesis.check?.message}</p>}
        {!settings && <Link to="/settings"><Settings2 size={14}/>{chinese ? '查看模型状态与语言设置' : 'Model status & language settings'}</Link>}
        </div>
    </div>;
}

export function ModelConnection() {
    const { session } = useResearchMode();
    const client = useQueryClient();
    const check = useMutation({ mutationFn: () => api<SynthesisCapability>('synthesis/', 'POST', {}), onSuccess: result => {
        client.setQueryData<Session>(['session'], old => old && ({ ...old, synthesis: result, generation_configured: result.configured, model: result.model }));
    } });
    const status = session?.synthesis;
    const state = status?.state || (session?.generation_configured ? 'unchecked' : 'unconfigured');
    const labels = { unconfigured: 'Setup required', unchecked: 'Configured · not checked', ready: 'Connection check passed', error: 'Connection check failed' };
    return <section className="panel account-panel connection-panel"><h2>AI connection</h2><span className="pill">{labels[state]}</span>
        <p>{status?.model ? `Server model: ${status.model}` : 'Connect your Gemini model to generate research answers, including Chinese.'}</p>
        <p className="muted">This check sends one short, nonmedical prompt to the configured service and checks JSON and Chinese output. It uses your provider quota. It does not validate medical answer quality.</p>
        <button disabled={!session?.generation_configured || check.isPending} onClick={() => check.mutate()}>{check.isPending ? 'Checking connection…' : 'Check AI connection'}</button>
        <Problem error={check.error}/>
        {status?.check && <div className={'notice ' + (state === 'ready' ? 'success' : 'error')} role="status"><p>{status.check.message}</p><small>Checked {new Date(status.check.checked_at).toLocaleString()} · Check expires after 10 minutes; changing model configuration requires a new check.</small></div>}
        <details className="setup-guide"><summary>Server setup guide · Gemini free tier</summary>
            <ol><li>Open <a href="https://aistudio.google.com/api-keys" target="_blank" rel="noreferrer">Google AI Studio</a> and obtain a key for a Free Tier project. Verify the model is available within your project quota.</li>
            <li>In the project folder, run <code>.\configure-model.ps1</code>. Enter the key in the terminal's hidden prompt. It is stored only in the ignored server environment file.</li>
            <li>Restart with <code>.\stop.ps1</code>, then <code>.\start.ps1</code>. Reload this page and check the connection.</li>
            <li>Choose Chinese, save preferences, then ask a new question or use Generate new answer on an existing result.</li></ol>
            <p>Never paste credentials into this website or commit them. This application cannot verify your project's billing tier and never enables billing. Free quotas are shared across testers; synthesis plus claim review normally uses two model calls. A language retry can add one more.</p>
            <p><a href="https://ai.google.dev/gemini-api/docs/pricing" target="_blank" rel="noreferrer">Provider pricing and data-use terms</a> · Use public research questions only.</p>
        </details>
    </section>;
}
