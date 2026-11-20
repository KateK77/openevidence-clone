# MedEvidence AI 3.0 — Independent Frozen CUA Acceptance Benchmark

**Source:** uploaded final `MedEvidence AI 3.0 — Complete Product Requirements` (same substantive text as repository `experiments/round-03/description.md`).

**Independent design:** **365 distinct hand-authored core scenarios / 473 genuine CUA execution definitions**. Not imported, adapted, or regenerated from the repository's two historical 100-test CUA branches.

**Initial status:** 473 `NOT_RUN`; **PASS rate N/A**. No actual browser test, provider call or app modification occurred during test design.

**Frozen canonical SHA-256:** `00cb1fb76cc7eeede32e0514c69e75cfc81a06f53bd94a5e65bcf26d945b5e13` (sorted compact UTF-8 JSON representation of `all_tests.json` → `tests`).

**Uploaded Description SHA-256:** `91df4cd29312aad57d12e052c5f07cc1727d9f7d83b5a33ce8e5213a38cbc8e9`.

## Design principles

1. Preserve every precondition, named step, expected UI result and strict PASS criterion after freeze. No cherry-picking or lowering difficulty.
2. A core scenario tests a distinct user goal with its own outcome; a second execution ID is allowed only for a materially different viewport or real keyboard-only action. Count both core and variant coverage separately.
3. Use genuine visual **Google Chrome CUA** for every scored step (screenshots, clicks, type, scroll, navigation). Never substitute Playwright, Selenium, DOM scripting, API calls, or unit tests for a CUA PASS.
4. Use synthetic accounts and isolated test state. Existing documented fixture setup is permitted before scored UI actions, but **never change or repair the app** during evaluation.
5. Real PubMed and real provider synthesis require a real reachable service. Controlled fault fixtures support failure-handling tests, not claims of live generation. If unavailable, mark attempted tests BLOCKED with reasons, or NOT_RUN if untouched.
6. The external provider probe and AI generation can incur fees. **Do not start a paid native CUA API or model operation without a separate explicit approval and budget.**
7. `PASS` only for fully observed expected outcomes, including persistence, sources and exports when required; `FAIL` for observed mismatch; `BLOCKED` for genuine prerequisite/tool/fixture blockage; `NOT_RUN` for untouched cases.

## Contents

- `SOURCE_DESCRIPTION.md`: copy of the authoritative uploaded requirements text.
- `test_cases/all_tests.json`: fully specified, frozen 473 CUA executions.
- `test_cases/all_tests.csv`: human-readable spreadsheet import.
- `test_cases/core_scenarios.json`: 365 distinct user goals.
- `test_cases/suite_manifest.json`: counts, coverage and immutable hash.
- `test_cases/fixture_gate_reference.json` and `reports/fixture_requirements.md`: prerequisites and safe environments.
- `results/all_results.csv`: 473 untouched status rows.
- `reports/requirements_coverage.md`: each V3 acceptance requirement mapped to candidate CUA tests and exclusions.
- `reports/non_cua_boundary.md`: rigorous scope for engineering-only verification.
- `reports/live_summary.*`: generated only from factual result rows.
- `scripts/score_results.py`: validates status rows and scores evidence-based outcomes.
- `CODEX_EXECUTION_PROMPT.md`: direct execution instructions for Work/Codex with permission gates.
- `MedEvidence_3_CUA_Tests_473.xlsx`: five-sheet readable review workbook.

## Pilot and batches

First **10 Test IDs in frozen order** (`ME3-CUA-0001`–`ME3-CUA-0010`). Submit the intact suite to GitHub before starting CUA. Stop and ask permission after the pilot; subsequent batches are **20 ascending unexecuted Test IDs** each. Never repeat completed IDs solely to inflate rates.

## Scoring

- Primary overall PASS rate: `PASS / 473 × 100%`, reported as **N/A** until at least one test receives definitive PASS/FAIL evidence.
- Executed PASS rate: `PASS / (PASS + FAIL) × 100%`, N/A if no definitive outcomes.
- Definitive execution coverage: `(PASS + FAIL) / 473 × 100%`.
- Report BLOCKED and NOT_RUN separately and retain original failed results.

Run from this directory: `python scripts/score_results.py`.
