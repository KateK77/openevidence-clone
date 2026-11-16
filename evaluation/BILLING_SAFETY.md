# Billing boundary review — paid execution paused

Updated November 16, 2026. **Target: $5 USD. Absolute actual-charge maximum: $10 USD. GPT-5.4; 100 unchanged frozen tests.** This revision authorizes preparation only. No paid approval file has been created and no OpenAI/Gemini requests have been made for this evaluation.

## Decision

**The actual invoice ceiling is not reliably established. Paid execution is disabled.** The runner's `--execute` path calls an unconditional stop before reading credentials or approval files, calling the token-count endpoint, creating a browser or dispatching a generation request. Editing a config flag or setting `approved: true` does not bypass this stop. No billing account settings, purchases, deployments or auto-recharge settings were changed.

The current official [spend-limits documentation](https://developers.openai.com/api/docs/guides/spend-limits) describes organization/project hard limits, but also says enforcement propagates with delay and recorded spending can exceed the configured amount. No numerical maximum overshoot is established there. An alert, dashboard limit or prepaid balance alone therefore does not prove an exact $10 invoice ceiling. This conclusion is not the outdated claim that OpenAI offers only soft alerts.

A $0.10 local cushion is a planning reserve, not a verified upper bound on provider overshoot. The account's applicable billing terms, existing charges, concurrent consumers, delayed metering, applicable taxes/fees and all tool/application-provider charges have not been independently bounded. A smaller dashboard cap cannot be called a guarantee without a documented maximum overrun. No paid pilot is permitted to discover this boundary.

## Defense in depth retained and checked offline

| Exposure | Local treatment | Remaining limit |
|---|---|---|
| Uncached/cached input | Reserve all input at uncached $2.50/M plus 10% metering margin; settle reported cached input at $0.25/M | Published rates and reported usage are not an invoice contract |
| Output/reasoning | Reserve full configured 1,200 output tokens at $15/M; reasoning already included in output usage | A metering discrepancy triggers a stop, not retrospective prevention |
| Native tool charges | Include up to 8 calls at the confirmed applicable unit rate in each reservation | Zero is a forecast assumption only; tool rate/units must be verified |
| Other endpoints/tools | Only native computer generation planned; count endpoint pricing must also be verified | Hosted containers, search, paid judges and paid summaries are not enabled |
| Application Gemini/provider | Disabled in offline evaluator; live profiles blocked until free entitlement or complete shared-budget accounting is verified | A free-tier label or successful earlier probe is not proof of current entitlement |
| In-flight/unknown charges | Single-flight loop and exclusive lock; durable reservation before dispatch; timeout/missing usage retains liability and halts future paid work | Provider may complete a timed-out request; timeout is not cancellation/free usage |
| Restart/resume | Persist ledger and attempted IDs; never reset charges or automatically rerun attempted cases | Unknown prior liabilities must be reconciled before any future release |
| Numeric/error states | Upward microdollar rounding; reject non-finite/negative financial values and malformed cache usage | Local arithmetic is still distinct from actual invoice enforcement |
| Retry/recharge | Zero paid retries, no automatic top-up, no paid model fallback | T080's required application corrective retry must use a free local fault fixture |
| Budget exhaustion | Decline a new reservation before dispatch; untouched cases remain NOT_RUN | An interrupted attempted case is incomplete/ERROR, not a fabricated FAIL |

The ledger covers all evaluation charges, including any earlier attempt, not a fresh $10 allowance per run. An exclusive local lock does not control other machines or API consumers; those must be excluded or included in a separately verified boundary. Unknown applicable fees prevent dispatch rather than being treated as zero.

## Conditions before reconsidering execution

1. Establish an enforceable, documented bound on **total actual charges**, including delayed/in-flight usage, all relevant endpoints/tools, application-provider usage, pre-existing evaluation liabilities and any applicable billing additions. Bind the boundary to the exact dedicated project/key and model configuration; no other consumer can spend outside the reservation system. Reconcile actual billing evidence, not just local token estimates.
2. Resolve or explicitly carry forward the [26 case prerequisites](PREREQUISITE_READINESS.md). Unresolved cases stay NOT_RUN; do not call a partial run completion of all 100 tests.
3. Review and implement that enforceable boundary, then test it without paid API calls. A boolean attestation alone is insufficient. If no such actual-charge guarantee is available, keep the unconditional stop and explain that the requested absolute guarantee cannot currently be met.
4. Obtain fresh explicit user approval referencing the unchanged suite hash, reviewed config hash, requested authorized amount no greater than $10 and resolved billing design. This budget-plan message is not approval to run.

## Evidence and forecast

See [budget scenarios](BUDGET_ESTIMATE.md) for per-difficulty requests/tokens, cached-billing assumptions, additional endpoint requests and fee uncertainty. The central 100-task token forecast is $10.2105 before extra fees; optimistic $5.3975; conservative $23.3475. These estimates do not justify a guarantee.

The free preflight checks the frozen suite, database/browser and actual dispatch stop. All 100 scored results remain NOT_RUN with zero native API calls. No native-call evidence can honestly be produced before a paid run is authorized and feasible.
