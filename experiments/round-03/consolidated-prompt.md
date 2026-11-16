# MedEvidence AI 3.0 — complete consolidated project prompt

## Precedence

The current Round 3 instructions below govern this version. Original requirements
and the Round 2 scope follow as preserved baseline reference. Historical commands
to stop after a prior round, prior version numbers and tag names do not override
the authorized Round 3 work. All reports and GitHub documentation are English.

# Round 3 consolidated implementation prompt

## Baseline and authorization

Build MedEvidence AI 3.0 from the original platform requirements in
`../round-01/description.md`, the Round 2 improvements in
`../round-02/description.md`, and the manual acceptance findings below.
This is the consolidated next-round prompt. Earlier instructions to stop after
Round 1 or to record issues without fixes are superseded by the user's explicit
request to implement this new version. Preserve the original prompts and release
tags for comparison. Baseline: `12eb0c0`, tag `v2.0.0-r2`.

All reports, repository documentation and GitHub descriptions must be English.
Chinese application copy and functional inputs are allowed. Preserve existing
accounts, research data, source provenance and successful workflows. Do not
replace live retrieval or generation with fixtures or canned medical answers.

## Manual acceptance evidence

Confirmed passing cases: profile save feedback and reload persistence; immediate
logout; answer bookmark feedback and persistence; follow-up placement and
GLP-1/obesity query context; conversation persistence; rename/history search.
Publication Saved feedback and metadata display have partial evidence only.
Untested or partly observed cases must not be declared passed.

The user selected Chinese but received no Chinese answer. The server was in
literature-only mode with no model configured. This is an unmet acceptance
requirement in the tested environment, not evidence of a model ignoring a prompt.
The language preference notice was insufficiently clear to this user.
A sign-in prompt appeared in another view; session loss was not reproduced or
confirmed and must not be described as a fixed authentication defect.

## Required changes

1. Provide a usable server-side model configuration workflow and an explicit
   connection/Chinese-output check. Support compatible hosted APIs and local
   Ollama. Keep keys out of the browser, logs, source control and reports.
   Do not purchase services or enable billing. Free tiers have provider limits;
   local models have hardware requirements. Never promise unlimited free cloud use.
2. Make the difference between missing configuration, configured-but-unchecked,
   successful connection check, provider failure and per-answer generation clear.
   Show the limitation at the question composer and beside language preferences.
3. Enforce Chinese prose for Chinese answers. Retry a wrong-language response
   once, then expose a clear failure instead of silently accepting English.
   Label source titles, quotations and abstracts as original-language material.
   Distinguish localized application messages from generated research answers.
4. Let the owner generate a new answer from an existing evidence snapshot with
   current preferences after configuring a model. Preserve the prior answer,
   saved state, provenance and evidence snapshot; label the new revision.
5. Validate source membership and exact abstract quotations, add conservative
   numerical consistency checks, and run a separate automated claim-support
   review against cited sources. Reject unsupported output. Do not describe
   another model pass as independent clinical validation or a guarantee.
6. Separate findings, limitations and evidence gaps. Show claim-level source
   excerpts and audit status. Keep unsupported limitations explicitly unavailable.
7. Clarify provenance labels: original question, normalized question before
   context, previous questions used, and actual executed PubMed queries.
   Preserve these distinctions in exports.
8. Preserve and regression-test authentication, ownership, persistence, saves,
   short/Chinese questions, history, exports and responsive interaction.

## Acceptance and delivery

Create a new branch `v3-round-03` and release tag `v3.0.0-r3` only after checks.
Produce consolidated feedback, a traceable change report, test evidence and
manual instructions. Keep automated tests distinct from user acceptance.
If no real model credentials or local model are available, finish the authorized
implementation and explicitly report live Chinese generation as blocked. Never
claim that synthetic model tests prove a live model works. Preserve v1 and v2.

## Provider references

The user selected Gemini Free Tier for this version. Provide a hidden local key
prompt and do not enable billing. The user also requested availability when their
PC is off: prepare persistent hosting configuration, but distinguish a tested
deployment package from an actually provisioned public website. No hosting
subscription or public deployment has been completed as part of local verification.

