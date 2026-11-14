# Round 1 results

Date: 2026-11-13 (America/Chicago)

Implementation commit: `2fd3909c08cdf65d2105818e572184da30c0d40a`

Release tag: `v0.1.0-r1`

Implementation agent: Codex (GPT-6 family). Application LLM is configured by the operator.

## Delivered

- React research workspace with question entry, recent conversations, suggested topics and mobile navigation.
- Live PubMed ESearch and EFetch with keyword and identifier resolution, filters, ranking, caching and deduplication.
- Structured, abstract-grounded synthesis with exact PMID and excerpt checks, provenance, and labeled failure and retrieval-only states.
- Session account flows, CSRF protection, per-user history and saved items, preferences, answer details, publication collections and four export formats.
- SQLite local setup, PostgreSQL configuration, labeled synthetic account and conversation seed, OpenAPI and GitHub Actions workflow.

## Verification

| Command | Result |
| --- | --- |
| `python -m pytest -q` with `RUN_LIVE_PUBMED=1` | 13 passed, including live PubMed |
| `python backend/manage.py check` | Passed |
| `python backend/manage.py makemigrations --check --dry-run` | No drift |
| `python backend/manage.py spectacular --validate --fail-on-warn --file docs/openapi.yaml` | Passed |
| `npm run build` | TypeScript and production build passed |
| `npm test` | 2 passed |
| `npm run e2e` | 2 passed in Chromium desktop and mobile emulation with synthetic API fixtures |
| `npm audit` | 0 reported vulnerabilities at verification |

## Known limitations

- Generation was exercised with mocked provider responses. Live model generation requires a compatible endpoint and credentials. PostgreSQL configuration was included, with the tests executed against SQLite.
- Citation validation checks exact source text and provenance. Claim entailment and clinical validity require human review. The application uses available PubMed abstracts and metadata.
- Synthesis is synchronous with progress feedback. The model is selected server-side. The PubMed implementation uses ESearch and EFetch. ESummary and ELink calls are absent.
- Follow-ups carry recent questions and retrieve fresh evidence. Search query extraction is primarily English-oriented.
- Demo data includes a synthetic user and conversation. Landing topics are available to all users. A standalone saved-search feature and preseeded publication records are absent.
- Display and response preferences are available. The interface remains English. Tested responsive coverage is Chromium desktop and mobile emulation.
- A deployment with multiple workers needs shared rate limiting and cache coordination. This is a research demonstration. The independent benchmark suite is outside Round 1 verification.

## Manual acceptance review

The user completed a guided manual review on November 13, 2026. The outcome is partial acceptance, with full platform acceptance still pending. The review contains 30 checks, records the user's save-feedback proposal, and distinguishes observed results from unverified behavior.

The English [manual acceptance report](manual-acceptance/report.html) includes 29 embedded application screenshots. Download the HTML file and open it in a browser to inspect the formatted report and expandable evidence. The English [structured results](manual-acceptance/results.json) provide check-level outcomes and issue records.

Recorded issues include inconsistent sign-out feedback, corrupted PDF/Markdown disclaimer text, duplicated reference punctuation and a five-character input minimum without explanatory feedback. One Chinese query returned no publications. Live model generation remains unverified because the model was unconfigured.

The manual environment used a local backend-port adjustment to 8021 in README.md and frontend/vite.config.ts after an initial conflict on port 8000. That adjustment preceded the user's instruction to record issues without repairs. This report documents the adjusted environment and preserves the original release tag as its baseline.
