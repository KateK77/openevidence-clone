# Architecture

The React SPA uses React Router for navigation and TanStack Query for server data. The browser uses Django sessions and sends a CSRF token with state-changing requests. Django REST Framework validates API inputs and filters private queries by the session user.

## Evidence flow

1. The backend normalizes a research question, detects research intent and builds up to two PubMed queries. Follow-ups can incorporate recent question terms.
2. ESearch yields ranked PMIDs. EFetch supplies publication metadata and abstracts. Calls have timeouts, per-process pacing and a 30-minute cache.
3. A deterministic rank combines search positions, title token overlap and abstract token overlap. PMID and DOI deduplication happen before context construction.
4. The prompt sends a bounded set of abstract excerpts and recent questions as untrusted JSON data. Structured model output is validated against the exact PMID and excerpt allowlist. Failure leaves the underlying literature visible.
5. The database stores private conversations and turns, canonical publications and per-answer evidence snapshots, query provenance, model identifier, timestamps and preferences. The transaction commits the turn and its sources together.

Exact-source checks verify record identity and quoted text. They do not establish that a generated interpretation follows from the text. The UI exposes the evidence for independent review. Retrieval is abstract-only and supports PubMed literature discovery. It does not grade clinical evidence quality. Guidance and safety claims require independent review.

## API

See [generated OpenAPI schema](openapi.yaml) or request `/api/schema/` after signing in.

| Area | Routes |
| --- | --- |
| Public bootstrap | GET session and health, POST register and login |
| Account | POST logout, GET/PATCH profile and settings |
| Research | POST ask, GET/DELETE conversations, GET/PATCH/DELETE conversation by ID |
| Answers | GET answer by ID, PUT/DELETE saved state, list saved answers, export md/pdf/bib/csv |
| Literature | GET search and details by PMID, PUT/DELETE saved state and collection, list saved publications |

All routes are under `/api/`. The session endpoint establishes a CSRF cookie and returns a masked token. Register and login rotate the session token. Send the current token in `X-CSRFToken` for writes. Invalid data returns HTTP 400, unauthorized actions return 403 or a scoped 404, and throttled actions return 429. A research request that successfully persists a retrieval or model failure returns 201 with the turn's status. Direct PubMed search failures return 503.

The single-process local application uses in-memory cache and request pacing. A multi-worker deployment needs shared caching, centralized NCBI pacing, and gateway-based request limits. Questions go to PubMed as search terms and to the configured model provider as text during generation. Application code avoids logging request bodies or provider credentials. No live patient data belongs in this research workspace.

[Official NCBI E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25501/)
