export type User = {
    username: string;
    first_name: string;
    last_name: string;
};
export type Session = {
    user: User | null;
    csrf: string;
    model?: string;
    generation_configured?: boolean;
};
export type Article = {
    pmid: string;
    title: string;
    authors: string[];
    journal: string;
    date: string;
    year: number | null;
    electronic_date?: string;
    issue_date?: string;
    date_type?: string;
    abstract: string;
    types: string[];
    doi: string;
    url: string;
    collection?: string;
};
export type Section = {
    text: string;
    status: string;
    citations: {
        pmid: string;
        quote: string;
    }[];
};
export type Answer = {
    id: number;
    conversation: number;
    question: string;
    created: string;
    status: string;
    model: string;
    saved: boolean;
    sources: Article[];
    result: {
        message?: string;
        sections?: Section[];
    };
    provenance: {
        intent?: string;
        pipeline_version?: string;
        retrieved_at?: string;
        normalization?: {
            original: string;
            normalized: string;
            method: string;
            notice: string;
        };
        searches?: {
            query: string;
            pmids: string[];
        }[];
    };
};
export type Thread = {
    id: number;
    title: string;
    updated: string;
    turns?: Answer[];
};
export type Preferences = {
    language: string;
    detail: string;
    display: string;
};
export type SavedSearch = {
    id: number;
    filters: Record<string, string | number | boolean>;
};
let token = '';
let authRevision = 0;
export function invalidateAuthRequests() { authRevision++; }
export async function api<T>(path: string, method = 'GET', body?: unknown, signal?: AbortSignal): Promise<T> {
    const revision = authRevision;
    const response = await fetch('/api/' + path, { method, signal, credentials: 'same-origin', headers: { Accept: 'application/json', 'Content-Type': 'application/json', 'X-CSRFToken': token }, body: body === undefined ? undefined : JSON.stringify(body) });
    const data = await response.json().catch(() => null);
    if (revision !== authRevision)
        throw new Error('The account session changed. Please repeat this action in the current account.');
    if (response.status === 204)
        return undefined as T;
    if (!response.ok) {
        const message = data?.detail || (data && Object.entries(data).map(([k, v]) => k + ': ' + String(v)).join(' '));
        if (response.status === 403 && path !== 'session/')
            window.dispatchEvent(new Event('session-check'));
        throw new Error(message || (response.status >= 500 ? 'The server could not complete this request. Please try again.' : 'Request failed (' + response.status + ').'));
    }
    if (data?.csrf)
        token = data.csrf;
    return data;
}
export function announceSession() { localStorage.setItem('medevidence-auth-event', String(Date.now())); }
export function date(value: string) {
    const parsed = new Date(value);
    return Number.isNaN(parsed.getTime()) ? 'Date unavailable' : new Intl.DateTimeFormat('en', { dateStyle: 'medium' }).format(parsed);
}
export async function downloadAnswer(id: number, kind: string) {
    const response = await fetch('/api/answers/' + id + '/export/' + kind + '/', { credentials: 'same-origin' });
    if (!response.ok)
        throw new Error('Export unavailable. Check your session and try again.');
    const url = URL.createObjectURL(await response.blob());
    const link = document.createElement('a');
    link.href = url;
    link.download = 'medevidence-' + id + '.' + kind;
    link.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
}
