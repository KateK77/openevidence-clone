# MedEvidence AI 3.0 — Complete Product Requirements

**Version:** 3.0

**Repository:** KateK77/openevidence-clone

**Release references:** v3.0.0-r3 and v3.0.0-r3-hosted

**Document type:** Standalone product and system requirements

This document defines the complete MedEvidence AI 3.0 product, including its research workspace, real literature retrieval, optional AI synthesis, language behavior, claim checks, evidence revisions and hosted operation. No earlier description, prompt or feedback transcript is required to understand it. Acceptance requirements are distinct from implementation status and test results.

## 1. Product purpose and research boundary

MedEvidence AI is a biomedical research workspace for healthcare professionals and researchers. It helps users formulate questions, retrieve relevant PubMed publications, inspect original abstracts, obtain source-linked synthesis when a model is available, continue research conversations and retain an auditable research history.

Use an independent MedEvidence identity. The product is not affiliated with OpenEvidence and must not copy proprietary branding or restricted material.

Display **“RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.”** across the application and answer exports. Do not claim medical certification, clinical validation, diagnostic certainty or suitability for real clinical decision automation. Use synthetic demonstration accounts and questions rather than real patient data.

Scientific publications must be retrieved from real services. Model generation must use the configured provider, not canned medical answers. Mock responses belong only in clearly identified development/test fixtures.

The supported evidence scope is PubMed metadata and available abstracts. Do not imply that unavailable full texts were analyzed or bypass publication access restrictions.

Repository documentation, requirements and reports are in English. Research input, localized status messages and generated responses can use supported languages.

## 2. Users, ownership and navigation

Anonymous visitors can inspect the introduction and sign in or register. Authenticated users maintain their own research workspace.

The interface must provide:

| Destination | Required purpose |
|---|---|
| Research home | Multiline question composer, topic examples, recent conversations, research disclaimer and current synthesis mode |
| Research history | Searchable and sortable conversations with reopen, rename and delete actions |
| Conversation | Ordered questions and outcomes with links to evidence and a follow-up composer |
| Answer details | Synthesis/status, findings, limitations, citations, source snapshots, provenance, revision information, copy/save/export |
| Search PubMed | Keyword, PMID and DOI search; filters; original publication details |
| Saved publications | Reading list, filtering, collections and removal |
| Saved answers | Bookmarks linked to the exact stored answer or revision |
| Settings | Answer language, detail, density, model readiness and an explicit connection check |
| Profile | Account identity, editable names and immediate sign out |

Saved publications and saved answers must be distinct. Every screen must provide meaningful loading, empty and failure states.

Backend authorization must scope all private resources, mutations and exports to their owner. A second account must not gain access by changing a URL or object ID.

## 3. Question input and terminology handling

Accept trimmed questions from 1 to 2,000 characters, including single-word English input and supported short Chinese medical terms. Reject whitespace-only submissions. Support Enter to submit, Shift+Enter for a newline and safe IME composition handling.

Prevent duplicate pending submissions and show progress during retrieval, generation and checking. A non-streaming workflow is acceptable when the pending state explains that the operation can take time.

Normalize supported Chinese terminology through a bounded glossary and record the transformation. Unknown terminology must produce an explicit mapping limitation and actionable guidance. Do not label an unsupported translation as a successful search with no evidence.

Chinese query normalization and Chinese answer generation are separate capabilities. Mapping a query to English PubMed terms does not mean an AI-generated Chinese answer exists.

## 4. Real literature retrieval

Use official PubMed E-utilities: ESearch, ESummary where applicable, and EFetch. Retrieval must remain independent of model configuration.

Required search capabilities:

- Topic keywords, PMID and DOI resolution.
- Publication year, journal, article type and free-full-text filters.
- Relevance and publication-date sorting.
- Multiple queries where appropriate.
- Deduplication by PMID/DOI and reproducible relevance ranking.
- Bounded requests, caching, timeouts, rate-limit handling and recoverable upstream errors.

Expose each publication's available title, authors, journal, year, PMID, DOI, article types, abstract and PubMed link. Separate electronic publication and journal-issue dates. Unknown date types and missing abstracts/metadata must remain explicitly unavailable.

