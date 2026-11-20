# CODEX / CHATGPT WORK — Execute the INDEPENDENT frozen MedEvidence 3.0 CUA benchmark

**Do not design, regenerate, reorder, rename, weaken, merge or omit any cases. Test authoring is COMPLETE.** This is a different product from MyChart/CareConnect. The target is **MedEvidence AI 3.0**, repository `KateK77/openevidence-clone`, Description `experiments/round-03/description.md`, public demo https://medevidence-ai-v3.onrender.com/ .

## 1. Import and freeze before execution

1. Extract this exact package into `experiments/round-03/cua-evaluation/` of `KateK77/openevidence-clone`. Compare pre-existing files/hashes; **never overwrite an existing frozen evaluation**. Check target branch/release and record the tested Git SHA and deployed URL. The package does not change application code.
2. Read `README.md`, `SOURCE_DESCRIPTION.md`, `test_cases/all_tests.json`, `test_cases/suite_manifest.json`, `reports/fixture_requirements.md` and `reports/non_cua_boundary.md`.
3. Confirm **365 distinct core scenarios and 473 execution IDs** and suite SHA-256 `00cb1fb76cc7eeede32e0514c69e75cfc81a06f53bd94a5e65bcf26d945b5e13`. Verify the uploaded Description matches current GitHub Description (allow only insignificant trailing newline difference; report any substantive difference).
4. Commit and push all frozen definitions and original all-NOT_RUN results **BEFORE** testing. Record commit SHA. Do not commit provider secrets, demo credentials or synthetic private data. Do not rewrite old releases or prior results.

## 2. Mandatory genuine CUA

Open the **actual rendered application in Google Chrome** using a genuine visual Computer Use Agent (screenshots/mouse/keyboard/scroll/navigation). For desktop use 1440x900, mobile 390x844 viewport, keyboard tests must avoid pointer interactions within scored workflow. **Never use Playwright, Selenium, Cypress, DOM scripting, HTTP/API calls, guessed UI states, or simulated actions as substitutes.** Environment setup, fixture creation and result-file processing may use CLI separately, but cannot be counted as CUA PASS.

The public demo can affect other visitors. Prefer an isolated disposable test environment for mutation/fault/role-swapping cases, with real Chrome CUA still performing scored steps. Only use synthetic accounts/queries. Do not change application behavior or repair defects during evaluation. Check each test's named `fixture_gate`; special missing fixtures => BLOCKED with specific reason after attempted setup, never PASS. Real PubMed must be verified as real, and any AI model use must be real when required for scoring. Controlled upstream/provider failures cannot establish live-generation success.

**Do NOT initiate a paid CUA API or paid provider probe/generation without new explicit user approval, model/pricing details and budget.** If genuine CUA unavailable, report limitation and keep unattempted cases NOT_RUN; do not fabricate evidence.

## 3. Pilot exactly first 10

| Test ID | Scenario | Mode |
|---|---|---|
| ME3-CUA-0001 | Independent brand and research-only boundary | desktop_pointer |
| ME3-CUA-0002 | Independent brand and research-only boundary | mobile_pointer |
| ME3-CUA-0003 | Anonymous landing actions | desktop_pointer |
| ME3-CUA-0004 | Anonymous landing actions | mobile_pointer |
| ME3-CUA-0005 | Research home composer discoverability | desktop_pointer |
| ME3-CUA-0006 | Research home composer discoverability | mobile_pointer |
| ME3-CUA-0007 | Primary research routes | desktop_pointer |
| ME3-CUA-0008 | Primary research routes | mobile_pointer |
| ME3-CUA-0009 | Answer details route entry | desktop_pointer |
| ME3-CUA-0010 | Mobile destination exposure | mobile_pointer |

For every attempted ID use its exact ordered steps, expected result, pass criteria and environment. Capture real `evidence/<Test ID>/before.png`, `after.png`, `actions.md` and intermediate screenshots / downloads as required. Record time, model/browser, viewport, tested SHA and observed result in the exact `results/all_results.csv` row.

`PASS`: all required assertions genuinely visible, including persistence, ownership, downloadable/copy results when relevant. `FAIL`: genuinely observed deviation, with reason and evidence. `BLOCKED`: real prerequisite/tool/fixture failure, with reason. `NOT_RUN`: untouched. No toast-only PASS, no historical smoke/unit test substitute.

## 4. Checkpoint

After IDs 0001–0010: run `python scripts/score_results.py`; inspect report; commit/push evidence and statuses; verify remote SHA; summarize PASS, FAIL, BLOCKED, NOT_RUN and both overall/executed rates with coverage. **Stop and ask whether to continue.** For later approvals, each batch contains precisely 20 next unexecuted IDs in ascending ID order; pause after every batch. Never silently overwrite prior outcomes or rerun to improve statistics.

Do not modify or repair the MedEvidence application during evaluation. Do not execute unrelated MyChart tests or legacy MedEvidence 100-task suites.
