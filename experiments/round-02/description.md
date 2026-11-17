# MedEvidence AI 2.0 — Complete Product Requirements

**Version:** 2.0

**Repository:** KateK77/openevidence-clone

**Release reference:** v2.0.0-r2

**Document type:** Standalone product and system requirements

This document defines the complete requirements for MedEvidence AI 2.0. It includes the full research workflow, interface behavior, data model, operational requirements and acceptance conditions. It can be read without earlier prompts, feedback logs or another version's description. Requirements describe intended behavior; they are not evidence that a feature has passed testing.

## 1. Product purpose and boundaries

MedEvidence AI is an independent biomedical literature and clinical research workspace. Researchers and healthcare professionals use it to find publications, inspect abstracts, request optional evidence-grounded synthesis, continue a research conversation and organize sources.

The product is inspired by literature-first clinical research tools but uses its own identity. It is not affiliated with OpenEvidence and must not copy proprietary branding or restricted content.

Display **“RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.”** throughout the workspace and in answer exports. The application must not present generated text as validated medical advice, diagnose patients, automate clinical decisions or claim regulatory certification.

The research workflow uses real PubMed retrieval. Source material is limited to available metadata and abstracts unless additional material is legally accessible and its use is explicitly identified. The application must not imply that it reviewed unavailable full text. Synthetic examples and mocked test responses must be visibly distinguished from real literature and live generation.

All repository descriptions, requirements, reports and installation documentation are in English. Research questions and generated answers may use supported languages.

## 2. Users and access model

The application supports anonymous visitors and authenticated research users.

- Visitors can see the product introduction, research disclaimer and account entry points.
- Users can register, sign in, sign out, maintain their profile and save research preferences.
- Each user owns their conversations, answer bookmarks, saved publications, collections and saved searches.
- An authenticated session is required for private workspace operations.
- Ownership is enforced by the backend for direct URLs, API requests, updates, deletion and exports. Hiding a navigation link is not authorization.
- Seeded users and sample conversations are synthetic. The application must not require real patient information.

Passwords use secure hashing. Authentication uses Django sessions with CSRF protection. The username is stable; profile editing supports first and last names.

## 3. Information architecture and interface

Provide a responsive React interface with a restrained research-oriented visual identity, clear typography and accessible controls.

| Destination | Required content and actions |
|---|---|
| Ask AI / research home | Introduction, multiline question input, topic examples, recent conversations and submission status |
| Research history | Conversation list, search, date sorting, reopening, renaming and deletion |
| Conversation | Chronological questions and answers, source access and a follow-up composer |
| Answer details | Question, answer status, synthesis when available, evidence, citations, provenance, copy, save and export |
| Search PubMed / evidence library | Search by topic or identifier, filters, article details and publication saving |
| Saved publications | Saved reading list, filtering, removal and collection editing |
| Saved answers | Answer bookmarks with links to the original answer |
| Settings | Answer-language, detail-level and display-density preferences; model availability information |
| Profile | Account identity, editable names and sign out |

Saved answers and saved publications must be separate destinations with clear names. Success messages must direct users to the appropriate destination.

Every data view needs a loading state, an understandable failure state and an empty state. Empty search results must not be presented as proof that scientific evidence does not exist.

On narrow screens, navigation must open and close reliably, remain scrollable and expose every account/workspace destination. Support keyboard focus, a visible close control and Escape. Wide evidence tables must scroll within their container rather than create page-wide overflow.

## 4. Question input and submission

The composer must:

- Accept trimmed, nonempty questions from 1 to 2,000 characters, including a single English keyword or short Chinese input.
- Reject whitespace-only input and prevent submission while a request is pending.
- Support multiline text; Enter submits when appropriate, Shift+Enter inserts a newline, and Enter during IME composition must not submit.
- Display pending progress while retrieval or generation runs. Streaming is optional; a visible non-streaming loading state is required.
- Preserve a usable recovery path after validation, network or provider failure.
- Require sign-in before creating private research data.

Chinese query support uses a bounded medical terminology mapping. Supported terms must be normalized to English biomedical search terms with the transformation recorded. Unrecognized Chinese input must produce an actionable mapping limitation instead of silently claiming that no publications exist. This mapping is not unrestricted medical translation.

## 5. PubMed search and source inspection

Use the official NCBI E-utilities interfaces: ESearch for identifiers, ESummary where needed for record resolution, and EFetch for metadata and abstracts. Do not substitute hardcoded research results or bypass publisher access restrictions.

Support:

- Topic keywords, PMID lookup and DOI lookup.
- Publication year, journal, article-type and free-full-text filters.
- Clinical trial, randomized controlled trial, review, systematic review and meta-analysis categories where available.
- Relevance and publication-date ordering.
- More than one search query when useful for a research question.
- Deduplication by stable publication identifiers and deterministic relevance ranking.
- Cached retrieval, bounded requests, timeouts and rate-limit handling.

A source record must expose its PMID, title, available authors, journal, publication year/date, article types, abstract, DOI when available and original PubMed URL. Missing metadata must be labelled unavailable, not invented.

