# Portfolio release verification

**Corrected public workflow run: 17/18 passed (94.4%); 1 failed; 0 NOT_RUN.**
**AI generation: 0/2 research requests produced an accepted synthesis.** Source and numeric checks rejected both drafts. Literature retrieval, follow-up context and saved research remained usable. This is a material limitation.

Application commit: c903b65ce3f8f49fe72416ca8948d215a0690a49.
Public URL: https://medevidence-ai-v3.onrender.com. Verified November 16, 2026.
Render deployment dep-dbtbu4p9aqoc73akvgl0 was live before this run.

## Methods and evidence

- Chromium controlled by Playwright locators plus labelled API assertions; no intercepted or mocked live responses.
- Desktop 1440 x 1050; mobile 390 x 844. Synthetic shared accounts only.
- Two application questions: GLP-1 evidence, then limitations. Existing Gemini configuration, no automatic failed-generation rerun.
- Application model calls are distinct from browser automation. No OpenAI native CUA requests were made. Provider token/invoice usage was not independently measured; a free-tier setting is not a billing receipt.
- [Exact corrected runner](public-2026-11-16T08-41-45-564Z/runner.cjs), [results](public-2026-11-16T08-41-45-564Z/results.json), [answer snapshot](public-2026-11-16T08-41-45-564Z/answer.json), [follow-up](public-2026-11-16T08-41-45-564Z/follow-up.json).
- [Screenshot manifest](../../docs/screenshots/README.md). Raw captures and downloaded exports remain in each run directory.

## Difficulty summary

| Difficulty | Executed | PASS | FAIL | NOT_RUN | Pass rate |
|---|---:|---:|---:|---:|---:|
| Easy | 4 | 4 | 0 | 0 | 100.0% |
| Medium | 10 | 10 | 0 | 0 | 100.0% |
| Hard | 4 | 3 | 1 | 0 | 75.0% |

These 18 release checks do not replace the frozen 100 native-CUA cases. No Expert cases were included in this smoke suite. The rate measures workflows, not medical correctness.

## Per-check results

| ID | Difficulty | Acceptance condition | Result |
|---|---|---|---|
| P01 | Easy | HTTPS health confirms PostgreSQL and public demo mode | **PASS** |
| P02 | Easy | Published researcher credentials log in and survive reload | **PASS** |
| P03 | Medium | Shared profile changes are forbidden in UI and API | **PASS** |
| P04 | Medium | Real PubMed PMID search resolves metadata, abstract and DOI | **PASS** |
| P05 | Medium | Save publication confirms success and persists after reload | **PASS** |
| P06 | Medium | Collection edit and filter persist without duplicating records | **PASS** |
| P07 | Medium | Saved PMID search can be saved and restored | **PASS** |
| P08 | Hard | GLP-1 question creates a real literature-backed conversation | **PASS** |
| P09 | Hard | AI synthesis completes with exact source quotations and automated claim checks | **FAIL** |
| P10 | Medium | Answer bookmark persists and appears in Saved answers | **PASS** |
| P11 | Medium | Markdown, PDF, BibTeX and CSV downloads are nonempty and correctly encoded | **PASS** |
| P12 | Hard | Follow-up stays in the conversation and PubMed queries retain GLP-1 context | **PASS** |
| P13 | Medium | Conversation rename and history search persist | **PASS** |
| P14 | Medium | Preferences save and survive page reload | **PASS** |
| P15 | Hard | Published reader credentials work; another account cannot access the researcher answer | **PASS** |
| P16 | Medium | Mobile dashboard and evidence table have no page overflow; drawer can close | **PASS** |
| P17 | Easy | Sign out removes access to the protected answer | **PASS** |
| P18 | Easy | No uncaught browser exceptions during the run | **PASS** |

P03 and P15 include direct API assertions. P09 inspects stored citation support. P12 passes conversation/retrieval-context requirements only; its generated draft failed numeric validation.

## Failed synthesis: retained, not retried

