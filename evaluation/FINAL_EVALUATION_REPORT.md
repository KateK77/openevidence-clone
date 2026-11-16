# MedEvidence final evaluation — NOT EXECUTED

**Preparation report; no paid native CUA evaluation has started.**

Application baseline: `7d64a988fc1b1e27433aa96c90b743c6336baea5`. Model planned: `gpt-5.4-2026-03-05`.
Paid native requests: 0. Estimated API spending recorded: $0.00.

| Status | Count |
|---|---:|
| PASS | 0 |
| FAIL | 0 |
| BLOCKED | 0 |
| ERROR | 0 |
| NOT_RUN | 100 |

Primary scheduled ratio: 0/100 = 0%. This is **not a measured success rate** while all cases remain unexecuted.
Validly evaluated pass rate: **N/A (no validly evaluated tests)**.

## Difficulty summary

| Difficulty | Total | PASS | FAIL | BLOCKED | ERROR | NOT_RUN | Scheduled pass ratio |
|---|---:|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 0 | 0 | 0 | 0 | 30 | 0% (unexecuted) |
| Medium | 40 | 0 | 0 | 0 | 0 | 40 | 0% (unexecuted) |
| Hard | 20 | 0 | 0 | 0 | 0 | 20 | 0% (unexecuted) |
| Expert | 10 | 0 | 0 | 0 | 0 | 10 | 0% (unexecuted) |

## Functional categories

| Category | Total | PASS | FAIL | BLOCKED | ERROR | NOT_RUN |
|---|---:|---:|---:|---:|---:|---:|
| Navigation and accessibility | 8 | 0 | 0 | 0 | 0 | 8 |
| Accounts, sessions and ownership | 13 | 0 | 0 | 0 | 0 | 13 |
| Question validation and short/Chinese input | 4 | 0 | 0 | 0 | 0 | 4 |
| Context and conversation history | 10 | 0 | 0 | 0 | 0 | 10 |
| Evidence library and save feedback | 7 | 0 | 0 | 0 | 0 | 7 |
| Real literature, metadata and retrieval | 7 | 0 | 0 | 0 | 0 | 7 |
| Answer saves and exports | 10 | 0 | 0 | 0 | 0 | 10 |
| Preferences and regenerated answers | 7 | 0 | 0 | 0 | 0 | 7 |
| Configuration, readiness and failures | 8 | 0 | 0 | 0 | 0 | 8 |
| Literature filtering and sorting | 8 | 0 | 0 | 0 | 0 | 8 |
| Auditable provenance | 2 | 0 | 0 | 0 | 0 | 2 |
| Evidence-grounded AI and detail page | 4 | 0 | 0 | 0 | 0 | 4 |
| Security, untrusted inputs, rate limits | 5 | 0 | 0 | 0 | 0 | 5 |
| Citation and claim verification | 6 | 0 | 0 | 0 | 0 | 6 |
| Public persistence and research-only identity | 1 | 0 | 0 | 0 | 0 | 1 |

## Free preflight and limitations

Offline infrastructure: PASS; 13 checks recorded. Harness unit tests: see logs/harness-unit-tests.tap. Browser/SQLite checks used fresh synthetic data with application LLM credentials removed and external networking blocked.
The first restricted-environment server start did not become ready; rerunning the same offline preflight with local process permission passed. This was an infrastructure rerun with zero API requests, not a paid test retry.
No live PubMed, Gemini, OpenAI model entitlement, native paid compatibility, provider-fault fixture or hosted restart was validated in this offline run. See PREREQUISITE_READINESS.md for all 26 explicitly blocked prerequisites and BILLING_SAFETY.md for the global paid-execution block.

## Budget

Central estimate: $10.21 for 100 tasks; optimistic $5.40; conservative $23.35. These are forecasts, not actual charges. $5 and $10 central scenarios forecast 49 and 99 full task attempts before conservative call reservations/prerequisite failures. Neither is a promised valid completion count. Full assumptions and per-difficulty token totals are in BUDGET_ESTIMATE.md.
Local computer-tool surcharge is not separately itemized in reviewed pricing; $0 is conditional, and unconfirmed applicable fees block paid execution. No other billable tools are enabled. Paid application-side provider costs must also fit the shared $10 ceiling.

