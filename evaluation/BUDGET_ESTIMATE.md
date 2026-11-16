# Budget scenarios — GPT-5.4 native CUA

These are assumption-based forecasts, not measured usage, completed-test counts or pass rates. Every scenario retains all 100 frozen tasks. No caching discount, Batch discount, prepaid credits or automatic top-up is assumed.

## Optimistic

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 2 | 60 | 132,000 | 7,200 | $0.44 |
| Medium | 40 | 4 | 160 | 432,000 | 28,800 | $1.51 |
| Hard | 20 | 7 | 140 | 476,000 | 35,000 | $1.72 |
| Expert | 10 | 11 | 110 | 462,000 | 38,500 | $1.73 |

**100-test forecast: $5.40.**

- $3: 57 full-task attempts forecast; not a predicted pass count.
- $4: 75 full-task attempts forecast; not a predicted pass count.
- $5: 92 full-task attempts forecast; not a predicted pass count.
- $15: 100 full-task attempts forecast; not a predicted pass count.

## Central

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 3 | 90 | 243,000 | 16,200 | $0.85 |
| Medium | 40 | 6 | 240 | 792,000 | 60,000 | $2.88 |
| Hard | 20 | 10 | 200 | 860,000 | 70,000 | $3.20 |
| Expert | 10 | 16 | 160 | 880,000 | 72,000 | $3.28 |

**100-test forecast: $10.21.**

- $3: 29 full-task attempts forecast; not a predicted pass count.
- $4: 39 full-task attempts forecast; not a predicted pass count.
- $5: 49 full-task attempts forecast; not a predicted pass count.
- $15: 100 full-task attempts forecast; not a predicted pass count.

## Conservative

| Difficulty | Tests | Requests/test | Total requests | Input tokens | Output tokens | Token cost |
|---|---:|---:|---:|---:|---:|---:|
| Easy | 30 | 5 | 150 | 525,000 | 45,000 | $1.99 |
| Medium | 40 | 9 | 360 | 1,620,000 | 162,000 | $6.48 |
| Hard | 20 | 15 | 300 | 1,800,000 | 180,000 | $7.20 |
| Expert | 10 | 24 | 240 | 1,920,000 | 192,000 | $7.68 |

**100-test forecast: $23.35.**

- $3: 15 full-task attempts forecast; not a predicted pass count.
- $4: 18 full-task attempts forecast; not a predicted pass count.
- $5: 23 full-task attempts forecast; not a predicted pass count.
- $15: 67 full-task attempts forecast; not a predicted pass count.

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

## Hard ceiling and fee uncertainty

The $3 target is a planning target; only a newly approved amount up to $5 can authorize execution. Reserve counted input with 10% margin, maximum possible output and applicable native-tool fees before every dispatch, retain $0.10 headroom, persist spending and ambiguous-charge reservations, and run one request at a time. No SDK retries, paid reattempts, model fallback or recharge. Unknown billing stops all future calls. Provider-side billing controls remain necessary: a local estimate cannot guarantee the provider invoice if rates or metering change.

The reviewed pricing table does not separately itemize a local computer-tool fee. Forecast additional tool fee is $0 conditional on confirmation; no hosted container, web search, file search or other billable tool is enabled. An unknown applicable tool rate blocks paid execution. Existing Render/Neon usage is not new CUA tool usage. Any paid application-side LLM cost must be reserved in the same ceiling; the current evaluator disables application LLM calls and blocks live profiles until zero-cost access or a metered allowance is established.

## Feasibility

The central forecast is below $15 but above $5; the conservative forecast is above $15. Without a paid pilot there is no empirical basis to promise all 100 under either $3 or $5. The optimistic forecast is a scenario, not a commitment. Prerequisite failures can further reduce valid completion; skipping blocked tests does not prove that 100 tests were affordable. Leave never-executed cases NOT_RUN on a budget stop. No paid pilot is approved now.

## Official references checked November 16, 2026

- https://developers.openai.com/api/docs/models/gpt-5.4
- https://developers.openai.com/api/docs/pricing
- https://developers.openai.com/api/docs/guides/images-vision
- https://developers.openai.com/api/docs/guides/conversation-state
- https://developers.openai.com/api/docs/guides/tools-computer-use
