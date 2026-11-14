# Architecture

The React SPA uses React Router for navigation and TanStack Query for server data. The browser uses Django sessions and sends a CSRF token with state-changing requests. Django REST Framework validates API inputs and filters private queries by the session user.

## Evidence flow

1. The backend normalizes a research question, detects research intent and builds up to two PubMed queries. Follow-ups can incorporate recent question terms.
2. ESearch yields ranked PMIDs. Library searches also use ESummary. EFetch supplies publication metadata and abstracts, including distinct electronic and journal-issue dates. Calls have timeouts, per-process pacing and a 30-minute cache.
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
| Saved searches | GET/POST saved-searches, DELETE saved-searches by ID |

All routes are under `/api/`. The session endpoint establishes a CSRF cookie and returns a masked token. Register and login rotate the session token. Send the current token in `X-CSRFToken` for writes. Invalid data returns HTTP 400, unauthorized actions return 403 or a scoped 404, and throttled actions return 429. A research request that successfully persists a retrieval or model failure returns 201 with the turn's status. Direct PubMed search failures return 503.

The single-process local application uses in-memory cache and request pacing. A multi-worker deployment needs shared caching, centralized NCBI pacing, and gateway-based request limits. Questions go to PubMed as search terms and to the configured model provider as text during generation. Application code avoids logging request bodies or provider credentials. No live patient data belongs in this research workspace.

[Official NCBI E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25501/)

## Version 2 behavior

Common Chinese terms are mapped using a bounded terminology glossary before query construction. Unmapped Chinese text returns an actionable query limitation; a zero-result search is never described as proof that no evidence exists. Normalization and actual search strings are stored in provenance. Explicit follow-ups inherit topic terms; a new short standalone topic does not inherit an unrelated previous topic.

Private objects remain owner-scoped. Saved searches use a per-owner hash of normalized filters for idempotence. Logout accepts an already-anonymous session while still requiring CSRF protection. App-specific session and CSRF cookie names prevent collisions with other local Django applications. The browser cancels queries at authentication changes, clears private caches, synchronizes tabs, and discards responses started before an account boundary.

SaveForm tracks edited versus persisted fields. Controls disable during saving and after a successful unchanged save. Errors preserve edits for retry. Source and answer bookmarks expose a disabled Saved state with a separate remove action.

PDFs use an embedded, openly licensed static Noto-derived font for Chinese and Latin text. Markdown uses UTF-8; CSV adds a UTF-8 BOM and escapes spreadsheet formula prefixes. Existing evidence snapshots remain unchanged; older records without a date type are labeled accordingly.
