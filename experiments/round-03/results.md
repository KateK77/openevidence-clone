# MedEvidence AI 3.0 — implementation and verification report

Date: November 15, 2026, America/Chicago. Some artifact timestamps are November 16 UTC.
Baseline: `12eb0c0f5792f821ac7d1f587998fd56fec9c755` (`v2.0.0-r2`).
Delivery branch: `v3-round-03`. Release tag: `v3.0.0-r3`.

## Outcome

The new version implements the recorded language, model-setup, answer-revision,
claim-review and provenance changes while retaining the existing research data
and workflows. Local v3 is running at `http://127.0.0.1:5173`, backed by API port
8021. A persistent deployment package is included and locally tested.

**Public test site is live:** https://medevidence-ai-v3.onrender.com

The real public browser acceptance run passed 14 checks. See
[hosting-status.md](hosting-status.md) for the verified deployment and scope.
**Live Gemini Chinese-answer acceptance remains blocked by the missing operator
key.** The current website runs in literature-only mode.

## Changes traced to feedback

| Requirement | Delivered behavior | Evidence and remaining limit |
| --- | --- | --- |
| Chinese selected but no Chinese answer | Explicit literature-only mode; bilingual explanation; Gemini setup and connection check; Chinese prose validation with one retry | Synthetic generation and rejection cases pass. A real Gemini answer still needs a key and manual citation review. |
| Unclear language preference availability | Composer, preferences and connection panel distinguish stored preference from actual capability | Desktop/mobile browser fixtures exercise unconfigured and configured states. |
| Generate an answer after connecting the model | Owner-only new revision reuses stored evidence and current preferences; original answer/bookmark preserved | API and browser fixture checks pass; no live model call was made. |
| More trustworthy evidence synthesis | PMID membership, exact excerpt, numeric guard and automated claim-support review; uncited evidence-gap sections are reviewed too | Unsupported or malformed output is withheld. Same-model review is not independent clinical validation. |
| Confusing provenance labels | Original question, normalized question before context, prior questions and executed queries have distinct labels in UI and exports | Context handling retained; export and browser assertions pass. |
| Keep the site available for other people | Built frontend, Caddy HTTPS recipe, Gunicorn, persistent PostgreSQL and shared Redis | Container integration passes. Public Render HTTPS and Neon deployment verified in the separate 14-check acceptance run. |
| Preserve successful v2 behavior | Save feedback, account isolation, history, exports and short/Chinese queries retained | Live PubMed workflow and regression suites pass within the scopes below. |

## Verification evidence

| Check | Result | Scope |
| --- | --- | --- |
| Python backend tests | 52 passed, 1 skipped | Includes synthetic model replies, invalid claims, Chinese retry/rejection, safe provider errors, shared quota, regeneration and ownership. Optional live marker skipped here. |
| Frontend unit tests | 9 passed | Composer validation, API behavior and save state. |
| Playwright browser tests | 20 passed | 10 cases each on desktop/mobile Chromium, using synthetic API fixtures. |
| Live integration smoke | 14 checks passed | Real Django, isolated SQLite, real browser and official PubMed retrieval; AI explicitly disabled. |
| TypeScript and frontend production build | Passed | No TypeScript errors; Vite bundle generated. |
| Django checks, migration drift, OpenAPI validation | Passed | No new migration required; no schema warnings. |
| API and frontend Docker builds | Passed | Production images built locally. |
| Production service integration | 4 checks passed | Disposable PostgreSQL migrations, Redis cache, secure login/session, actual Gunicorn health and Caddy configuration validation. |
| Export visual inspection | Passed for supplied sample | Both pages of the generated PDF rendered and inspected; Chinese heading and source text readable. Not an exhaustive font or document-size test. |
| Public HTTPS deployment | 14 checks passed | Real Render service, Neon database, live PubMed and desktop/mobile browser; no AI calls. |
| Local normal-site startup | Passed | Health reports version 3.0.0 through frontend proxy; existing SQLite backed up before startup. |

Initial browser failures were caused by an ambiguous test selector and were
resolved before the complete 20-case passing run. Initial container smoke failures
were missing HTTPS host/referer context in the test client; the corrected test
passes with CSRF protection enabled. No protection was disabled to make it pass.

Machine-readable evidence: [backend](backend-tests.xml),
[frontend](frontend-tests.xml), [browser](browser-tests.xml),
[live integration](live-smoke.json), [deployment](deployment-smoke.json).
Illustrated report: [report.html](report.html).

## Manual acceptance is separate

Six explicitly confirmed v2 checks remain recorded as passed: profile saving,
logout, follow-up context, conversation persistence, rename/history search and
answer bookmarking. The Chinese-answer case remains blocked in the unconfigured
environment. Screenshots of partial workflows are not complete test results.
An alternate-window sign-in prompt was not established as session loss.
See [feedback.md](feedback.md) and [manual-feedback.json](manual-feedback.json).

No v3 manual acceptance is inferred from automated fixtures. The following are
still required after the operator configures Gemini:

1. Run `configure-model.ps1` locally, enter the key only at its hidden prompt,
   restart the app, and pass **Check AI connection** in Settings.
2. Save Chinese and submit a new GLP-1 research question. Confirm Chinese prose,
   original-language source quotations and accurate claim-to-source support.
3. Regenerate an existing literature-only answer; verify a new revision and an
   unchanged original answer and bookmark.
4. Exercise real provider quota/errors. Confirm sources remain visible and that
   no unsupported or wrong-language draft is published.
5. Public HTTPS, reload persistence and account isolation now pass. A timed idle/wake cycle and backup/restoration drill remain untested.

## Boundaries and operational status

- Gemini Free Tier was selected, but this app cannot inspect account billing or
  guarantee model availability. Provider configuration does not imply a working key.
- Testers share the server's Gemini quota. Draft plus review normally needs two
  calls; a language retry may add another. No automatic paid fallback is enabled.
- Retrieval uses abstracts and metadata, not unavailable full text. Chinese query
  mapping remains a bounded glossary. Language detection and numerical checks are
  conservative heuristics, not complete semantic or clinical verification.
- Production instructions use a new PostgreSQL database; local research is not
  silently uploaded or migrated. A Free Render service and a Neon project in the Free organization were provisioned with explicit user authorization; no paid upgrade was made.
- No public-load benchmark, independent security audit or clinical validation
  was performed. The app has no password-reset or invitation-management UI.
- Prior version tags are preserved. This round's reports and GitHub text are English.

## Inputs and reproduction

- [Original and accumulated implementation prompt](consolidated-prompt.md)
- [Round 3 scope](description.md)
- [README setup and verification commands](../../README.md)
- [Persistent deployment procedure](../../docs/deployment.md)
- [Sample exported research PDF](sample-research-export.pdf)
