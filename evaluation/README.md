# MedEvidence final evaluation — preparation only

**No paid execution is authorized. No OpenAI or Gemini API call was made in this
preparation. All 100 application cases are NOT_RUN.** Offline preflight and harness
unit checks are infrastructure evidence, not native CUA results.

- [Frozen 100 tests](FINAL_TEST_CASES.md) / [JSON](final_test_cases_100.json)
- [Final authoritative Description](FINAL_DESCRIPTION.md) / [hashes](freeze.json)
- [Budget scenarios and comparison](BUDGET_ESTIMATE.md)
- [Execution status and per-case report](FINAL_EVALUATION_REPORT.md)
- [Downloadable HTML showcase](index.html)
- [Offline preflight](logs/offline-preflight.json)
- [26-case prerequisite readiness](PREREQUISITE_READINESS.md) / [JSON](prerequisite-readiness.json)
- [Actual-bill boundary and execution block](BILLING_SAFETY.md)
- [Frozen fixtures specification](FIXTURES.md)

## Specification provenance

The source is `experiments/round-03/consolidated-prompt.md` at application commit
`7d64a988fc1b1e27433aa96c90b743c6336baea5`. It includes the approved V3 Description,
explicitly inherited V2/original functional requirements, and the authorized free
public-hosting follow-up. The copy is byte-identical and frozen; earlier standalone
Descriptions and observed implementation behavior did not set expected results.
Required features remain tests even if absent. Conditional requirements stay
conditional (for example, streaming when practical is not made mandatory).

There was no pre-existing MedEvidence 100-case suite in this workspace. This is
the newly designed suite requested by the user, with 30 Easy / 40 Medium / 20 Hard /
10 Expert tests. It is frozen before any paid execution. A change to tests or
criteria after freezing requires an explicit protocol amendment, not silent edits.

## Free local preparation

From the repository root, using the existing Python environment:

```powershell
& ..\venv\Scripts\python.exe evaluation/budget.py
node --test evaluation/harness/test_core.mjs
node evaluation/harness/preflight.mjs
```

Paths may be supplied using `EVAL_PYTHON`, `EVAL_PLAYWRIGHT_MODULE` and
`EVAL_FRONTEND_DIST`. Defaults reuse the original local Node/Python installation;
no dependencies are installed or upgraded by preflight. A loopback server on
18483 and headless Chromium use fresh synthetic state. Existing app servers,
databases and public deployment are untouched. Preflight refuses an occupied port.

The reused frontend build is recorded by hash and checked against its source
baseline. Live network, Gemini entitlement, native OpenAI request compatibility,
fault fixtures and production restart behavior are not established offline.

## Paid execution gate — do not run now

Target is **$5**; the absolute maximum actual charges are **$10**. The original
100 tests and 30/40/20/10 difficulty distribution are unchanged.

`node evaluation/harness/native-cua.mjs` defaults to check-only. `--execute` is
unconditionally blocked before any HTTP or credential loading: a reliable actual
invoice ceiling has not been established. Local reservations and provider spend
limits with propagation delays are not an exact invoice guarantee. Config flags
and an approval file cannot override this stop. See BILLING_SAFETY.md.

A future reviewed enforcement solution also requires a new explicit user approval,
exact suite/config hashes, model, confirmed applicable tool/endpoint fees and an
approved amount no higher than $10. The sample uses the $5 target and remains
`approved: false`. No approval file or paid pilot is created by this preparation.

The solver is the native Responses `computer` tool; it receives screenshots,
original task/criteria and a text action history. It emits `computer_call.actions`;
the adapter only executes those actions. Scripted selectors appear solely in the
offline infrastructure check, never in the paid task solver. Model-requested
browser shortcuts (address entry, refresh, back and tab switch) are translated by
the browser adapter; the model chooses the address/action. Protocol or tool errors
stop the attempt rather than falling back to model-generated JavaScript.

Raw request/response JSON, response/call IDs, screenshots, action trajectories,
usage and durable fee reservations go to ignored `.private/`. Identical screenshots
share a content hash. An ambiguous charge halts all future paid calls. SDK retries
and automatic reruns are disabled. Do not delete the paid ledger to evade the
cumulative budget. For a later authorized resume, use the same ledger and count
all earlier charges against the same ceiling.

## Scoring and publication

Agent self-reported success is not PASS. Independent reviewers must evaluate every
frozen criterion against screenshots, native action traces and read-only state or
download evidence. Record which evidence supports each criterion. Missing app
features are FAIL; unattempted cases with missing external prerequisites remain NOT_RUN with a prerequisite-blocked reason; CUA navigation,
execution limits and infrastructure failures are ERROR. Budget-stopped unattempted
cases stay NOT_RUN. An interrupted attempted case records its incomplete execution,
not a false application FAIL.

Primary rate is PASS / 100; validly evaluated rate is PASS / (PASS + FAIL), undefined
when no valid cases exist. Report all categories and original difficulty totals.
Incomplete runs must never be called complete evaluations. Offline screenshots
must remain labeled offline, not native API evidence.

Before publishing paid evidence, redact synthetic credentials, cookies and keys,
preserve response/call IDs and usage, and link per-case trace/screenshot manifests.
Only reviewed evidence and criterion-level verdicts enter `final_results_100.json`.
`generate_report.py` builds Markdown, CSV and a standalone HTML report. Commit to
this evaluation branch; do not merge main or enable public Pages/private-data
exposure without separate authorization.

## Framework comparison provenance

The available CareFlow EHR repository contains no native-CUA harness or $3.38
ledger. The related CareConnect-v3 harness was inspected for its freeze, explicit
approval, per-test isolation, durable pre-dispatch reservations and no-retry rules.
Its $32.50–110 forecast is documented, not measured. This MedEvidence adapter uses
headless Chromium infrastructure rather than controlling the user's desktop, and
retains only the newest screenshot in model context while archiving all evidence.
No claim is made that this reproduces the missing CareFlow execution record.