An empty response is not proof of an absence of scientific evidence. Source details must remain inspectable when model generation is unavailable or rejected.

## 5. Research pipeline and persisted evidence

For each research request:

1. Validate and normalize the question.
2. Identify research intent and relevant prior-question context.
3. Construct and execute PubMed queries.
4. Normalize, deduplicate and rank publications.
5. Build bounded source context from available abstracts.
6. Apply the user's current answer-language and detail preferences.
7. Request structured model output when generation is configured.
8. Check source membership, quotations, numerical consistency and claim support.
9. Persist the question, final status, accepted answer or safe failure information, source snapshots and provenance.

Treat user input, abstracts and publication metadata as untrusted data. They must not override model instructions or cause unauthorized actions.

Persist the evidence actually used for each answer. Updating a canonical publication record must not silently alter historical source snapshots. Research retrieval and answer generation must be separately testable.

Deterministic ranking is acceptable; a vector database is not required. Do not claim systematic-review completeness or independent grading of clinical evidence quality.

## 6. Optional provider configuration and operating modes

The application must start and provide authentication, literature retrieval, saved research, conversations and exports without an AI provider.

Support a server-side OpenAI-compatible API configuration, including a Gemini-compatible endpoint and a local Ollama-compatible option. Model identifier, API base, credentials, timeouts and output limits belong in environment configuration.

Provide a documented local configuration workflow with hidden credential entry and a hosted environment-variable procedure. Never expose provider keys in frontend forms, JavaScript assets, URLs, Git history, screenshots, logs or reports.

The preferred hosted provider configuration is an eligible Gemini free-tier project. Do not enable billing, purchase subscriptions, automatically switch to paid models or promise unlimited free use. Local models require suitable hardware. Availability and pricing depend on the operator's actual provider account.

Show these distinct conditions:

| State | Required meaning |
|---|---|
| Unconfigured | A required model/credential/endpoint setting is missing or invalid; literature workflows remain usable. |
| Configured, unchecked | Configuration exists but no successful connectivity check has established readiness. |
| Connection check passed | A bounded provider probe succeeded; this does not guarantee every research answer will succeed. |
| Connection check failed | A safe, actionable provider failure is visible without exposing credentials. |
| Answer generation outcome | The individual answer succeeded, failed, was withheld or has insufficient evidence independently of the connection indicator. |

The composer and settings must both communicate the current limitation. When generation is unavailable, use a literature-search action label rather than imply that a generated answer will be returned.

Provide an authenticated, CSRF-protected connection-check action. The probe is a real provider call, consumes usage allowance and does not establish clinical accuracy.

## 7. Answer language and response detail

Persist answer language, response detail and display density. Offer the configured language choices, Concise/Standard/Detailed responses and Comfortable/Compact display.

Language/detail preferences apply to newly generated responses. Saving a preference must not silently translate an existing answer, source title or abstract.

For Chinese generation:

- Request Chinese explanatory prose for findings, limitations and evidence gaps.
- Check the generated prose rather than assuming the requested language was followed.
- Permit at most one explicit corrective attempt for a wrong-language draft.
- If the correction still fails, withhold the draft and show a language failure.
- Keep original source quotations, titles and abstracts in their source language and label that distinction.
- Do not count a localized UI message as a generated Chinese research answer.

Use an understandable bilingual explanation when Chinese is selected but generation is not available. Source quotations retaining English are not, by themselves, a language-preference failure.

## 8. Citation, numerical and claim-support checks

Every displayed reference must belong to the retrieved source snapshot. Never invent titles, authors, PMIDs, DOIs, quotations, numerical outcomes or study findings.

Before accepting generated content:

1. Validate the structured response and its source identifiers.
2. Verify that every supporting quotation matches the cited abstract.
3. Apply conservative numerical consistency checks against the cited excerpts.
4. Submit the draft to a separate automated claim-support review using the supplied evidence.
5. Reject malformed, unsupported or failed review output.

