# Execution and evidence plan

## Current gate

Preparation only. `execution_authorized` is false. No approval file has been created; no API key is loaded by offline checks. The $5 cap cannot credibly cover all 100 tasks. Do not run the paid entry point until the user separately approves a clearly described scope and estimate. A partial run may not be advertised as completion of all 100.

The frozen application and catalog are distinct from the mutable execution configuration. Before approval, finalize prerequisite adapters, record their hashes and rerun free readiness checks. This must not change task goals, difficulty or assertions. Any task amendment needs a new catalog version and documented justification.

## Runtime prerequisites

| Mode | Required environment | Current status |
|---|---|---|
| N | Fresh SQLite, synthetic users/history/sources, explicit empty-state variants | Implemented for supported tasks |
| U | Two synthetic owners, known private IDs, session transitions | Basic history/saved-answer/cross-tab setup implemented; collection-ID adapter pending |
| P | Real official PubMed data, verified identifiers, recorded source responses | Gated; external application requests disabled in current configuration |
| G | Real no-paid/local application model with provenance; no successful mock | Gated; no application provider configured or called |
| C | Reviewed controlled transport for timeouts/429/503/delays/language/citation/claim errors | Gated; named fault payloads and trigger timing still require adapter implementation/validation |
| L | Verified legacy-version fixture, original schema/snapshot hashes, migration on a copy | Gated; no invented legacy fixture substituted |
| M | 390×844 browser; all live requirements of its task still apply | Screenshot capture validated; full mobile workflows remain gated |

[readiness.json](preflight/readiness.json) maps every task to current prerequisite support. **37 have baseline fixture support; 63 remain gated.** This is not 37 passes or a claim that all workflows are execution-ready. Complex adapters must preserve task requirements; never downgrade them to the synthetic baseline to spend the remaining budget. Fully preparing these adapters is required before a complete 100-task run can be approved.

For controlled transports, save original/injected payload hashes, trigger conditions and timestamps. Inject only the named upstream failure or delay, never the expected UI result. Real-provider success and recovery stages must still be genuine where specified. For legacy tasks, preserve the historical fixture and migration log. For live tasks, allow only reviewed official source domains and the approved no-paid provider. Never use the public deployment or real user records.

## Free commands

Run from the repository root. Install the application's existing Python requirements plus WhiteNoise and frontend dependencies beforehand. The checked configuration uses a workspace Python environment at `../venv/Scripts/python.exe`, installed Playwright at `frontend/node_modules/playwright/index.mjs` and Windows Edge. Adjust machine paths for other systems before the configuration is approved.

```powershell
node frontend/node_modules/typescript/bin/tsc --noEmit -p frontend/tsconfig.json
# In frontend/: node node_modules/vite/bin/vite.js build
node --test evaluation/harness/test-harness.mjs
node evaluation/harness/native-cua.mjs --config evaluation/config.json
node evaluation/harness/preflight.mjs
python evaluation/harness/manifest.py --verify
```

The native runner defaults to configuration validation only. Preflight starts its own loopback server on port 18493, creates a new synthetic database, and cleans up only its own process. It never imports an OpenAI SDK or sends provider requests. Dependency installation/builds are free tooling, not model evaluation.

## Paid execution, only after later explicit approval

1. Resolve applicable prerequisites, review pricing/model compatibility, recheck the exact application build and fixture manifests, and publish the final execution-config hash. No paid compatibility probe is permitted before approval.
2. Obtain approval specifying catalog hash, configuration hash, requested model, scope and at most $5 **cumulative project** spending. Keep the exact user statement in ignored `evaluation/private/approval.json`; do not generate approval from elapsed time or an earlier general request.
3. Set the approved execution flag/configuration, provide the key privately in the runner process, and run once. The API key must never be in source, screenshots or public traces. The app subprocess strips provider keys and production connections.
4. Execute the predeclared stratified order. Every task gets a fresh database/context. Anonymous tasks remain anonymous; others may use a disclosed pre-created session. Run setup before paid calls so missing prerequisites spend nothing.
5. Per-level request/action ceilings are 6/20, 10/40, 16/70, 22/100 and 32/150; time ceilings 180/300/540/720/1200 seconds. These are ceilings, not shortened task definitions. A hit stops and is adjudicated; no hidden paid retry or continuation.
6. Count the exact proposed request input before each generation; reserve its maximum output cost with a margin in the shared ledger. Stop before exceeding $5. Paid-call failures retain their reservation until reconciled.
7. Stop on unexpected native protocol/reasoning state, safety approval request, missing usage or billing uncertainty. Retain original evidence. Do not silently switch models or fall back to scripted completion.

## Evidence and independent review

The driver preserves original API request/response bodies privately, including requested/returned model, response ID, HTTP request ID when supplied, native `computer_call` item ID and `call_id`, usage and status. The public trace redacts typed values; the private originals remain available for integrity review. Raw HTTP credentials are never saved.

Every action records its type, coordinates/keys and the before/after screenshot SHA-256. Coordinate bounds are checked against the current screenshot. Local screenshots are captured after each action; only the final image in a safe native batch is sent back to the model. Original screenshots are preserved, with exact duplicate bytes sharing one file. Downloads get file hashes. A separate read-only database snapshot excludes passwords and sessions and is never given to the actor.

An independent reviewer must examine every assertion using the trace, images, database and downloaded artifacts. Use `review.mjs --run <private-run-folder> --reviews <review.json>` with assertion IDs, PASS/FAIL/UNVERIFIED, evidence paths/hashes, reviewer identity, outcome and reason. It rejects PASS without complete evidence and rejects a native PASS/FAIL without native API-call evidence. It writes a new reviewed file and does not overwrite the original run.

Before publication, preserve an original manifest privately; create redacted derivatives and record both hashes plus redaction reasons. Review screenshots visually for secrets and sensitive data, not just regex matches. Do not publish synthetic passwords, sessions, provider keys, production URLs containing secrets, or private database files. Screenshot redactions must not cover assertion-relevant content without marking the assertion unverified.

## GitHub publication

The present PR publishes preparation artifacts and explicit NOT_RUN rows only. Keep the repository's current visibility. After genuine execution/review, publish a separate results commit/PR linking all 100 cases, per-task JSON/CSV, redacted screenshot gallery, action traces, methodology and evidence manifest. Original hashes remain auditable. Preserve this preparation commit as the baseline.

README metrics must show overall and per-group/per-level PASS, FAIL, BLOCKED, NOT_RUN; evaluable rate and coverage; API generation versus token-count requests; actions, observed input/cached/output tokens; estimated cost; requested/returned model identities; and categorized failures. Budget/provider/runner blockers must remain visible. Offline results appear in a separate section. Only describe the 100-task benchmark as completed after all required tasks have genuine, reviewable outcomes; a budget-stopped run is explicitly partial.
