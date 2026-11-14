import { useState, type ReactNode, type FormEvent } from 'react';
import { Check, LoaderCircle } from 'lucide-react';
export function Problem({ error }: {
    error?: Error | null;
}) {
    return error ? <div role="alert" className="notice error">{error.message}</div> : null;
}
export function Page({ title, children, eyebrow = 'RESEARCH WORKSPACE' }: {
    title: string;
    children?: ReactNode;
    eyebrow?: string;
}) {
    return <section className="page"><p className="eyebrow">{eyebrow}</p><h1>{title}</h1>{children}</section>;
}
export function fields(event: FormEvent<HTMLFormElement>) { event.preventDefault(); return Object.fromEntries(new FormData(event.currentTarget)); }
export function SaveButton({ busy, saved, disabled, label = 'Save' }: {
    busy: boolean;
    saved?: boolean;
    disabled?: boolean;
    label?: string;
}) {
    return <button className={saved ? 'saved-button' : 'primary'} disabled={busy || saved || disabled}>{busy ? <LoaderCircle className="spin" size={16}/> : saved ? <Check size={16}/> : null}{busy ? 'Saving…' : saved ? 'Saved' : label}</button>;
}
export function SaveForm({ initial, submit, label, children }: {
    initial: Record<string, string>;
    submit: (data: Record<string, FormDataEntryValue>) => Promise<unknown>;
    label: string;
    children: ReactNode;
}) {
    const [baseline, setBaseline] = useState(initial);
    const [dirty, setDirty] = useState(false);
    const [busy, setBusy] = useState(false);
    const [saved, setSaved] = useState(false);
    const [error, setError] = useState<Error | null>(null);
    return <form className="fields save-form" onChange={e => {
            const values = Object.fromEntries(new FormData(e.currentTarget));
            setDirty(Object.keys(baseline).some(k => String(values[k] ?? '') !== baseline[k]));
            setSaved(false);
            setError(null);
        }} onSubmit={async (e) => {
            const data = fields(e);
            if (busy || !dirty)
                return;
            setBusy(true);
            setError(null);
            try {
                await submit(data);
                setBaseline(Object.fromEntries(Object.entries(data).map(([k, v]) => [k, String(v)])));
                setDirty(false);
                setSaved(true);
            }
            catch (error) {
                setError(error instanceof Error ? error : new Error('Could not save. Please try again.'));
            }
            finally {
                setBusy(false);
            }
        }}><fieldset disabled={busy}>{children}</fieldset><div className="save-row"><SaveButton busy={busy} saved={saved} disabled={!dirty} label={label}/><span role="status">{saved ? 'Changes saved successfully.' : dirty ? 'Unsaved changes' : 'No unsaved changes'}</span></div><Problem error={error}/></form>;
}