Review evidence-gap statements as well as positive findings; an unsupported assertion of missing evidence is still a claim.

Separate findings, study limitations, tentative interpretations and insufficient evidence. Do not fill an empty limitations field with unsupported generalizations. Make supporting excerpts and automated-check status inspectable at claim level.

The automated reviewer may use the same configured model. It is **not independent clinical validation** and does not guarantee correctness. Exact-source and numeric checks can reject valid prose or miss semantic errors; preserve human access to the original abstracts.

Rejected drafts must not appear as accepted answers or leak through exports. Keep the underlying sources and safe failure reason available.

## 9. Answer detail and source presentation

An answer has a stable URL and must expose:

- Original question, timestamp, status and available model identity.
- Requested/generated language and relevant check status.
- Accepted findings, limitations and evidence gaps when available.
- Claim-level citations with expandable original-language excerpts.
- Publication cards and an evidence table.
- Copy, save/unsave and export controls.
- A link back to the owning conversation.
- Retrieval provenance and revision information.

The evidence table includes study, year, study type, relevant findings, limitations and source link. Unextracted or unsupported fields must say so. Missing synthesis must not prevent browsing source abstracts.

An outcome with no generated answer must remain clearly differentiated from a completed synthesis, even when bookmarked or exported.

## 10. Regeneration from an existing snapshot

Allow the owner to generate a **new answer revision** from an existing answer's stored evidence using current preferences and current server model configuration.

This action must:

- Be explicit and available only when configuration and stored evidence permit it.
- Reuse the saved source snapshot rather than silently run a different literature search.
- Apply current language/detail settings and all generation checks.
- Create a new answer with its own timestamp, model information, status and provenance.
- Link the new revision to its source answer and identify that evidence was reused.
- Preserve the original answer, evidence, bookmark and audit history unchanged.
- Preserve a failed revision as an honest outcome rather than overwrite the old answer.

A bookmark belongs to a specific answer. Regeneration must not silently redirect it to a new revision.

## 11. Provenance and research context

Separate the following fields in the answer UI and relevant exports:

1. **Original question:** exactly the user's submitted research question.
2. **Normalized question before context:** terminology preprocessing, including mapping method and limitations.
3. **Previous questions available for context:** the prior questions provided to the retrieval/generation process.
4. **Executed PubMed queries:** the actual final queries after topic selection and context expansion.
5. **Retrieval details:** timestamps, per-query PMID results, evidence associations and pipeline identifier.
6. **Generation details:** preference snapshot, model identity, accepted check status and any revision relationship.

Do not label the original follow-up sentence as the executed PubMed query. Counts for separate searches can overlap and must not be misrepresented as unique totals.

A follow-up about “these studies” must retain the relevant research topic. A deliberate new topic must not inherit unrelated terms. Previous model answers are not automatically authoritative evidence.

## 12. Conversations, history and saved research

Persist chronological threads and expose reopening, title changes, search, date sorting and confirmed deletion. Questions, outcomes and source associations must survive reload and sign-out/sign-in.

Provide answer bookmarks, publication bookmarks, publication collections, saved-publication filtering and reusable saved-search parameters.

All save operations must show progress, visible success and recoverable failure. Disable pending or unchanged duplicate saves; re-enable edited forms. Provide separate unsave/remove actions. Enforce per-user deduplication for publications and equivalent searches.

Clearing a saved-publication filter must restore the list. Deleting a conversation must remove its dependent saved-answer links without removing another user's research or unrelated saved publications.

## 13. Authentication, profile and session behavior

Provide registration, login, logout, profile-name editing and preference persistence using secure password hashing and Django sessions.

Enforce CSRF protection and backend ownership for all private reads and writes. Update the visible signed-in state immediately on logout. Clear private caches, synchronize account changes across tabs and reject stale responses initiated under a different session.

Use application-specific cookie names to avoid local-project conflicts. A sign-in requirement in a separate browser context is not, by itself, proof that a session was lost.

Use synthetic demo identities only. Shared demonstration access, if published, must be clearly identified as shared; do not imply that it provides a private patient workspace.

## 14. Exports and copying

