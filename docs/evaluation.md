# Evaluation evidence index

Application tests, live browser checks, manual acceptance and native Computer Use API experiments are separate. Fixture success is not evidence of clinically correct generation.

## Portfolio release

[Report](../experiments/portfolio-release/REPORT.md) · [Reference comparison](../experiments/portfolio-release/PLAN.md) · [Public test definitions](../scripts/portfolio_public_smoke.cjs).

| Method | Evidence | Meaning |
|---|---|---|
| Backend pytest | [JUnit](../experiments/portfolio-release/backend-tests.xml) | 62 passed, 1 skipped |
| Vitest | [JUnit](../experiments/portfolio-release/frontend-tests.xml) | 9 component checks passed |
| Playwright regression | [JUnit](../experiments/portfolio-release/browser-tests.xml), [definitions](../frontend/e2e) | 20 desktop/mobile checks; mocked APIs |
| Production container | [Results](../experiments/portfolio-release/hosted-image-smoke.json), [runner](../scripts/portfolio_hosted_smoke.py) | 6 checks against disposable PostgreSQL; no provider calls |
| Public browser | [Per-step report](../experiments/portfolio-release/REPORT.md) | Real deployed UI, PubMed and configured application model |
| Render Blueprint | [Schema validation](../experiments/portfolio-release/blueprint-validation.json) | JSON-schema check, not Render CLI validation |

The public runner assigns difficulty and expected conditions before execution, and records observations, PASS/FAIL/NOT_RUN and per-run screenshots. It uses Playwright locators plus explicitly labelled API assertions. It is **not an AI browser agent or native CUA**. The application model answers questions; it does not operate the browser.

## Frozen native-CUA experiment

[100-case suite and records](https://github.com/KateK77/openevidence-clone/tree/evaluation/medevidence-native-cua-100). Original baseline: `7d64a988fc1b1e27433aa96c90b743c6336baea5`.

- Planned: GPT-5.4, OpenAI native Computer Use API.
- Frozen distribution: **30 Easy, 40 Medium, 20 Hard, 10 Expert**.
- **0 executed, 100 NOT_RUN. No native-CUA pass rate exists.**
- Target $5, absolute maximum $10. Paid execution remains unauthorized and blocked; token estimation alone cannot guarantee an actual invoice ceiling.
- Original requirements, difficulty, acceptance criteria, prerequisite markings and offline evidence remain unchanged on the experiment branch.
- That baseline differs from this release; its offline preflight is not represented as verification of the changed deployment.

The separate [standardized benchmark branch](https://github.com/KateK77/openevidence-clone/tree/benchmark/medevidence-standardized-cua-v1) is preserved too. Its existence does not establish executed results.

## Earlier rounds

| Round | Records |
|---|---|
| 1 | [Description](../experiments/round-01/description.md), [results](../experiments/round-01/results.md), [manual acceptance](../experiments/round-01/manual-acceptance) |
| 2 | [Description](../experiments/round-02/description.md), [results](../experiments/round-02/results.md), [report](../experiments/round-02/report.html) |
| 3 | [Description](../experiments/round-03/description.md), [results](../experiments/round-03/results.md), [public smoke](../experiments/round-03/public-smoke.json), [hosting snapshot](../experiments/round-03/hosting-status.md) |

Historical reports describe their recorded versions and provider state. They are preserved rather than rewritten to match today. Results from MyChart or another project never count as MedEvidence evidence.

## Scoring boundaries

Use passes divided by **executed cases**, with FAIL and NOT_RUN separately visible. Do not combine unit tests and browser journeys into an artificial product accuracy score. Public smoke is not load testing, accessibility certification, clinical validation or comprehensive literature-quality assessment. Preserve failed attempts and explain test-harness corrections. Shared accounts and provider variability can change later outcomes.
