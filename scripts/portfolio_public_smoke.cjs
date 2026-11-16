// Real HTTPS UI verification. No intercepted responses or native CUA calls.
const { chromium, expect } = require('../frontend/node_modules/@playwright/test');
const fs = require('node:fs');
const path = require('node:path');
const base = process.argv[2];
if (base !== 'https://medevidence-ai-v3.onrender.com') throw Error('Explicit portfolio origin required');
const root = path.resolve(__dirname, '..');
const stamp = new Date().toISOString().replace(/[:.]/g, '-');
const out = path.join(root, 'experiments/portfolio-release', 'public-' + stamp);
const shots = path.join(root, 'docs/screenshots');
fs.mkdirSync(out, { recursive: true }); fs.mkdirSync(shots, { recursive: true });
const report = { site: base, started_at: new Date().toISOString(), method: 'Playwright UI + labelled API assertions; real PubMed and configured Gemini; NOT native CUA', automatic_retries: 0, checks: [], screenshots: [] };
const save = () => fs.writeFileSync(path.join(out, 'results.json'), JSON.stringify(report, null, 2) + '\n');
let browser, page, context, answer, answerURL, threadURL;
const errors = [];
async function check(id, difficulty, expected, fn, ready = true) {
  const row = { id, difficulty, expected, result: ready ? 'RUNNING' : 'NOT_RUN' };
  report.checks.push(row); save();
  if (!ready) { row.reason = 'Required earlier workflow did not complete'; save(); return; }
  try { row.observed = await fn() || 'Expected behavior observed'; row.result = 'PASS'; }
  catch (e) { row.result = 'FAIL'; row.observed = e.message.slice(0, 1800); if (page) await page.screenshot({ path: path.join(out, id + '-failure.png') }).catch(() => {}); }
  save(); console.log(row.result + ' ' + id + ': ' + row.expected);
}
async function shot(name, locator) {
  const file = path.join(shots, name + '.png');
  if (locator) await locator.screenshot({ path: file }); else await page.screenshot({ path: file });
  // Keep immutable run evidence in addition to the selected README images.
  fs.copyFileSync(file, path.join(out, name + '.png'));
  report.screenshots.push({ path: 'docs/screenshots/' + name + '.png', url: page.url(), captured_at: new Date().toISOString() }); save();
}
async function login(p, name) {
  await p.goto(base + '/profile');
  await p.getByLabel('Username', { exact: true }).fill(name);
  await p.getByLabel('Password', { exact: true }).fill('MedEvidence-Demo-2026!');
  await p.getByRole('button', { name: 'Sign in', exact: true }).click();
  await expect(p.locator('.account')).toContainText(name);
}
(async () => {
  browser = await chromium.launch({ headless: true });
  context = await browser.newContext({ viewport: { width: 1440, height: 1050 }, acceptDownloads: true });
  page = await context.newPage(); page.setDefaultTimeout(30000); page.on('pageerror', e => errors.push(e.message));
  await check('P01', 'Easy', 'HTTPS health confirms PostgreSQL and public demo mode', async () => {
    const h = await (await page.request.get(base + '/api/health/', { timeout: 120000 })).json();
    if (h.database !== 'postgresql') throw Error(JSON.stringify(h));
    const s = await (await page.request.get(base + '/api/session/')).json();
    if (!s.public_demo) throw Error('Public demo flag absent');
    report.model_configured = s.generation_configured; report.model = s.model;
    return h;
  });
  await check('P02', 'Easy', 'Published researcher credentials log in and survive reload', async () => {
    await login(page, 'portfolio_researcher'); await page.reload(); await expect(page.locator('.account')).toContainText('portfolio_researcher');
    await expect(page.getByRole('heading', { name: /Better questions/ })).toBeVisible(); await shot('01-dashboard');
  });
  await check('P03', 'Medium', 'Shared profile changes are forbidden in UI and API', async () => {
    await page.goto(base + '/profile'); await expect(page.getByText(/Shared demo profiles and credentials are protected/)).toBeVisible();
    const s = await (await page.request.get(base + '/api/session/')).json();
    const r = await page.request.patch(base + '/api/profile/', { headers: { 'X-CSRFToken': s.csrf }, data: { first_name: 'Forbidden change' } });
    if (r.status() !== 403) throw Error('Expected 403, received ' + r.status()); return { status: r.status() };
  });
  await check('P04', 'Medium', 'Real PubMed PMID search resolves metadata, abstract and DOI', async () => {
    await page.goto(base + '/library'); await page.getByLabel('Keywords, PMID or DOI').fill('33567185');
    await page.getByRole('button', { name: 'Search PubMed', exact: true }).click();
    await expect(page.getByText('Once-Weekly Semaglutide in Adults with Overweight or Obesity.', { exact: true })).toBeVisible({ timeout: 120000 });
    await shot('02-literature-search');
    await page.getByText('Abstract & publication details', { exact: true }).click();
    await expect(page.getByText('Electronic publication', { exact: true })).toBeVisible();
    await expect(page.getByText('Journal issue', { exact: true })).toBeVisible();
    await expect(page.locator('.abstract')).toContainText('1961');
    await expect(page.getByRole('link', { name: /10.1056\/NEJMoa2032183/ })).toHaveAttribute('href', /doi.org/);
    await shot('04-source-citation', page.locator('.publication').first());
  });
  await check('P05', 'Medium', 'Save publication confirms success and persists after reload', async () => {
    const b = page.getByRole('button', { name: 'Save publication', exact: true });
    if (await b.count()) await b.click();
    await expect(page.getByRole('button', { name: 'Saved', exact: true })).toBeDisabled();
    await page.goto(base + '/publications'); await page.reload(); await expect(page.getByText(/Once-Weekly Semaglutide/, { exact: false })).toBeVisible();
  });
  await check('P06', 'Medium', 'Collection edit and filter persist without duplicating records', async () => {
    const collection = (await page.getByLabel('Collection', { exact: true }).inputValue()) === 'Metabolic health' ? 'Metabolic evidence' : 'Metabolic health'; await page.getByLabel('Collection', { exact: true }).fill(collection);
    const b = page.getByRole('button', { name: 'Update collection', exact: true }); if (await b.isEnabled()) await b.click();
    await expect(page.getByText('Changes saved successfully.')).toBeVisible();
    await page.reload(); await expect(page.getByLabel('Collection', { exact: true })).toHaveValue(collection);
    await page.getByLabel('Search saved publications').fill(collection); await expect(page.locator('.publication')).toHaveCount(1); await shot('05-saved-publications');
    await page.getByLabel('Search saved publications').fill('no_match_984032'); await expect(page.getByText('No saved publications found')).toBeVisible();
  });
  await check('P07', 'Medium', 'Saved PMID search can be saved and restored', async () => {
    await page.goto(base + '/library'); await page.getByLabel('Keywords, PMID or DOI').fill('33567185'); await page.getByRole('button', { name: 'Search PubMed', exact: true }).click();
    await expect(page.getByText(/Once-Weekly Semaglutide/)).toBeVisible({ timeout: 120000 });
    const saveSearch = page.getByRole('button', { name: 'Save this search', exact: true }); if (await saveSearch.count()) await saveSearch.click(); await expect(page.getByRole('button', { name: 'Search saved', exact: true })).toBeDisabled(); await page.reload();
    await page.locator('.saved-searches summary').click(); await page.locator('.saved-search-row').getByRole('button').first().click();
    await expect(page.getByLabel('Keywords, PMID or DOI')).toHaveValue('33567185');
  });
  await check('P08', 'Hard', 'GLP-1 question creates a real literature-backed conversation', async () => {
    await page.goto(base); await expect(page.locator('.account')).toContainText('portfolio_researcher'); await page.getByLabel('Research question', { exact: true }).fill('What is the evidence for GLP-1 receptor agonists in obesity treatment?');
    await page.getByRole('button', { name: /^(Ask AI|Search literature)$/ }).click();
    await expect(page).toHaveURL(/thread\/\d+$/, { timeout: 180000 }); threadURL = page.url();
    await page.getByRole('link', { name: 'View answer and evidence' }).first().click(); await expect(page).toHaveURL(/answer\/\d+$/); answerURL = page.url();
    answer = await (await page.request.get(base + '/api/answers/' + answerURL.split('/').pop() + '/')).json();
    fs.writeFileSync(path.join(out, 'answer.json'), JSON.stringify(answer, null, 2));
    if (!answer.sources?.length) throw Error('No live publications returned'); await shot('03-evidence-synthesis', page.locator('.synthesis-panel'));
    return { answer_id: answer.id, conversation: answer.conversation, status: answer.status, source_count: answer.sources.length };
  });
  await check('P09', 'Hard', 'AI synthesis completes with exact source quotations and automated claim checks', async () => {
    if (answer.status !== 'complete') throw Error('Actual status: ' + answer.status + '. ' + answer.result.message);
    const cited = answer.result.sections.filter(x => x.citations?.length);
    if (!cited.length) throw Error('No source-linked claims');
    for (const s of cited) for (const c of s.citations) {
      const src = answer.sources.find(x => x.pmid === c.pmid);
      const norm = s => s.replace(/\s+/g, ' ').trim();
      if (!src || !norm(src.abstract).includes(norm(c.quote))) throw Error('Citation does not match snapshot');
      if (s.verification !== 'automated_checks_passed') throw Error('Claim checks absent');
    }
    const details = page.locator('.citation details');
    for (let i = 0; i < Math.min(await details.count(), 2); i++) await details.nth(i).locator('summary').click();
    await shot('07-citations', page.locator('.synthesis-panel'));
    return { source_linked_sections: cited.length, status: answer.status };
  }, !!answer);
  await check('P10', 'Medium', 'Answer bookmark persists and appears in Saved answers', async () => {
    await page.getByRole('button', { name: 'Save answer', exact: true }).click(); await expect(page.getByRole('button', { name: 'Saved', exact: true })).toBeDisabled();
    await page.reload(); await expect(page.getByRole('button', { name: 'Saved', exact: true })).toBeDisabled();
    await page.goto(base + '/saved'); await expect(page.getByRole('link', { name: /What is the evidence for GLP-1/ })).toBeVisible();
  }, !!answer);
  await check('P11', 'Medium', 'Markdown, PDF, BibTeX and CSV downloads are nonempty and correctly encoded', async () => {
    await page.goto(answerURL); await page.locator('.export-menu summary').click();
    for (const kind of ['Markdown', 'PDF', 'BibTeX', 'CSV']) {
      const pending = page.waitForEvent('download'); await page.getByRole('button', { name: kind, exact: true }).click();
      const d = await pending; const dest = path.join(out, d.suggestedFilename()); await d.saveAs(dest);
      const bytes = fs.readFileSync(dest); if (bytes.length < 100) throw Error('Empty export: ' + kind);
      if (kind === 'PDF' && !bytes.subarray(0, 4).equals(Buffer.from('%PDF'))) throw Error('Invalid PDF');
      if (kind === 'Markdown' && (!bytes.toString('utf8').includes('—') || bytes.toString('utf8').includes('â€'))) throw Error('Broken Unicode');
    }
  }, !!answer);
  await check('P12', 'Hard', 'Follow-up stays in the conversation and PubMed queries retain GLP-1 context', async () => {
    await page.goto(threadURL); await page.getByLabel('Follow-up question', { exact: true }).fill('What are the limitations of these studies?');
    await page.getByRole('button', { name: /^(Ask AI|Search literature)$/ }).click();
    await expect(page.getByRole('link', { name: 'View answer and evidence' })).toHaveCount(2, { timeout: 180000 });
    await page.getByRole('link', { name: 'View answer and evidence' }).last().click();
    const a = await (await page.request.get(base + '/api/answers/' + page.url().split('/').pop() + '/')).json();
    fs.writeFileSync(path.join(out, 'follow-up.json'), JSON.stringify(a, null, 2));
    if (a.conversation !== answer.conversation || a.provenance.intent !== 'limitations' || !a.provenance.searches.some(x => /glp-1.*obesity/i.test(x.query))) throw Error('Context not retained');
    return { conversation: a.conversation, status: a.status, queries: a.provenance.searches.map(x => x.query) };
  }, !!answer);
  await check('P13', 'Medium', 'Conversation rename and history search persist', async () => {
    await page.goto(threadURL); await page.getByRole('button', { name: 'Rename', exact: true }).click(); await page.getByLabel('Conversation title').fill('Portfolio · GLP-1 evidence review');
    await page.getByRole('button', { name: 'Save title', exact: true }).click(); await expect(page.getByText('Changes saved successfully.')).toBeVisible();
    await page.goto(base + '/history'); await page.getByLabel('Search history').fill('GLP-1'); await page.getByRole('button', { name: 'Search', exact: true }).click();
    await expect(page.getByRole('link', { name: /Portfolio · GLP-1/ })).toBeVisible(); await shot('06-conversation-history');
  }, !!answer);
  await check('P14', 'Medium', 'Preferences save and survive page reload', async () => {
    await page.goto(base + '/settings'); await page.getByLabel('Display density').selectOption('Compact'); await page.getByRole('button', { name: 'Save preferences', exact: true }).click();
    await expect(page.getByText('Changes saved successfully.')).toBeVisible(); await page.reload(); await expect(page.getByLabel('Display density')).toHaveValue('Compact');
    await page.getByLabel('Display density').selectOption('Comfortable'); await page.getByRole('button', { name: 'Save preferences', exact: true }).click(); await expect(page.getByText('Changes saved successfully.')).toBeVisible();
  });
  await check('P15', 'Hard', 'Published reader credentials work; another account cannot access the researcher answer', async () => {
    const c = await browser.newContext(); const p = await c.newPage(); p.setDefaultTimeout(30000);
    try { await login(p, 'portfolio_reader'); const r = await p.request.get(base + '/api/answers/' + answer.id + '/'); if (r.status() !== 404) throw Error('Cross-account access was not denied'); return { status: r.status() }; } finally { await c.close(); }
  }, !!answer);
  await check('P16', 'Medium', 'Mobile dashboard and evidence table have no page overflow; drawer can close', async () => {
    await page.setViewportSize({ width: 390, height: 844 }); await page.goto(base); await expect(page.locator('.account')).toContainText('portfolio_researcher'); await expect(page.locator('.mode-banner')).toBeVisible(); await expect(page.getByRole('heading', { name: /Better questions/ })).toBeVisible();
    if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error('Dashboard horizontal overflow'); await shot('08-mobile-dashboard');
    await page.getByRole('button', { name: 'Open menu' }).click(); await page.getByRole('button', { name: 'Close menu', exact: true }).click();
    if (!answerURL) throw Error('Evidence-table prerequisite missing'); { await page.goto(answerURL); await page.getByRole('button', { name: 'Evidence table', exact: true }).click(); await expect(page.getByRole('table')).toBeVisible(); if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error('Evidence table page overflow'); }
  });
  await check('P17', 'Easy', 'Sign out removes access to the protected answer', async () => {
    await page.setViewportSize({ width: 1440, height: 1050 }); await page.goto(base + '/profile'); await page.getByRole('button', { name: 'Sign out', exact: true }).click();
    await expect(page.getByRole('heading', { name: 'Welcome back' })).toBeVisible(); if (!answerURL) throw Error('Protected-answer prerequisite missing'); { await page.goto(answerURL); await expect(page.getByRole('link', { name: 'Sign in or register' })).toBeVisible(); }
  });
  await check('P18', 'Easy', 'No uncaught browser exceptions during the run', async () => { if (errors.length) throw Error(errors.join('; ')); return { exceptions: 0 }; });
})().catch(e => { report.fatal = e.message; process.exitCode = 1; }).finally(async () => {
  report.finished_at = new Date().toISOString(); report.counts = Object.fromEntries(['PASS', 'FAIL', 'NOT_RUN'].map(s => [s, report.checks.filter(x => x.result === s).length])); save(); console.log(JSON.stringify({ report: path.relative(root, out), counts: report.counts })); if (browser) await browser.close();
});
