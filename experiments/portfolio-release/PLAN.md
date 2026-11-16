# Portfolio release: comparison and verification plan

Reference inspected: KateK77/mychart-clone main README, deployment guide and AI-browser report on November 16, 2026. Reference content is a presentation benchmark only; no patient-portal medical functionality or reported pass rate is transferred to MedEvidence.

| Area | Existing MedEvidence gap | This release |
|---|---|---|
| Entry point | Default branch describes V2; public service runs V3 | Bring V3 plus portfolio improvements to main; preserve historical branches/tags |
| README | Setup-first, no featured gallery or published login | Introduction, live tour, protected demo accounts, gallery, architecture, installation, evidence and limitations |
| Hosting | Working Render Docker + Neon PostgreSQL, no reusable root Blueprint | Preserve service/database; add reproducible opt-in Blueprint and database-aware health check |
| Demo | Local-only seed requires private password | Two nonprivileged, explicitly synthetic shared accounts; idempotent opt-in seed; protected profiles |
| Public AI budget | Per-minute cache cap resets on restart | PostgreSQL daily/lifetime reservations before every attempted provider call; explicit live-AI opt-in |
| Screenshots | Scattered historical smoke images | Capture actual current deployed UI into docs/screenshots, with provenance and honest synthesis status |
| Evaluation | Historical reports and unexecuted frozen native-CUA suite on separate branch | Evidence index distinguishes unit tests, mocked Playwright, real public smoke and unexecuted native CUA |

## Planned release checks (not the frozen native-CUA 100)

Backend pytest, Django system/migration/OpenAPI checks, frontend Vitest, TypeScript/Vite production build, existing desktop/mobile Playwright fixtures, Docker build and disposable PostgreSQL migration/seed/concurrency smoke. Public Playwright steps are defined in scripts/portfolio_public_smoke.cjs before execution, with per-step difficulty, expected condition, actual status and screenshots. Record failures and test-only corrections; do not relabel fixtures as genuine model output.

No paid OpenAI native CUA requests are authorized. The frozen 100 cases remain unchanged on evaluation/medevidence-native-cua-100. Their original baseline differs from this deployment; they must not be presented as validation of the portfolio changes. The separate standardized benchmark branch is also preserved.

Public smoke uses only synthetic shared accounts and clearly named test records. Live PubMed is never mocked. At most one initial research question and one follow-up are planned for live application generation; failures remain evidence. These are application-provider calls, not native CUA. Do not auto-retry a failed generation for a flattering screenshot.
