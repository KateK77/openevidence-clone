# MedEvidence Native CUA Benchmark

**Stage: preparation only. Paid calls: 0. Estimated spend: $0. Native results: 100 NOT_RUN.**

Application freeze: `7d64a988fc1b1e27433aa96c90b743c6336baea5` (V3). Catalog v1.0.1 contains 100 independent spec-based tasks, distributed **10 / 20 / 30 / 25 / 15** across Levels 1–5. GPT-5.4 Responses API with native computer use is the planned actor. The paid runner is disabled and requires new explicit approval.

| Deliverable | Link |
|---|---|
| All 100 test cases | [Readable catalog](catalog-v1/TASKS.md), [JSON](catalog-v1/tasks.json) |
| Requirements and freeze | [Requirement map](catalog-v1/requirements.json), [freeze/hashes](catalog-v1/freeze.json), [authoring clarification](catalog-v1/AUTHORING_REVIEW.json) |
| Evaluation methodology | [Definitions, setup boundary and denominators](METHODOLOGY.md) |
| Offline readiness | [Report](OFFLINE_READINESS.md), [machine-readable checks and task gates](preflight/readiness.json) |
| Budget | [Estimate and comparison](BUDGET.md), [scenario arithmetic](budget.json) |
| Execution/evidence/publication plan | [Plan](EXECUTION_PLAN.md) |
| Per-task results | [Status table](RESULTS.md), [JSON with every assertion](results.json) |
| Results CSV | [Download](results.csv) |
| Screenshots | [Native evidence status](screenshots/README.md), [separate offline captures](preflight/) |
| Action traces | [Native evidence status](logs/README.md) |
| Evidence manifest | [SHA-256 preparation manifest](EVIDENCE_MANIFEST.json) |

Central estimate for unchanged tasks: **$13.30**, with scenarios **$8.68–$23.68**. The project limit remains **$5**. Under central assumptions and the fixed stratified order, $4/$5 could cover roughly 35/39 tasks before reserve effects, provided all prerequisites were ready. No full-run promise is made.

Free checks passed: **12 environment checks, 15 harness unit checks, TypeScript and frontend build**. These do not constitute a native success rate. **37 tasks have baseline fixture support; 63 retain explicit prerequisite gates.** Full native execution is not ready or authorized. Do not change task requirements to fit the budget.

The PR adds benchmark assets only. It does not change application behavior, merge V3 into main, deploy a new release, or alter repository visibility. Native scores will be published only after genuine execution and independent review, with partial coverage and blockers clearly disclosed.
