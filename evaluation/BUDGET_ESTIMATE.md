# Budget scenarios — GPT-5.4 native CUA

Target budget: $5 USD. Absolute maximum actual charges: $10 USD. Paid dispatch is blocked because an actual-bill guarantee has not been established.

These are assumption-based forecasts, not measured usage, completed-test counts or pass rates. Every scenario retains all 100 frozen tasks. No caching discount, Batch discount, prepaid credits or automatic top-up is assumed.

## Optimistic

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 2 | 60 | 132,000 | 7,200 | $0.44 |
| Medium | 40 | 4 | 160 | 432,000 | 28,800 | $1.51 |
| Hard | 20 | 7 | 140 | 476,000 | 35,000 | $1.72 |
| Expert | 10 | 11 | 110 | 462,000 | 38,500 | $1.73 |

**100-test forecast: $5.40.**

- $5: 92 full-task attempts forecast; not a predicted pass count.
- $10: 100 full-task attempts forecast; not a predicted pass count.

## Central

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 3 | 90 | 243,000 | 16,200 | $0.85 |
| Medium | 40 | 6 | 240 | 792,000 | 60,000 | $2.88 |
| Hard | 20 | 10 | 200 | 860,000 | 70,000 | $3.20 |
| Expert | 10 | 16 | 160 | 880,000 | 72,000 | $3.28 |

**100-test forecast: $10.21.**

- $5: 49 full-task attempts forecast; not a predicted pass count.
- $10: 99 full-task attempts forecast; not a predicted pass count.

## Conservative

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 5 | 150 | 525,000 | 45,000 | $1.99 |
| Medium | 40 | 9 | 360 | 1,620,000 | 162,000 | $6.48 |
| Hard | 20 | 15 | 300 | 1,800,000 | 180,000 | $7.20 |
| Expert | 10 | 24 | 240 | 1,920,000 | 192,000 | $7.68 |

**100-test forecast: $23.35.**

- $5: 23 full-task attempts forecast; not a predicted pass count.
- $10: 45 full-task attempts forecast; not a predicted pass count.

## What explains the earlier estimates?

The $32.50–110 estimate was located in the different CareConnect-v3 project. It assumed 10–35 million cumulative input tokens and 0.5–1.5 million output tokens. At $2.50/$15 per million, these give exactly $32.50/$110. Its request caps were 30/50/80/120 per difficulty, and it appended the complete screenshot history to every request. Per-action local captures increase storage; only images actually submitted to the API affect tokens. Its desktop capture was up to 1440x1000.

No $3.38 CareFlow EHR usage ledger, model configuration or original estimator was found in the available CareFlow repository. The CareConnect framework is a related patient-portal reference, not proof that the original CareFlow framework has been recovered. A verified task-complexity/request/token/image/model comparison against $3.38 is therefore unavailable. That number must not be called an observed 100-test cost. It could reflect different assumptions, but no explanation is asserted without evidence.

MedEvidence adds live literature, cross-source audits, Chinese synthesis, regeneration and provider-failure prerequisites. This describes its frozen workload, not a proven complexity difference from the missing CareFlow run.

## Optimization without changing tasks

- Exact GPT-5.4 snapshot; standard service tier, low reasoning; output usage includes reasoning tokens.
- 1280x768 desktop and original-resolution 390x844 mobile, device scale 1; no unreadable thumbnail downsampling. Approximate screenshot input: 1,152 / 422 tokens under current 32px patch rules.
- One latest screenshot in each request; retain full original task, criteria, native action transcript and recorded observations. Old screenshots remain in evidence, not in the billed prompt. No previous_response_id chain is claimed to be free.
- Execute model-issued action batches; capture local evidence after each action, reuse the last capture as the batch response, deduplicate identical PNGs by hash. No scripted task solver, paid summarizer or paid judge.
- Request caps 8/14/24/36; action caps 35/70/120/200; these are resource stops, never relaxed acceptance criteria. Exhaustion is an execution error, not an application FAIL.
- Each group of ten scheduled tests contains 3 Easy, 4 Medium, 2 Hard and 1 Expert. Difficult tasks are not pushed to the end merely to maximize inexpensive completions.

## Actual-bill ceiling: execution blocked

The $5 target is a planning target, not authorization. The absolute maximum is $10 of actual charges. The --execute entry point now unconditionally stops before approval/key loading, token counting or HTTP. A config flag or approval JSON cannot bypass it. A reviewed enforceable billing boundary and new explicit user approval are both required to unblock. See BILLING_SAFETY.md.

Local accounting remains defense in depth: reserve uncached counted input with 10% margin, full maximum output and applicable native tool charges before dispatch; retain $0.10 planning headroom; round liabilities upward to microdollars. Persist reservations before sending, allow one request in flight, retain unknown charges on timeout and stop on missing usage or metering discrepancy. Cached usage is settled at its actual cached rate; reasoning is included in output, not charged twice. None of these estimates independently guarantees the actual invoice.

The reviewed pricing table does not separately itemize a local computer-tool fee. Forecast additional tool fee is $0 conditional on confirmation; no hosted container, web search, file search or other billable tool is enabled. An unknown applicable tool rate blocks paid execution. Existing Render/Neon usage is not new CUA tool usage. Any paid application-side LLM cost must be reserved in the same ceiling; the current evaluator disables application LLM calls and blocks live profiles until zero-cost access or a metered allowance is established.

## Feasibility

The central forecast is $10.2105 before any extra fees, already above the $10 absolute maximum; optimistic $5.3975 is above the $5 target, and conservative $23.3475 exceeds both. No valid completion count is guaranteed. The $5/$10 scenario counts assume all prerequisites resolved and represent full task attempts, not passes. Actual dispatch remains zero under the unresolved billing block. Never-executed cases remain NOT_RUN; no paid pilot is approved.

## Request-count scope

Tables count generation requests. The current framework also makes one input-token-count request per generation request (470 / 690 / 1,050 additional requests by scenario); these are not generation retries. Their applicable pricing must be confirmed before execution; no fee is silently assumed away. Only the latest screenshot is submitted, with unchanged task/criteria and all semantic actions/observations. Redundant archive paths, duplicate IDs and timestamps are now omitted from model context. No unmeasured savings are subtracted from the scenario totals.

## Official references checked November 16, 2026

- https://developers.openai.com/api/docs/models/gpt-5.4
- https://developers.openai.com/api/docs/guides/spend-limits
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/guides/images-vision
- https://developers.openai.com/api/docs/guides/conversation-state
- https://developers.openai.com/api/docs/guides/tools-computer-use
