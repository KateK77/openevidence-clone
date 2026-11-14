import { afterEach, expect, it, vi } from 'vitest';
import { api, invalidateAuthRequests } from './api';
afterEach(() => vi.unstubAllGlobals());
it('discards a private response that completes after an account boundary', async () => {
    let finish: (value: unknown) => void = () => { };
    vi.stubGlobal('fetch', vi.fn(() => new Promise(resolve => { finish = resolve; })));
    const pending = api('answers/1/');
    invalidateAuthRequests();
    finish({ status: 200, ok: true, json: async () => ({ question: 'Previous account private data' }) });
    await expect(pending).rejects.toThrow('account session changed');
});
