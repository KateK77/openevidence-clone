import { afterEach, expect, it, vi } from 'vitest';
import { cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { SaveForm } from './ui';
afterEach(cleanup);
it('disables duplicates, confirms success, and re-enables on edits', async () => {
    const submit = vi.fn().mockResolvedValue({});
    render(<SaveForm initial={{ name: 'Before' }} label="Save profile" submit={submit}><label>Name<input name="name" defaultValue="Before"/></label></SaveForm>);
    expect((screen.getByRole('button') as HTMLButtonElement).disabled).toBe(true);
    fireEvent.change(screen.getByLabelText('Name'), { target: { value: 'After' } });
    fireEvent.click(screen.getByRole('button', { name: 'Save profile' }));
    await screen.findByText('Changes saved successfully.');
    expect((screen.getByRole('button', { name: 'Saved' }) as HTMLButtonElement).disabled).toBe(true);
    fireEvent.click(screen.getByRole('button', { name: 'Saved' }));
    expect(submit).toHaveBeenCalledTimes(1);
    fireEvent.change(screen.getByLabelText('Name'), { target: { value: 'Next' } });
    expect((screen.getByRole('button') as HTMLButtonElement).disabled).toBe(false);
});
it('keeps edits and permits retry after a failed save', async () => {
    const submit = vi.fn().mockRejectedValue(new Error('Synthetic save failure'));
    render(<SaveForm initial={{ name: '' }} label="Save" submit={submit}><label>Name<input name="name"/></label></SaveForm>);
    fireEvent.change(screen.getByLabelText('Name'), { target: { value: 'Keep this' } });
    fireEvent.click(screen.getByRole('button', { name: 'Save' }));
    await screen.findByRole('alert');
    expect((screen.getByLabelText('Name') as HTMLInputElement).value).toBe('Keep this');
    await waitFor(() => expect((screen.getByRole('button') as HTMLButtonElement).disabled).toBe(false));
});
