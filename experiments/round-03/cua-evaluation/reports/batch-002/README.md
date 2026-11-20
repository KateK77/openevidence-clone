# Batch 002 — ME3-CUA-0011–0030

This batch was actually attempted in Google Chrome visual CUA in frozen order. It was interrupted during 0029 and resumed in the same browser tab. No completed test was rerun. Application commit: `c903b65ce3f8f49fe72416ca8948d215a0690a49`; URL: https://medevidence-ai-v3.onrender.com/ .

## Evidence-loss incident and scoring

Original screenshots for 0011–0028 were displayed and inspected in the conversation, but were held in transient orchestration state rather than written immediately to files. That state, original timestamped action ledger, and the dedicated synthetic account's temporary password were unavailable after resume. This was an evaluator archival failure. It is not an application failure.

The frozen scorer requires actual `before.png` and `after.png` files for both PASS and FAIL. We did not weaken the scorer, create placeholder images, substitute screenshots from other IDs, reconstruct screenshots, or rerun completed tests to replace missing original evidence. Accordingly the formal CSV records 0011–0028 as **BLOCKED due to evidence archival failure**. Their original observed dispositions and concrete findings are preserved in `observation_ledger.json` and each test's `actions.md`; these findings are not erased or counted as fully evidenced outcomes.

| Accounting | PASS | FAIL | BLOCKED |
|---|---:|---:|---:|
| Preserved browser observations, before artifact validation | 16 | 3 | 1 |
| Formal batch results accepted by unchanged scorer | 1 | 0 | 19 |

Formal cumulative results: **11 PASS, 0 FAIL, 19 BLOCKED, 443 NOT_RUN**. Overall pass rate 2.33%; definitive coverage 2.33%; executed pass rate 100% among the 11 fully evidenced definitive cases only. This 100% excludes the three observed mismatches and must not be described as application-wide success.

## Preserved findings requiring original-artifact recovery or separately authorized follow-up

- **0017 observed FAIL:** nonexistent route returned a bare server Not Found page without application navigation/recovery link. The required return using app navigation was impossible.
- **0026 and 0027 observed FAIL against the exact frozen workflow:** the prescribed email/matching-password registration flow did not match the actual Username/Password form, which had no email or confirmation field. No substitute registration was submitted. These are benchmark/UI workflow mismatches, not proof that username registration is broken.
- **0011–0016, 0018–0025, 0028 observed PASS:** actual actions and observed assertions are preserved in the observation ledger, but original image files are missing. Exact original execution timestamps are unavailable and were not invented.
- **0029 BLOCKED:** started on mobile Profile, resumed same account, clicked Sign out; Signing out... remained visible. A later desktop reload showed anonymous login. The correct password was lost with transient state, preventing the prescribed re-login and subsequent account checks. No credential reset or alternate-account substitution was performed.
- **0030 PASS:** submitted the known registered dedicated username with a deliberately incorrect password; observed Invalid username or password and unauthenticated Sign in. Its original screenshots were saved immediately. A supplemental History click produced an immediate/stale screenshot and is not used to claim a resolved History guard.

## Environment and boundaries

Requested CSS viewports: desktop 1440×900, mobile 390×844. Original raster dimensions may differ due to browser screenshot scaling. Temporary malformed/scaled or stale screenshots were not used to establish assertions. Some scroll commands timed out; subsequent screenshots supplied actual visible state. No DOM, Playwright, Selenium, test API or unit-test replacement was used for scored actions.

The dedicated account was created during pilot setup and used for empty-state and correct-login checks. Published synthetic `portfolio_researcher` fixture answer 5 / thread 5 and publication were viewed only; the shared fixture was not exclusively isolated from other visitors. Existing answer state was Generation unavailable and does not establish successful AI synthesis. No provider generation/probe or paid native CUA API was initiated; no accounts were created in this batch; no application code, settings, deployment, shared research data, frozen definitions or pilot outcomes were changed.

Browser family was verified as Chrome by the connected runtime; exact build and controller model/reasoning were not independently exposed. Viewport override was reset, session was anonymous at completion. Recorded recovery timestamps are UTC, not guessed original execution times.

`resumed_action_trace.json` contains exact resumed calls with credential values omitted. `evidence/batch-002-resume/` preserves resumed original JPEGs, including intermediate pending/stale states. PNG evidence is a pixel-preserving conversion of genuine JPEG captures. In 0029, `after.png` still shows pending Signing out... despite the older raw filename `0029_signedout.jpg`; see its capture notes.

The original `SHA256SUMS.txt` remains the frozen import inventory. Mutable results/reports intentionally differ; test definitions and workbook remain unchanged. Original all-NOT_RUN import: `66432c918cc981e3a0e28b21df69ce4ec4ba3347`. Prior pilot commit: `2156a6ab86925965506d3bce619640f6d8da8a12`.

Stop after this 20-ID batch. Next untouched ID: **ME3-CUA-0031**. Do not silently rerun blocked IDs or overwrite the preserved observed failures.