Electronic publication dates and journal-issue dates must have separate labels. Older snapshots without a known date type must say that the type is unavailable.

The interface must handle an invalid identifier, absent abstract, partial metadata, no results, upstream throttling and service failure without losing existing saved research.

## 6. Retrieval-augmented answer pipeline

Keep retrieval, generation and validation independently testable.

For each question:

1. Validate input and identify the research intent.
2. Normalize supported query terminology and select relevant conversation context.
3. Construct and execute biomedical search queries.
4. Normalize and deduplicate publications, then rank the candidates.
5. Build a bounded prompt from source abstracts and relevant prior questions.
6. Request structured output from an optionally configured compatible model.
7. Validate source identifiers and quoted excerpts.
8. Persist the question, outcome, sources, model information and retrieval provenance.

External article text and user-supplied material are untrusted data. They must not override application instructions or initiate unauthorized actions.

Each displayed citation must refer to a publication retrieved for that answer. Quoted support must match the corresponding abstract. Publication titles, authors, PMIDs, DOIs, quotations and study findings must never be fabricated.

Separate supported findings, tentative or conflicting interpretations, limitations and evidence gaps. A field without extracted support must remain explicitly unavailable.

**Version 2 verification boundary:** PMID membership and exact excerpt matching establish source traceability; they do not independently prove that a clinical interpretation follows from a quotation. The interface and documentation must not describe those checks as clinical validation.

## 7. Model configuration and unavailable-generation behavior

Configure model identity, compatible API base URL and credentials on the server through environment variables. Keys must not be entered into an insecure frontend form, included in the bundle, committed to Git or exposed in logs/reports.

The application must start without a model key. Authentication, PubMed retrieval, history, saved research and exports must continue to operate independently of AI availability.

When generation is unconfigured or fails:

- Display a labelled literature-only or generation-unavailable outcome.
- Retain and expose successfully retrieved sources.
- Do not display a canned answer or label a retrieval result as a completed synthesis.
- Explain that a saved answer-language preference does not translate source abstracts or activate a missing model.

Language and response-detail preferences apply to new generation requests. Existing stored answers are not silently rewritten.

## 8. Answer details, citations and provenance

Each answer has a stable detail URL. Show the original question, timestamp, status, available model identity, generated sections, sources and evidence scope.

Support both publication cards and a structured evidence table containing study, year, study type, relevant findings, limitations and source link. Users must be able to expand original abstracts and follow DOI/PMID links.

Persist and expose the relationship among the question, retrieval queries, retrieved publications and answer. Store the retrieval time and source snapshot used by that answer. Later publication updates must not silently rewrite historical evidence.

Provide copy, save/unsave and export actions. A failed or literature-only answer may be saved, but its status must remain visible.

## 9. Conversations and research history

Persist chronological conversation threads with questions, outcomes and answer-to-source associations.

Users must be able to reopen, search, sort, rename and delete their own conversations. Deletion requires an explicit confirmation and must remove dependent answer bookmarks without deleting another user's data.

Follow-up retrieval must retain relevant topic context. For example, “What are the limitations of these studies?” within a GLP-1/obesity conversation must remain related to that topic. A deliberate topic change must not be forced into the previous topic. Earlier generated claims are context, not established facts.

Conversations and bookmarks must survive reload and sign-out/sign-in.

## 10. Saved research and save feedback

Provide publication bookmarking, answer bookmarking, named publication collections and reusable saved search filters.

For every save operation:

- Show progress during submission.
- Confirm success visibly through a Saved state or clear success message.
- Prevent duplicate submissions while pending and while the persisted value remains unchanged.
- Re-enable saving when a form value changes.
- Keep an explicit remove/unsave action separate from the disabled Saved control.
- Show failures and retain the user's edits for an intentional retry.

Saved-publication filtering must match useful identifiers and metadata, including title, author, PMID and collection. Clearing the filter restores the full saved list. Saving the same article or normalized search repeatedly must not create duplicates for that user.

## 11. Preferences, sessions and account transitions

Persist answer language, response detail and display density. Support the offered language choices, Concise/Standard/Detailed responses and Comfortable/Compact layout.

Profile and settings saves use the same progress, success, unchanged-state and error behavior as other forms.

Logout must immediately update the visible account state and clear private query caches. An already-anonymous logout must be handled safely. Account changes must propagate across browser tabs. Requests started before an account change must not repopulate the interface with another account's data.

Use application-specific cookie names to avoid conflicts with unrelated local Django projects. A one-time sign-in after a cookie-name migration is acceptable; deleting existing users or research is not.

## 12. Exports

Support copying answer Markdown, exporting answers as Markdown/PDF and exporting references as BibTeX/CSV.

Exports must preserve question, status, timestamp, available model identity, evidence scope, references and source traceability. Literature-only exports must not imply successful generation.