Actual invoice cap is unverified. The runner blocks --execute before any HTTP even with an approval file. All 26 additional prerequisite cases are individually documented; none has been silently downgraded or removed. See BILLING_SAFETY.md and PREREQUISITE_READINESS.md.

## Findings

No benchmark application defects or passes are asserted before execution. The previously observed Gemini verification failure is historical development evidence, not a result for any frozen case. Live and fault-profile prerequisites remain incomplete. Native API trace files do not exist yet because generating them would require unapproved paid calls.

## Per-case results

### T001 — Research identity

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Original identity and research-only disclaimer are visible; no clinical-use or regulatory guarantee.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T002 — Primary navigation

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Each required destination is reachable with a meaningful heading and no fatal page error.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T003 — Register synthetic researcher

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Account created and authenticated identity shown; independent DB check confirms password is hashed.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T004 — Valid sign-in

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: A identity is displayed and account pages are accessible.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T005 — Invalid password

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Clear failure message; no authenticated identity or access to private data.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T006 — Immediate logout

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: UI immediately becomes unauthenticated and private account content is inaccessible.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T007 — Session reload

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: A remains authenticated and the current private view loads.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T008 — Profile name save

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Visible save confirmation; displayed names match submitted values.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T009 — Empty question validation

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: No research turn created; invalid input prevented or explained.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T010 — One-word research

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Submission accepted; real literature or informative retrieval failure shown; not rejected solely for word count.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T011 — Chinese research input

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Input accepted; meaningful translated search terms retrieve relevant diabetes literature; no fabricated result.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T012 — Multiline composer

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Composer contains both lines; Shift+Enter does not submit prematurely.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T013 — Suggested research topic

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: A relevant research question is populated or submitted with visible feedback.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T014 — History list

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: A's seeded synthetic conversations appear; B's private title is absent.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T015 — Reopen conversation

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Original question, chronology and stored evidence are accessible.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T016 — Library navigation

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Search and saved-publication views are distinguishable and usable.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T017 — Known PMID lookup

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Returned PMID and title match the independently supplied official record.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T018 — Publication details

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Authors, journal, dates, DOI and source abstract are inspectable and match source metadata.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T019 — Open original record

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: New or current tab reaches the matching official PubMed record, not a fabricated destination.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T020 — Saved-publication listing

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Seeded publication is present with stable identifier and distinguishable from saved answers.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T021 — Saved-answer listing

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Correct answer detail is opened with original question and source information.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T022 — Language save feedback

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Chinese is selected; success feedback appears and unchanged saves cannot duplicate work.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T023 — Detail preference

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Detailed preference is visibly retained; save succeeds.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T024 — Display preference

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Selected preference persists in UI and relevant layout adapts without losing controls.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T025 — Missing-model composer

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Literature-only limitation is visible before submission; UI does not promise a generated answer.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T026 — Missing-model language notice

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Notice distinguishes future generated answers from original-language sources and current lack of generation.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T027 — Keyboard navigation

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Focus is visible and actionable controls are keyboard reachable in usable order.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T028 — Mobile menu

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: All destinations remain reachable; overlay closes; no inaccessible bottom links.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T029 — Empty saved state

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Accurate, readable empty states; no A data or generic server error.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T030 — Answer detail metadata

Difficulty: **Easy**. Status: **NOT_RUN**.