- Initial answer: generation_error / verification_failed: **A source ID or quoted excerpt failed validation.**
- Follow-up: generation_error / verification_failed: **A numerical statement was not present in its cited excerpts.**
- Both retained 12 real PubMed records. The UI withheld rejected prose and allowed source inspection and exports.
- The synthesis screenshot shows the unavailable state. The citation screenshot is an original publication/DOI, not a validated generated claim.
- No validator was weakened, model result fabricated, or failed status relabelled. Model/schema investigation remains necessary before claiming reliable synthesis.

## First attempt and harness correction

[Original results](public-2026-11-16T08-35-54-110Z/results.json) and [original runner](public-2026-11-16T08-35-54-110Z/runner.cjs) remain intact.
The initial runner clicked Ask AI immediately after navigation, before session bootstrap completed. Render application logs contained no /api/ask/ request in that run; the conversation wait timed out. The corrected runner waits for the authenticated account label.

The original raw file records 11 PASS, 1 FAIL and 6 NOT_RUN. Two provisional PASS labels (P16 and P17) covered only the independent mobile/logout portions because no answer existed. They are **not full acceptance passes** and are excluded from final scoring. The corrected runner requires those answer-specific portions. Original evidence was not overwritten.

This was a test-readiness correction, not an automatic provider retry. The only two actual research submissions occurred in the corrected run. Acceptance conditions were retained.

## Local verification

| Check | Actual result | Evidence |
|---|---|---|
| Backend pytest | 62 passed, 1 live contract skipped | [JUnit](backend-tests.xml) |
| Django system and migration checks | Passed | No issues or missing migrations |
| OpenAPI validation | Passed | [Schema](../../docs/openapi.yaml) |
| Frontend Vitest | 9 passed | [JUnit](frontend-tests.xml) |
| TypeScript/Vite build | Passed | Compiled into hosted image |
| Playwright desktop/mobile fixtures | 20 passed | [JUnit](browser-tests.xml), mocked API |
| Hosted Docker build | Passed | Python 3.12 / Node 24 multi-stage image |
| PostgreSQL hosted smoke | 6 checks passed | [Results](hosted-image-smoke.json) |
| Blueprint | JSON schema passed | [Result](blueprint-validation.json); CLI unavailable |

The PostgreSQL smoke exercised migration/startup, SPA/static routing, 404 behavior, nonprivileged idempotent seeding, and six concurrent reservations admitting exactly two calls under a two-call test quota. No provider request was made.

## Remaining limits and manual steps

- No visitor setup is required. Both published credentials work over HTTPS.
- Live synthesis remains unreliable in this sample. The operator can disable it using PUBLIC_DEMO_LIVE_AI=0 while retaining literature features. Source checks must not be bypassed.
- Free Render services sleep; Neon has quotas, not a fixed trial deletion date. Other visitors can change shared research.
- Call caps bound volume, not an exact invoice. Provider billing visibility was not tested.
- No clinical validation, sustained load test, general medical translation, full-text coverage or accessibility certification is claimed.
- The frozen 100 native-CUA cases remain NOT_RUN. Paid execution needs explicit approval and reliable budget controls. [Evaluation index](../../docs/evaluation.md).

## GitHub Actions verification

Both complete CI runs passed for commit 31f1a2ce9d216bdb7e816e69feabcf0bde7be6e7: [main](https://github.com/KateK77/openevidence-clone/actions/runs/43834431102) and [v3-round-03](https://github.com/KateK77/openevidence-clone/actions/runs/43834431112). This includes backend, frontend, desktop/mobile browser tests, both production container profiles, and the PostgreSQL public-demo concurrency smoke. [Recorded run metadata](github-actions.json).

The subsequent evidence-only commit records these completed runs and a fully loaded mobile gallery capture. It changes no backend, frontend, deployment configuration or application tests. The published smoke runner now also waits for mobile session bootstrap before capturing; the exact previously executed runners remain archived. No additional research/model request was made for that recapture.
