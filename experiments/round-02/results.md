# MedEvidence AI 2.0 — Round 2 report

**Disposition: ready for a second manual acceptance round in retrieval-only mode.**

The interface and affected workflows were rebuilt from the original requirements and the user's Round 1 feedback. Existing account and research data were preserved with a backup and an additive database migration. Version 1 remains available under v0.1.0-r1; this release is tagged v2.0.0-r2.

AI synthesis is still a configuration-dependent feature. No live model credential was available, so this report does not mark live AI answer quality as accepted.

## Verification

| Check | Result | Scope |
| --- | --- | --- |
| Backend regression suite | 27 passed; 1 opt-in live test skipped | pytest with deterministic provider fixtures; JUnit retained |
| Frontend interaction suite | 9 passed | Composer, save feedback/retry, and stale account-response rejection |
| Desktop and mobile browser suite | 14 passed | Chromium desktop and iPhone-sized viewport; synthetic API fixtures |
| Real application smoke test | 14 checks passed | Real Django sessions, separate SQLite database, browser, and live PubMed |
| Official PubMed contract smoke | 1 passed | Live ESearch, ESummary, and EFetch for PMID 33567185 |
| Production build and type check | Passed | TypeScript and Vite production build |
| Django checks / migrations / API schema | Passed | No system-check issues; no missing migrations; OpenAPI validation passed |
| PDF visual verification | Passed | Two rendered pages inspected; embedded Chinese/Latin glyphs, headings, citations, and page numbers |
| Local startup and shutdown | Passed | Port validation, SQLite backup, additive migration, and Windows process-tree shutdown |

The backend suite's single skipped test was subsequently run separately against live PubMed and passed. Deterministic tests use clearly labeled synthetic fixtures; the separate live smoke test uses real external literature and real application authentication.

## Feedback addressed

| Round 1 feedback | Round 2 outcome | Evidence / implementation |
| --- | --- | --- |
| Save actions provided no clear feedback | Implemented and tested | Saving/Saved controls, persistent success messages, disabled duplicate submission, edit-to-enable behavior, and recoverable failures. |
| Logout left a stale authenticated profile | Observed behavior resolved in tests | Idempotent CSRF-protected logout, app-specific cookies, private-cache clearing, cross-tab updates, and rejection of old-account responses. The precise cause of the original incident was not proven. |
| Short Chinese terms and single words could not submit | Implemented and tested | Non-empty input is accepted; whitespace-only input remains invalid. Chinese IME composition and Shift+Enter remain supported. |
| Chinese query produced no literature | Improved with an explicit scope limit | A bounded glossary maps common terms, including diabetes mellitus, and exposes the mapping. Unknown terms return an actionable translation limitation. The real Chinese test retrieved 12 records. |
| Saved answers and saved publications were confusing | Implemented and tested | Separate navigation destinations and contextual links make the two collections explicit. |
| PDF/Markdown export contained mojibake | Implemented and inspected | Correct Unicode disclaimer, embedded OFL font, page numbers, and readable source records. CSV includes a UTF-8 BOM and formula-prefix protection. |
| Reference punctuation was duplicated | Implemented and tested | Terminal title punctuation is normalized before formatting references. |
| Publication date type was unclear | Implemented and tested | Electronic publication and journal issue dates are separate. Legacy snapshots identify an unspecified date type. |
| Mobile drawer obscured Profile | Implemented and tested | Scrollable navigation, visible close control, focus handling, Escape support, and narrow-screen overflow checks. |
| Startup failed because of paths, npm, or port conflicts | Implemented and locally verified | Project-relative scripts, dependency discovery, port/service checks, readiness checks, SQLite backup, and migration. Blank DATABASE_URL now correctly selects SQLite. |
| AI generation was unavailable | Transparent; live generation remains unverified | The optional provider integration and citation validator remain available. No model credential was configured; the application explicitly uses Literature mode rather than claiming generated findings. |

## Real browser checks

- Registration and authenticated session survive a page reload: **PASS**.
- Short Chinese clinical query maps to English and retrieves live PubMed records: **PASS**.
- Answer save is visible and persists after reload: **PASS**.
- Structured evidence table remains contained on a narrow screen: **PASS**.
- PDF downloads through authenticated export endpoint: **PASS**.
- Markdown disclaimer is valid Unicode: **PASS**.
- Official ESearch + ESummary + EFetch resolves known PMID and separate publication dates: **PASS**.
- Publication collection persists: **PASS**.
- Preferences persist with visible save confirmation: **PASS**.
- Profile save and immediate logout clear the authenticated UI: **PASS**.
- Saved answer remains after sign-out and sign-in: **PASS**.
- Mobile drawer reaches Profile without page overflow: **PASS**.
- Second account cannot access the first account answer, history, or saved publications: **PASS**.
- No uncaught browser exceptions: **PASS**.

The live query mapped to **diabetes mellitus treatment** and returned **12** PubMed records. PMID 33567185 was independently resolved through official E-utilities, and electronic and issue dates were displayed separately.

## Data and version preservation

- The migration adds SavedSearch and does not rewrite existing evidence snapshots.
- Existing local account, conversation, turn, and saved-publication counts were unchanged by the upgrade checks.
- SQLite backups are kept locally in .runtime/backups and excluded from Git, together with credentials, databases, dependencies, and logs.
- App-specific cookies require one new sign-in after upgrading from v1.
- The repository remains private. Reports, release notes, and documentation are in English.

## Remaining limits

- Live model-provider generation was not exercised. Both LLM_MODEL and LLM_API_KEY must be configured server-side before accepting the AI synthesis workflow.
- Citation validation checks retrieved PMID membership and exact abstract excerpts. It does not independently prove that a clinical interpretation is supported.
- Chinese query support is a limited terminology glossary, not unrestricted translation. Unmapped terms require reformulation or English medical keywords.
- Evidence retrieval is limited to PubMed abstracts and metadata. Retrieval ranking and search recall have not been clinically validated.
- PostgreSQL, production multi-worker operation, load testing, and a formal security/accessibility audit were not exercised.
- The reported passes are automated and agent-inspected checks. They are not a substitute for the user's second manual acceptance round.

## Reproduce and review

Run the commands in the root README. The checked-in scripts/live_smoke.py runner uses separate test ports and a separate database. The English live-smoke.json record, backend-tests.xml, frontend-tests.xml, screenshots, and sample-research-export.pdf provide supporting evidence.

Open the local workspace at http://127.0.0.1:5173. Sign in once, then manually retest save feedback, logout, short bilingual queries, source dates, exports, and mobile navigation. Configure the model only when ready to validate live synthesis and claim support.

GitHub Actions runs the deterministic checks after pushes. Consult the repository Actions page for the status of the release commit; this local report does not assume a remote CI result.

[Illustrated report](report.html) · [Live test record](live-smoke.json) · [Release](https://github.com/KateK77/openevidence-clone/tree/v2.0.0-r2)
