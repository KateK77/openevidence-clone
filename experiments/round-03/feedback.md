# Consolidated manual feedback and Round 3 response

Recorded November 14-15, 2026 (America/Chicago). This is a snapshot of user-led
Round 2 acceptance, not a claim that every checklist item was exercised.

| Finding | Evidence strength | Round 3 response | Acceptance still needed |
| --- | --- | --- | --- |
| Chinese selected but no Chinese answer delivered | Explicit user report and screenshot; model unconfigured | Gemini setup, capability notices, Chinese prose validation, a retry, owner-only answer regeneration | Live Gemini Chinese answer and citation inspection after a key is supplied |
| Saved language preference appeared to promise an immediately available feature | Explicit usability feedback | Prominent bilingual limitation next to preferences and composers; mode-specific submit label | User review of the new wording |
| Source existence alone does not establish claim support | Review of the v2 implementation; no fabricated claim was demonstrated | Exact-quote and membership checks plus numeric guard and a separate automated claim review; failures withhold drafts | Independent review of real generated claims |
| Provenance labels mixed preprocessing with final query execution | Expanded screenshot showed both the original follow-up and context-expanded queries | Four stages with distinct labels in UI and exports | User comprehension of the revised trace |
| Testers need a site that works when the owner's PC is off | User deployment question | Built React, Gunicorn, HTTPS proxy, PostgreSQL and shared Redis deployment recipe | Choose host/domain, provision and verify external availability |
| Alternate view displayed a sign-in prompt | Screenshot only; original tab remained available | Recorded as an unconfirmed observation; no session-loss fix is claimed | Reproduce with browser/window/session details if it recurs |

## Confirmed passing manual checks to preserve

- V2-MAN-001: **passed** — Profile save feedback and persistence.
- V2-MAN-002: **passed** — Immediate sign-out and persistence after reload.
- V2-MAN-018: **passed** — Follow-up conversation placement and retrieval context preservation.
- V2-MAN-021: **passed** — Conversation persistence after reload and reopening from research history.
- V2-MAN-022: **passed** — Conversation rename, history search and persistence.
- V2-MAN-020: **passed** — Answer bookmarking, feedback and persistence.
- V2-MAN-034: **blocked** — Chinese AI answer availability with Chinese selected.

## Partial and untested evidence

Publication Saved feedback, displayed metadata and result lists were observed.
That alone does not establish reload persistence, source fidelity, filter quality
or citation entailment. Unreported tests remain unverified. The language check is
blocked in the original environment, not passed. Round 3 automated mock responses
are explicitly synthetic and must never be merged into user acceptance results.

No user-requested fixes were performed during manual acceptance. Implementation
started only after the explicit request to consolidate feedback and build a new version.