Support copied Markdown, Markdown/PDF answer exports and BibTeX/CSV reference exports.

Answer exports must retain question, status, language where relevant, timestamp, model identity, evidence scope, citations, retrieval provenance and revision relationships. Failed or literature-only answers must not be relabelled as generated syntheses.

Maintain Unicode correctness, readable Chinese/Latin PDF fonts, usable page layout, nonduplicated reference punctuation, valid BibTeX entries and correctly escaped CSV columns. Guard CSV spreadsheet-formula prefixes.

All export routes must enforce ownership. Source excerpts must retain their original language and association with the corresponding publication.

## 15. Architecture, API and data model

Use React, TypeScript, Vite, React Router and TanStack Query for the frontend, and Python, Django and Django REST Framework for the backend.

Use SQLite for local development and PostgreSQL for hosted persistence. Model users, preferences, conversations, answer turns, canonical publications, immutable answer-specific evidence snapshots, saved answers, saved publications/collections and saved searches. Persist relevant query and generation provenance.

Document API operations for authentication, profiles/settings, research submission, conversations, answers, regeneration, publication lookup/search, saved items/searches, exports, model readiness and health.

Validate inputs consistently, sanitize user-facing errors and render untrusted text safely. Credentials and unnecessary research-body content must not appear in logs.

Upgrades must preserve existing users, research and snapshots. Back up local data before migration and prefer additive schema changes. Do not upload local private data to a hosted instance implicitly.

## 16. Local startup and public deployment

Provide project-relative Windows setup/start/stop scripts and manual setup commands for other supported systems. Detect dependency, working-directory and port problems; verify readiness and stop only launcher-owned processes.

Provide a production frontend build and Docker deployment configuration. Distinguish these delivery stages:

- A container image built successfully.
- A deployment package verified against disposable services.
- A real public website verified over HTTPS.

For the public test environment, serve the complete frontend and Django API on Render with persistent PostgreSQL, using Neon for the selected free database setup. Users must be able to visit from another computer without running the owner's local servers.

The hosted configuration must:

- Use production security settings, trusted hosts/origins and private environment variables.
- Persist accounts, sessions and research outside an ephemeral web-service filesystem.
- Run required migrations and expose a useful health endpoint.
- Support public login, literature retrieval, saved research and conversations.
- Document the actual public URL only after verification.
- Explain idle sleep, wake-up delay and provider quotas.
- State the actual database expiration policy; do not confuse a quota-reset date with deletion.
- Avoid unauthorized paid upgrades or automatic recharge.

Maintain a separate self-managed deployment option where applicable, using PostgreSQL and shared caching such as Redis. Choose worker/cache settings consistent with the service profile. A configured deployment file is not proof of a live service.

## 17. Usage controls and safety

Apply appropriate authentication, research, literature and model-check rate limits. Bound model context, output and request duration.

Account for each provider operation: a draft, claim review, connection probe and corrective language attempt can consume separate calls. Use a shared allowance appropriate to the deployment; creating a new user must not bypass a global provider allowance. Do not silently fall back to paid services when the free quota is exhausted.

A request-count limit is not an exact provider-invoice guarantee. Document cache/restart behavior and provider-account limits honestly. Application-provider usage is separate from any paid native-CUA evaluation budget.

No real patient data, fabricated evidence, regulatory-compliance claim or automated clinical action belongs in the demonstration. Preserve the research disclaimer and treat retrieved text as untrusted throughout the pipeline.

## 18. Responsive and accessible interaction

Provide clear labels, keyboard-operable controls, visible focus, meaningful status messages and readable layouts on desktop and narrow screens.

Mobile navigation must remain scrollable, expose Profile and all research destinations, support a visible close control and Escape, and manage focus sensibly. Evidence tables may scroll horizontally inside their own container; the page must not overflow.

Save feedback, mode information, language limitations and provider errors must remain visible and understandable on mobile.

## 19. Acceptance conditions

The following conditions define product acceptance. They do not report completed tests.