- Markdown must use correct Unicode.
- PDF must render the supported Chinese and Latin text with appropriate fonts, readable layout and usable page boundaries.
- Reference punctuation must not be duplicated by formatting.
- BibTeX must produce distinct, usable entries with available publication metadata.
- CSV must preserve column boundaries and Unicode and guard spreadsheet-formula prefixes.
- Every export endpoint must enforce ownership.

## 13. Architecture, API and persistence

Use React, TypeScript, Vite, React Router and TanStack Query for the frontend; Python, Django and Django REST Framework for the backend. Use SQLite for local development and a PostgreSQL-compatible relational design for hosted operation. Styling must support the responsive layout without depending on static screenshots.

Relational data must represent users, preferences, conversations, answer turns, publications, answer-specific evidence snapshots, saved answers, saved publications/collections and saved searches. Preserve stable identifiers, timestamps and ownership.

Provide documented API operations for authentication, profiles/settings, question submission, follow-ups, conversations/history, answer details, publication search/details, saves, saved searches, exports and health. Inputs and errors must be consistently validated and must not leak private data.

Upgrades must use additive migrations where practical. Back up local SQLite before migration. Existing users, conversations, bookmarks and evidence snapshots must not be discarded or silently replaced.

## 14. Security and operating requirements

Require CSRF protection, password hashing, server-side authorization, input validation, appropriate request limits and safe rendering of untrusted text. Do not expose internal exception details or credentials. Avoid logging research bodies unnecessarily.

Provide synthetic development data and clearly labelled external-service fixtures. Real retrieval and optional live model checks must be separate from deterministic tests.

Supply reliable project-relative setup/start/stop scripts for Windows and documented manual commands for other supported platforms. Detect missing dependencies and occupied ports, report actionable errors, verify server readiness and stop only processes owned by the launcher. Do not assume that the terminal starts in the correct directory.

Provide environment-variable examples without secrets, API documentation, a production frontend build and installation/troubleshooting instructions. PostgreSQL compatibility does not itself establish that a public deployment has been provisioned.

## 15. Acceptance conditions

These are requirements for evaluation, not recorded test results.

| ID | Scenario | Acceptance condition |
|---|---|---|
| V2-A01 | Install and launch | Documented commands start the API and frontend; wrong paths, missing dependencies and port conflicts produce actionable messages. |
| V2-A02 | Register, login and reload | A synthetic user can authenticate and retain a valid session after refresh. |
| V2-A03 | Logout and switch accounts | Visible state updates immediately; stale responses and another tab cannot expose the previous user's data. |
| V2-A04 | Direct cross-account access | Another user's conversations, answers, saves and exports cannot be read or modified. |
| V2-A05 | Short and multiline input | A single keyword and supported short Chinese question can submit; whitespace and IME composition do not trigger invalid requests. |
| V2-A06 | Chinese mapping | Supported terminology produces traceable English search terms; unsupported terminology explains the limitation. |
| V2-A07 | Known PMID and filters | A real known record, such as PMID 33567185, resolves; matching/nonmatching filters behave consistently. |
| V2-A08 | Source details | Available authors, DOI, abstract and separate electronic/issue dates are inspectable. |
| V2-A09 | Unconfigured or failed model | Sources remain usable, generation status is honest and no fabricated synthesis appears. |
| V2-A10 | Configured synthesis | With a working provider, citations belong to the retrieved snapshot and excerpts match their sources; inadequate support is not invented. |
| V2-A11 | Follow-up and topic change | Relevant context is retained within the same conversation; a changed topic is not incorrectly constrained. |
| V2-A12 | Save and remove | Progress/success/errors are visible, duplicate unchanged saves are disabled and removal persists. |
| V2-A13 | Collections and saved searches | Edits and filters persist; a saved search restores its parameters without duplicating records. |
| V2-A14 | History management | Search, sorting, reopening, renaming and confirmed deletion work for the owner. |
| V2-A15 | Preferences/profile | Edited values persist after refresh; unchanged values cannot be resubmitted unnecessarily. |
| V2-A16 | Export integrity | Markdown/PDF preserve Unicode and provenance; BibTeX/CSV references remain usable and owner-scoped. |
| V2-A17 | Mobile and keyboard use | All navigation destinations and research controls are reachable; wide tables remain contained. |
| V2-A18 | Upgrade and failure recovery | Migration preserves existing research; provider failures do not erase successful retrieval or saved work. |

## 16. Verification and delivery requirements

Run backend tests, frontend component tests, production build/type checks, Django/migration/schema checks and desktop/mobile browser tests. Use deterministic service fixtures for repeatable tests and separately identify real PubMed/model verification.

Record actual outcomes, commands, evidence and remaining limitations in the version's result report. A missing provider credential makes live model acceptance unverified or blocked; it must not be counted as a successful synthesis. Built-in development checks are not the final independent native-CUA benchmark.

Deliver the complete application source, migrations, environment template, setup instructions, API documentation, test definitions and evidence. Preserve prior release tags and data. Version 2's release reference is v2.0.0-r2; documentation revisions must not rewrite that historical tag.

**Evaluation record, separate from these requirements:** [Version 2 results](results.md).
