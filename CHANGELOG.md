# Changelog

## v3.0.0-r3

Integrated Round 2 manual feedback into a consolidated implementation prompt.
Added Gemini server-side setup, a credential-free connection state and Chinese
output check, explicit literature-only language notices, and a mode-aware submit
button. Chinese generations must pass a prose check; a wrong-language draft is
retried once and otherwise withheld. New answer revisions reuse the original
evidence snapshot without overwriting saved research. Added numerical consistency
and a separate automated claim-support review after source/quote checks, with
claim-level audit labels and limitations sections. Provenance and exports now
separate normalization from executed queries. Added a shared model-call budget
and Docker/Caddy/PostgreSQL/Redis deployment configuration. Live Gemini acceptance
depends on the operator's key and quota; automated fixtures are not clinical validation.

## v2.0.0-r2

Rebuilt the research interface and save workflows following manual acceptance. Added short Chinese query normalization with transparent fallbacks, saved searches, distinct publication dates, embedded multilingual PDF fonts, clearer evidence cards/table views, and reliable local startup. Hardened logout and account-switch response handling. Preserved existing data through an additive migration and local backups. See experiments/round-02/results.md for verification and remaining limitations.

## v0.1.0-r1

Initial research workspace with PubMed integration, optional abstract-grounded synthesis, citation and excerpt validation, persistent conversations, source and answer libraries, research exports, and session authentication.
