# MedEvidence Native CUA Benchmark — methodology v1

This is a **preparation-only** benchmark. The application is frozen at `7d64a988fc1b1e27433aa96c90b743c6336baea5` on `v3-round-03`. The authoritative input is [the final consolidated product description](../experiments/round-03/consolidated-prompt.md). Main still contains an earlier application version; the benchmark PR therefore targets the frozen V3 branch.

## Design and difficulty

The [100 tasks](catalog-v1/TASKS.md) were authored from the final description before implementation inspection. A documented, pre-execution v1.0.1 clarification corrected initial authentication wording and the new-account role; goals, levels and assertions did not change. [Freeze hashes](catalog-v1/freeze.json) and [authoring history](catalog-v1/AUTHORING_REVIEW.json) are retained. No native results have been seen. Future changes require a separately versioned catalog and a reason; never replace this catalog after observing failures.

| Level | Count | Definition applied consistently across projects |
|---|---:|---|
| 1 | 10 | Locate or inspect a simple UI state; minimal navigation |
| 2 | 20 | Short interaction, validation, persistence or one source operation |
| 3 | 30 | Multi-step research, filtering, export or saved-work workflow |
| 4 | 25 | Ownership, concurrency, recovery, provenance or evidence-integrity challenge |
| 5 | 15 | Extended workflow across accounts, research, revisions and/or exports |

These are task-complexity definitions, not post-hoc labels based on success. The same framework can be reused for healthcare projects, with product-specific goals. The reference CareFlow report used a different historical distribution (10/33/27/20/10); do not present these suites as statistically interchangeable or claim identical task difficulty.

## Actor and setup boundary

Use GPT-5.4, OpenAI Responses API, native `computer` tool. The actor receives real browser screenshots, the entire frozen task and disclosed fixture notes. It chooses every task click, keypress, scroll and typed value. Playwright is only the action driver. DOM selectors, JavaScript evaluation, backend calls and database observations cannot enter the actor's context.

Scripts may create a fresh isolated SQLite database, migrate it, create synthetic accounts, seed labelled history/source/answer fixtures and establish a session when login is **not** under test. Login/registration tasks start anonymous; logout starts authenticated. All tasks start at home unless their frozen precondition specifies a known private target. No setup may perform the goal itself. Each task is independent; it cannot depend on another task's output.

The default environment blocks external application requests and clears provider credentials. Synthetic records are not real PubMed retrieval or model synthesis. Real retrieval tasks require official live sources. Real synthesis tasks require a verified no-paid/local application model; the application model is distinct from GPT-5.4, which drives the browser. Controlled fault transports must be labelled and capture exact injected payloads. They may test rejection/recovery but cannot replace successful live-generation requirements.

## Independent adjudication

Every frozen assertion requires a reviewer decision and hashed evidence. Allowed oracles: read-only final database snapshots, screenshot/action chronology, downloaded artifacts, official PubMed records and separately retained provider transcripts. No actor self-report can establish PASS. Reviewers must see evidence of actions the task requires, not just a pre-existing desired state.

- **PASS:** every assertion is independently satisfied by a real native attempt.
- **FAIL:** a real, evaluable attempt leaves at least one required assertion unsatisfied. Distinguish product defects from agent mistakes. An agent's inability to complete a healthy UI is still an end-to-end failure, not a product diagnosis.
- **BLOCKED:** budget, missing fixture/provider, uncertain billing, approval, or runner failure prevents a valid assessment. Limits initially stop as BLOCKED pending review; healthy-environment agent exhaustion is reviewed as FAIL, while budget exhaustion stays BLOCKED.
- **NOT_RUN:** no attempt was scheduled/executed. All 100 currently have this status.

First attempts are immutable; paid retries are disabled. Fixing the runner offline does not create a native pass. A future rerun needs separate approval, version/run identity and budget accounting; retain the original result.

## Reporting denominators

Publish PASS/(PASS+FAIL) with both counts and coverage (PASS+FAIL)/100. Also show all four status counts and PASS/100 as catalog completion, clearly labelled. Budget-blocked tasks are excluded from the evaluable denominator, never silently dropped. An incomplete run is a **partial run**, not a completed 100-task benchmark. Report these same counts and denominators for read/search, write/workflow and each difficulty. Group assignments are frozen per task.

Model response counts, actions, tokens, cost and failure categories come from preserved evidence. Estimated costs are not invoices. Offline Django, scripted API, Playwright smoke and harness checks have separate reports and never contribute to native CUA success rates.

Reference: [CareFlow native CUA report](https://github.com/KateK77/careflow-ehr/blob/docs/public-showcase-cua100/docs/testing/cua100-v1/results.md). API protocol: [official computer-use guide](https://developers.openai.com/api/docs/guides/tools-computer-use).