| ID | Scenario | Acceptance condition |
|---|---|---|
| V3-A01 | Startup without a model | Accounts, literature retrieval, history and saves work; no generated answer is implied. |
| V3-A02 | Authentication and ownership | Login persists, logout clears private state, and another account cannot read/change/export private objects. |
| V3-A03 | Input handling | Short English/supported Chinese questions submit; whitespace, duplicate pending requests and IME Enter are handled correctly. |
| V3-A04 | Real source lookup | A known PMID/DOI resolves through PubMed with inspectable metadata, dates and abstract. |
| V3-A05 | Filters and external failures | Filters apply consistently; empty, missing-data, timeout and quota conditions have honest recoverable states. |
| V3-A06 | Configuration visibility | Missing configuration, unchecked configuration, connection success and connection failure are distinguishable. |
| V3-A07 | Server-only credentials | No provider key appears in the frontend, repository, screenshot, export or user-facing error. |
| V3-A08 | Chinese while unconfigured | Settings and composer explain that the preference cannot produce Chinese synthesis without a working model. |
| V3-A09 | Live Chinese synthesis | With an eligible working provider, accepted generated prose is Chinese and supporting quotations retain their source language. |
| V3-A10 | Wrong-language draft | One corrective attempt is permitted; a still-invalid draft is withheld with a clear status. |
| V3-A11 | Citation and claim checks | Invalid PMID, altered quotation, unsupported number or rejected claim review prevents acceptance of the draft. |
| V3-A12 | Evidence gaps | Findings, limitations and gaps are distinct; unsupported missing-evidence assertions are not silently accepted. |
| V3-A13 | Regenerate with new preferences | A new owner-scoped answer uses the same source snapshot and current preferences; the original answer/bookmark remains unchanged. |
| V3-A14 | Revision failure | Failed generation does not overwrite or falsely upgrade an earlier answer. |
| V3-A15 | Context and provenance | A limitations follow-up remains in the same topic/thread, and normalization, prior questions and executed queries are distinct. |
| V3-A16 | Topic change | New research intent can retrieve different evidence without inheriting unrelated prior-topic constraints. |
| V3-A17 | Save lifecycle | Visible save progress/success/error, duplicate prevention, editing and removal work for answers, publications and forms. |
| V3-A18 | Organization and history | Collections, saved searches, filtering, renaming, sorting, reopening and confirmed deletion persist correctly. |
| V3-A19 | Export fidelity | Formats retain status, source identity and provenance; answer exports retain revision context and readable Unicode. |
| V3-A20 | Mobile/keyboard workflow | Navigation and all research actions remain reachable; evidence tables stay within their container. |
| V3-A21 | Provider failure and allowance | Errors do not erase sources; limits apply across users; no unauthorized paid fallback occurs. |
| V3-A22 | Database upgrade | Existing users, research, saved items and evidence snapshots survive migration. |
| V3-A23 | Public hosting | The real HTTPS site works from another client, with PostgreSQL-backed sessions and saved data. |
| V3-A24 | Hosting claims | Free-tier constraints, actual expiry policy and verification stage are documented without claiming guaranteed uptime. |

## 20. Verification and delivery requirements

Run backend tests, frontend component tests, production build/type checking, Django/schema/migration checks and desktop/mobile browser tests. Verify the production container with disposable PostgreSQL and applicable cache services. Verify a public deployment separately against its actual URL.

Keep deterministic fixtures, real PubMed checks, real model generation, manual acceptance and native-CUA evaluation distinct. Passing a mocked model test does not establish live Chinese generation or supported clinical claims.

Live generation acceptance needs working credentials and human inspection of claim/source support. If unavailable or rejected, record the limitation rather than fabricate output or weaken the checks. Missing prerequisites and unexecuted cases must not be counted as successful execution.

Deliver complete source, configuration examples, migration/startup instructions, API documentation, this standalone requirements document, deployment instructions and separate result/evidence records. Preserve prior data, prompts as historical records, experiment artifacts and release tags. Do not rewrite the frozen independent native-CUA test suite or infer its completion from development tests.

**Evaluation records, separate from these requirements:** [Version 3 results](results.md) and [hosted verification](hosting-status.md).