- Gemini compatible endpoint: https://ai.google.dev/gemini-api/docs/openai
- Gemini free-tier conditions: https://ai.google.dev/gemini-api/docs/billing
- Ollama local compatibility: https://docs.ollama.com/api/openai-compatibility
- Ollama pricing: https://ollama.com/pricing

Consulted November 15, 2026. Provider models, quotas and prices can change.


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


---
# Preserved Round 2 scope

# Round 2 scope

The user authorized a version 2 implementation based on the original platform requirements and the completed manual acceptance feedback. The previous instruction to record defects without fixing them applied to Round 1 acceptance; this round explicitly authorizes implementation.

All reports, GitHub descriptions, and repository documentation must be written in English. Chinese strings appear only as functional test inputs, terminology mappings, and captured application data.

## Baseline

- Repository: KateK77/openevidence-clone (private).
- Original source requirements: ../round-01/description.md.
- Version 1: v0.1.0-r1.
- Baseline before Round 2: 56256603ee3b10ef5bea359a73ea1a23fa4ec517.
- Round 2 branch: v2-round-02.
- Planned version tag: v2.0.0-r2.

## Requested improvements

1. Make logout immediately and consistently update the interface.
2. Retain working account isolation, persistence, literature search, history, and exports.
3. Accept short English and Chinese clinical queries.
4. Improve Chinese retrieval and explain unsupported query mapping.
5. Show unambiguous save progress/success/failure and prevent duplicate saves while unchanged.
6. Clarify saved answers versus saved publications.
7. Correct PDF/Markdown character corruption and repeated reference punctuation.
8. Identify electronic and issue publication dates.
9. Make the mobile navigation and evidence views usable at narrow widths.
10. Provide an easier, reliable startup path after the original directory/npm/port difficulties.
11. Preserve independent round comparison, test the changes, document results, and upload the new version to the private repository.

## Implementation approach

Rebuild the React presentation and interaction layer while preserving and extending the tested Django persistence and retrieval foundation. Use an additive database migration and a backup rather than recreating the user's database. Keep model unavailability transparent. Do not claim clinical validation or successful live model testing without evidence.


---
# Preserved original platform requirements

# CODEX MASTER INSTRUCTION — OPENEVIDENCE-INSPIRED MEDICAL AI PLATFORM

## 0. Read This First

You are an autonomous senior full-stack software engineer, AI engineer, software architect, and QA engineer.

Your task is to build a complete, functional, end-to-end medical AI evidence assistant inspired by OpenEvidence.

This is a real software engineering experiment. You must create the entire application, implement its features, test it, document it, and push the completed first-round implementation to GitHub.

**Do not stop after creating a scaffold, design mockup, project plan, or minimum viable prototype.**

Do not divide implementation into multiple user-facing development phases. Implement the complete specified application during this first generation round.

You may organize your internal coding tasks however you wish, but the expected deliverable is a functioning application.

You have no previous conversation context. Everything necessary for this task is specified below.

Do not assume that other projects, repositories, files, APIs, or credentials already exist.

## 1. Project Identity

Project name: MedEvidence AI

Reference product: https://www.openevidence.com/

GitHub owner: KateK77

Target repository: KateK77/openevidence-clone

Preferred local directory:

D:\AI-Workspace\Personal\openevidence-clone

Repository visibility: PRIVATE

Application type: AI-powered clinical evidence search and medical research assistant.

This application is an independent educational and research prototype. It is not affiliated with OpenEvidence.

Do not copy proprietary branding, logos, source code, or restricted content.

Use an original visual identity.

Display the following disclaimer:

"RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE."

Do not represent generated answers as verified medical advice.

## 2. Experiment Context

This project is one of three independently generated healthcare software applications in an AI software engineering benchmark.

The experiment evaluates:

- Complete software generation ability
- Functional correctness
- Frontend quality
- Backend quality
- API integration
- Database design
- AI/RAG implementation
- Security and error handling
- Automated test performance
- Improvement across development iterations

The experiment allows up to five development rounds.

**This instruction initiates Round 1 only.**

For Round 1:

1. Build the complete application.
2. Run all available validation checks.
3. Save the original requirements.
4. Commit and tag the resulting software.
5. Push the implementation to GitHub.
6. Produce a detailed completion report.
7. Stop and wait for user feedback.

Do not automatically begin Round 2.

Future rounds will refine the existing implementation based on feedback. Preserve the ability to compare every round independently.

## 3. Product Objective

Build a full-stack web application that allows healthcare professionals and biomedical researchers to ask medical questions and receive evidence-grounded answers supported by scientific publications.

The system should support natural-language clinical questions, biomedical literature retrieval, structured evidence synthesis, citation verification, follow-up questions, and research history.

Example user questions:

- What is the current evidence for GLP-1 receptor agonists in obesity treatment?
- What are the differences between SGLT2 inhibitors and GLP-1 receptor agonists in heart failure?
- What studies investigate large language models in clinical documentation?
- What evidence supports the use of RAG in electronic health records?
- What are the limitations of AI-assisted medical diagnosis?

The application should prioritize scientific evidence and transparent source attribution.

## 4. Technology Stack

Use the following preferred technologies:

Frontend:
- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- TanStack Query

Backend:
- Python
- Django
- Django REST Framework

Database:
- PostgreSQL for production
- SQLite for local development

AI:
- OpenAI-compatible LLM API integration
- Configurable model identifier
- Retrieval-augmented generation
- Structured evidence extraction

Literature retrieval:
- NCBI PubMed E-utilities API

Testing:
- pytest / pytest-django
- Vitest
- React Testing Library
- Playwright

You may add dependencies when justified.

Use environment variables for all credentials.

Never commit secrets.

## 5. User Interface

Build a polished, professional medical research application.

Visual design:

- Modern, clean, research-oriented interface
- White and very light gray backgrounds
- Deep blue or teal accents
- Professional typography
- Spacious layout
- Clear information hierarchy
- Responsive desktop and mobile layouts
- Accessible controls
- Consistent loading, error, and empty states

Primary navigation:

- Ask AI
- Research History
- Saved Answers
- Evidence Library
- Settings
- Profile

### Home Page

The homepage should contain:

- Prominent medical question input
- Clear Ask button
- Example research questions
- Recent conversations
- Suggested research topics
- Short platform introduction
- Research-only disclaimer

The question input should support multiline text.

Pressing Enter should submit when appropriate, while Shift+Enter inserts a newline.

## 6. AI Medical Question Answering

Implement a complete medical question-answering workflow.

When a user submits a question:

1. Validate the input.
2. Classify the question or identify its research intent.
3. Generate appropriate biomedical search queries.
4. Retrieve relevant scientific literature.
5. Extract available publication metadata and abstracts.
6. Rank the retrieved evidence.
7. Construct an evidence-grounded model prompt.
8. Generate an answer using the configured LLM.
9. Attach source citations to supported claims.
10. Save the question, response, and source information.

Display:

- User question
- Generated answer
- Key findings
- Supporting evidence
- Important limitations
- References
- Generation status
- Model information, when appropriate

Use streaming responses when practical.

Provide a clear loading state if streaming is unavailable.

### Critical AI Requirements

The AI must not invent publication titles, authors, PMIDs, DOIs, quotations, or study findings.

Every displayed reference must correspond to a retrieved publication.

The system must distinguish between:

- Supported findings
- Tentative or conflicting findings
- Insufficient available evidence

If evidence is inadequate, explicitly say so.

If the LLM is unavailable, display a clear error or a labeled retrieval-only evidence view. Do not display a fake generated answer.

Do not silently use hardcoded medical answers.

## 7. Biomedical Literature Retrieval

Integrate PubMed through official NCBI E-utilities.

Documentation:
https://www.ncbi.nlm.nih.gov/books/NBK25501/

Use:

- ESearch
- ESummary
- EFetch
- ELink, where useful

Support:

- Keyword-based retrieval
- Multiple search queries
- Publication date filters
- Article type filters
- Metadata extraction
- Abstract retrieval
- PMID and DOI resolution
- Source deduplication
- Relevance ranking
- API caching

Build a dedicated literature retrieval service with testable interfaces.

