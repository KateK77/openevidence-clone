# CUA-only verification boundary

This is a real visual Google Chrome Computer Use Agent (CUA) benchmark. **A UI result is NOT proof of every technical or safety claim in the Description.**

- **V3-A02, V3-A07 / Sections 13, 15, 17:** Login denial, per-user UI behavior and browser-visible errors are CUA observations; Django password hashing, CSRF enforcement, route/API authorization, token/cookie scope, secrets scans and source-code-level prompt-injection defenses need separate authorized engineering reviews.
- **V3-A04, V3-A05 / Sections 4-5:** CUA can follow official PubMed links and compare visible metadata. It cannot certify PubMed request implementation, cache correctness, API rate limiting, source dedup internals, or full-text rights merely from UI.
- **V3-A09–A12 / Sections 7-8:** A real accepted answer and visible supporting excerpts are meaningful but not independent medical correctness or full claim-check algorithm proof. Controlled fault fixtures reveal visible rejection behavior, not genuine live review quality.
- **V3-A21 / Section 17:** Provider billing charges, global quotas, actual invoices, network timeouts and safe server-side provider config require authorized provider/runtime checks. Never spend on AI generation or provider probes without separate permission.
- **V3-A22 / Section 15:** Database upgrades preserving users, snapshots and histories require a pre/post migration copy with database assertions; **no CUA PASS can certify V3-A22**. It has zero CUA cases and is tracked in coverage as non-CUA.
- **V3-A23–A24 / Section 16:** HTTPS access and observable persistence are CUA-testable; actual Neon/Postgres architecture, worker lifecycle, deployment source SHA, free-tier expiry policy and service usage require deployment documentation/engineering evidence.
- **PDF / Section 14:** Opening PDFs visually tests rendering, not complete PDF structural validity; CSV/BibTeX syntax and formula escaping may need separate file parsing. If a test explicitly requires export-byte assurance beyond the permitted browser viewer, record the limitation instead of granting PASS.

If a required fixture, real provider, independent browser profile, special failure profile or faithful viewport is unavailable, record **BLOCKED** after an actual attempted setup with a precise blocker. If never attempted, leave **NOT_RUN**. Never infer PASS from Playwright/API/unit tests, historical smoke tests or fabricated screenshots.