Expected: Original question, timestamp, literature-only status and supporting sources are shown; no fabricated AI text.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T031 — Profile persistence

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Both names persist and save feedback accurately describes success.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T032 — Duplicate registration

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Duplicate rejected clearly; original A password/account unaffected.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T033 — Weak password rejection

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Weak value rejected; correction succeeds without duplicate accounts.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T034 — Logout survives back and reload

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: No live authenticated access remains; private API response independently denies unauthenticated access.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T035 — Conversation rename persistence

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: New title persists and original turns/source associations remain unchanged.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T036 — History query and reset

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Correct matching set, accurate empty state, then restored A history.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T037 — History date ordering

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Order reverses consistently using dates; no missing or cross-user entries.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T038 — Conversation deletion

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Deleted thread absent; old URL fails safely; other threads persist.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T039 — Save publication feedback

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Visible saving/saved state; no duplicate saved association.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T040 — Saved publication reload

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: One correct saved record survives reload and login cycle.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T041 — Remove saved publication

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Record remains removed from A's library; source record and B's data are not improperly removed.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T042 — Collection update

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Collection persists with visible success feedback.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T043 — Collection search and reset

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Matching collection is found; no-match is empty; clear restores all saved items.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T044 — Matching and conflicting year

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Matching filter includes record; conflicting filter excludes it; stale results are not presented as current.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T045 — Journal filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Every returned journal matches the filter; no invented records.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T046 — Clinical-trial filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Returned records have a qualifying trial type; filtering is reflected in request/provenance.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T047 — Review filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Results satisfy review metadata; detail matches listed records.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T048 — Systematic-review filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Results satisfy systematic-review classification; empty set is clearly distinguished from service failure.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T049 — Meta-analysis filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Result types comply; no unrelated stale results from earlier filters.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T050 — Free-full-text filter

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Returned records meet availability filter; app does not imply access to unavailable paywalled text.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T051 — Publication-date sort

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Dates follow documented direction; sorting does not corrupt metadata or repeat identifiers.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T052 — DOI lookup

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Resolves to PMID 33567185 with consistent title and DOI.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T053 — Invalid identifier

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Invalid lookup has clear empty/validation result; valid subsequent search works without stale error.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T054 — Separate publication dates

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Dates are labeled by type; unavailable type is explicit; values match official reference.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T055 — Save answer persistence

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Single bookmark persists with visible Saved feedback.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T056 — Unsave without deleting thread

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Bookmark absent but conversation and all turns remain intact.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T057 — Markdown export

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: UTF-8 disclaimer, question, status and traceable PMID/DOI links are intact; no mojibake.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T058 — PDF export

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Readable question, disclaimer and references; no clipped critical text or corrupted punctuation.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T059 — BibTeX export

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Entries parse; identifier/title/author/DOI preserved; special characters handled; no duplicate keys.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T060 — CSV export

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: CSV parses to consistent columns and preserves complete titles/authors/identifiers.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T061 — Copy answer

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Copied text corresponds to selected answer; no other user's content or broken encoding.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T062 — Preferences after login cycle

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: All three preferences persist independently.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T063 — No-key research workflow

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Literature is retrieved and stored; explicit missing-generation state; no fake synthesis.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T064 — Contextual limitations follow-up

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Both turns remain in one thread; executed queries preserve GLP-1/obesity context and limitations intent.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T065 — Four-stage provenance

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Original input, normalized question, previous questions and actual executed queries are distinct and accurate.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T066 — Evidence table unavailable fields

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Study/year/type/source retained; unsupported findings/limitations explicitly unavailable, never fabricated.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T067 — Mobile evidence and exports

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Table does not force inaccessible page overflow; all required controls can be operated.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T068 — Configured but unchecked

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Configuration is distinguished from a successful connection check and from generated answer success.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T069 — Chinese connection probe

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Actual configured provider returns valid Chinese response; ready status matches recorded call, not mere key presence.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T070 — English evidence synthesis

Difficulty: **Medium**. Status: **NOT_RUN**.