Handle:

- Timeouts
- Rate limits
- Empty responses
- Missing abstracts
- Incomplete metadata
- Invalid publication identifiers
- External service failures

Do not bypass publisher paywalls.

Only use publication full text when access and licensing permit it.

## 8. Retrieval-Augmented Generation

Implement a transparent RAG pipeline.

Required components:

1. Query preprocessing
2. Search query generation
3. PubMed retrieval
4. Document normalization
5. Candidate deduplication
6. Relevance ranking
7. Context construction
8. LLM answer generation
9. Citation mapping
10. Response persistence

Keep retrieval logic separate from generation logic.

Use deterministic or reproducible retrieval ranking where practical.

Each cited publication must include:

- PMID
- Title
- Authors
- Journal
- Publication date
- DOI, if available
- Link to PubMed

The system should allow users to inspect the supporting references.

Never present an abstract-only synthesis as if the system had analyzed an unavailable full-text article.

## 9. Answer Detail Page

Each AI answer should have its own detail page.

Show:

- Original question
- Generated response
- Key takeaways
- Supporting publications
- Evidence limitations
- Timestamp
- Conversation context
- Copy answer button
- Save answer button
- Export option

Allow users to expand references and open the original publication.

Provide a structured evidence table with:

- Study
- Publication year
- Study type, if available
- Relevant findings
- Limitations
- Source link

Unsupported fields must be labeled as unavailable rather than invented.

## 10. Multi-Turn Conversation

Implement persistent conversation threads.

Features:

- Ask follow-up questions
- Maintain relevant conversation context
- Preserve source references
- Display chronological messages
- Rename conversations
- Delete conversations
- Reopen previous conversations

Follow-up answers should incorporate previous discussion when relevant without assuming earlier claims were correct.

The model should retrieve additional evidence when the follow-up question requires it.

## 11. Evidence Library

Create an evidence management interface.

Users should be able to:

- Browse retrieved publications
- View article details
- Save articles
- Remove saved articles
- Search saved articles
- Open original PubMed records
- Organize saved research sources

Each publication should have a stable identifier and should not be duplicated unnecessarily in the database.

## 12. Search and Filtering

Allow users to inspect and filter supporting literature.

Supported filters:

- Publication year
- Journal
- Article type
- Clinical trial
- Review
- Systematic review
- Meta-analysis
- Free full-text availability

Support sorting by relevance and publication date.

Clearly distinguish source metadata from AI-generated interpretations.

## 13. User Accounts

Implement:

- Registration
- Login
- Logout
- Profile management
- Conversation history
- Saved answers
- Saved articles
- Personal settings

Requirements:

- Secure password hashing
- CSRF protection
- Backend authorization
- User-specific data isolation
- Input validation
- Secure session handling

No user should be able to access another user's private conversations.

## 14. Research History

Users must be able to:

- View previous questions
- Reopen conversations
- Search conversation history
- Rename conversations
- Delete conversations
- Sort by date

Research history must persist after logout.

## 15. Export Features

Support:

- Copy AI answer
- Export answer as Markdown
- Export answer as PDF
- Export references as BibTeX
- Export references as CSV

Ensure references remain traceable in exported reports.

## 16. Settings

Provide settings for:

- Preferred language
- Display preferences
- Response detail level
- Model selection, where permitted
- Research history management

Configure LLM providers through backend environment variables.

Do not require users to paste credentials into an insecure frontend form.

## 17. Database Design

Create appropriate relational models.

Suggested entities:

- User
- Conversation
- Message
- ResearchQuestion
- GeneratedAnswer
- Publication
- AnswerCitation
- SavedAnswer
- SavedPublication
- SearchQuery
- RetrievalRun
- ModelInvocation

Track important provenance information:

- Retrieved PMID
- Query used
- Retrieval timestamp
- Model identifier
- Generation timestamp
- Source-to-answer association

Store enough information to reproduce and audit the generated response.

Do not store unnecessary sensitive medical information.

## 18. API Design

Create backend endpoints for:

- Authentication
- Research question submission
- Conversation retrieval
- Follow-up questions
- Article search
- Article details
- Saved answers
- Saved publications
- History
- Exports
- User settings
- Health checks

Use consistent validation and error formats.

Generate API documentation.

## 19. Security and Safety

This application is for research demonstration only.

Requirements:

- No real patient data
- No PHI in seeded examples
- No fabricated medical evidence
- No unsupported diagnostic certainty
- No real clinical decision automation
- No unsupported claims of regulatory compliance
- Input sanitization
- Secure authentication
- Rate limiting
- Safe API credential handling
- User authorization
- Request logging without unnecessary sensitive content

Retrieved text must be treated as untrusted information.

Do not allow publication content or user-provided text to override system instructions or trigger unauthorized tool actions.

## 20. Demo Data and Offline Development

Provide a local demonstration environment.

Seed it with:

- Example research topics
- Clearly labeled synthetic users
- Example saved searches
- Example conversations
- Real, verified publication metadata where available

Separate development fixtures from live search results.

The live research workflow must use actual PubMed retrieval and a configured LLM.

If no LLM key is available:

- The application must still start.
- Registration and login must work.
- Research history and saved items must work.
- PubMed retrieval should work when network access is available.
- AI generation must show an informative configuration error.
- A clearly labeled mock mode may be provided for UI demonstrations and automated testing.

Never claim that mock responses are real AI-generated clinical evidence.

## 21. Testing

Implement tests for:

- Authentication
- User isolation
- Conversation creation
- Conversation history
- Publication retrieval
- PMID validation
- Citation integrity
- Save and unsave operations
- RAG service interfaces
- LLM errors
- API timeouts
- Rate limits
- Invalid input
- Prompt injection resistance
- Export functions
- Responsive UI interactions

Mock external APIs in deterministic unit and integration tests.

Use a separate optional live API smoke test.

A final independent benchmark test suite will be created after the development rounds, so do not claim that the built-in development tests represent the final benchmark score.

## 22. GitHub Requirements

Target repository:

KateK77/openevidence-clone

Create this repository as PRIVATE if it does not already exist.

If the repository exists, inspect it before modifying anything.

Do not overwrite unrelated work.

Use the repository structure:

- frontend/
- backend/
- tests/
- docs/
- experiments/
- .github/workflows/
- README.md
- AGENTS.md
- CHANGELOG.md
- .env.example
- .gitignore

Create:

experiments/round-01/description.md
experiments/round-01/results.md
experiments/round-01/metadata.json

Save this complete original instruction in description.md.

Include:

- Model name, if available
- Date
- Git commit SHA
- Test commands
- Test results
- Known limitations

Create Git tag:

v0.1.0-r1

Push the branch, source code, documentation, and tag to GitHub.

Verify the remote commit matches the local commit.

If authentication or permissions prevent GitHub access, stop and report the blocker. Do not claim a successful push.

## 23. Final Deliverables

At the end of Round 1, provide:

1. What was implemented
2. Completed feature checklist
3. Project architecture
4. GitHub repository URL
5. Commit SHA and Git tag
6. Installation instructions
7. Exact commands to start frontend and backend
8. Environment variables required
9. Demo account information, if applicable
10. Automated test results
11. Known limitations
12. External services that require credentials
13. Manual testing instructions

## 24. Execution Instructions

Start implementing immediately.

Make reasonable engineering decisions without repeatedly asking for confirmation.

Use the entire available coding context to complete the product.

Do not substitute static screenshots or nonfunctional mockups for actual application behavior.

Do not create fake search results in the production research workflow.

Do not start Round 2.

Stop after completing, verifying, documenting, and pushing Round 1.

Wait for my feedback before making further product changes.

**BEGIN ROUND 1: BUILD THE COMPLETE MEDEVIDENCE AI APPLICATION.**

## Authorized public hosting follow-up

The user selected a free public test site with idle suspension and explicitly
confirmed Render My Workspace plus Neon Jiawen Free. Deploy the tested single-
service image from v3-round-03, keep the repository private, preserve other apps,
store records in the separate Neon database, and verify the real public site.
Do not enable paid plans or billing. Keep Gemini credentials server-side and
report missing live AI acceptance separately from successful site deployment.