Expected: Real generated English findings, limitations and references supported by retrieved abstracts; retrieval-only is not PASS.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T071 — Chinese research synthesis

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Generated narrative is Chinese; source titles/quotes remain labeled original; claims are supported and not status-message-only.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T072 — Regenerate while preserving original

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: New revision uses original evidence snapshot/current preference; original content/bookmark/provenance unchanged.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T073 — Cross-account direct thread access

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: B cannot read A thread or its source content; server-side authorization confirmed independently.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T074 — Cross-account answer and export access

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: No A answer/export is disclosed; B saved list stays isolated.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T075 — Session and CSRF enforcement

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Normal UI save succeeds; unsafe mutation rejected; session cookie is HTTP-only and data remains unchanged by rejected request.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T076 — Reject nonexistent citation

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Unsupported draft withheld; verification failure explicit; authentic sources still accessible.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T077 — Reject altered quotation

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Draft fails exact-quotation validation; fabricated quotation not presented as verified.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T078 — Reject unsupported numeric claim

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Unsupported numerical claim rejected; verification failure does not masquerade as successful synthesis.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T079 — Reject contradicted claim

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: App withholds unsupported draft even though PMID and quote are valid.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T080 — Wrong-language retry boundary

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Exactly one corrective generation retry then explicit language failure; no English answer published as Chinese.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T081 — Provider credential failure

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Clear provider access failure; no secret exposed; retrieved sources and history remain usable.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T082 — Provider quota exhaustion

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Quota limitation explained; no automatic billing/fallback or endless retry; evidence persists.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T083 — Model timeout

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Bounded wait ends with explicit timeout; no false answer; retrieved evidence retained.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T084 — Literature service failure and recovery

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Failure is distinguishable from no results; UI recovers and successful new result is attributable to restored retrieval.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T085 — Untrusted article injection

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Article instructions are treated as data; no secret disclosure or unauthorized action; source provenance identifies fixture.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T086 — Untrusted user question

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: No fabricated citation is endorsed; response is evidence-grounded, explicit failure or justified refusal.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T087 — Follow-up topic switch

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: New evidence is retrieved for changed topic; original references preserved; context does not force irrelevant old topic.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T088 — Audit generated claims

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: All displayed claims/citations can be traced to actual source text; automated review is not labeled clinical validation.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T089 — Markup rendering safety

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: Input rejected or rendered safely as text; no script executes; no unauthorized data changes.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T090 — History management isolation

Difficulty: **Hard**. Status: **NOT_RUN**.

Expected: A history removed as requested; B history and saved sources preserved; stale A links deny access.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T091 — Complete evidence research lifecycle

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Every step completes with genuine Chinese synthesis, supported citations, intact source provenance, persistent saves and readable exports.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T092 — Two-researcher confidentiality lifecycle

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Both accounts retain own work; no cross-account disclosure/modification; denied accesses do not destroy originals.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T093 — Missing-model to live revision lifecycle

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Honest pre-configuration state; new real Chinese revision; original evidence snapshot/bookmark and exported status preserved.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T094 — Conflicting evidence comparison

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Distinct interventions and populations not conflated; uncertainty/limitations supported; no unsupported superiority or diagnostic certainty.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T095 — Verification failure and explicit recovery

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Initial failure retained; no unverified draft leaked; new answer independently supported; recovery does not overwrite audit trail.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T096 — Public availability and persistence

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Site works independent of developer workstation; data survives service restart; HTTPS sessions secure; no paid-plan change.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T097 — Mobile complete research workflow

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: All workflow steps accessible at narrow width; generated Chinese content intact; no inaccessible controls or privacy leakage.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T098 — Rate-limit isolation and recovery

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: Rate limit visible and enforced; successful recovery after interval; no automatic paid retries or lost existing records.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T099 — Cross-format provenance reconciliation

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: No reference corruption/duplication or mismatched IDs; answer formats preserve provenance and verification status; structured exports parse.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.

### T100 — Long research thread and reproducibility

Difficulty: **Expert**. Status: **NOT_RUN**.

Expected: All five turns persist in order with relevant context/retrieval, correct source-to-turn associations and honest evidence gaps; no assumption earlier claims are automatically true.

Actual: No native CUA attempt.

Reason: Paid native CUA execution has not been approved.

Evidence: None — not executed.
