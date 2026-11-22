# Batch023: ME3-CUA-0431–0450

{'PASS': 14, 'BLOCKED': 4, 'FAIL': 2}. Cumulative: {'PASS': 201, 'BLOCKED': 233, 'FAIL': 16, 'NOT_RUN': 23}

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

14 PASS /2 FAIL /4 BLOCKED.444/445: Escape fails to dismiss Delete conversation confirmation, reproduced using keyboard-only navigation; Cancel safely exits, no deletion. Keyboard nav/examples/multiline submissions/bookmarks and mobile menu pass.437 evidence-heavy fixture,440/441 registration prerequisites,450 verified export delivery remain BLOCKED.

## Integrity

Live SHA unchanged and verified read-only. No application/frozen-test/configuration changes or paid synthesis. Actual synthetic thread23 and24 created. PMID6373426 collection changed to CUA439 mobile collection;32356626 and33713498 saved (5 publications). All real original captures retained; canonical PNGs choose settled states.444/445 after.png intentionally shows failed Escape before subsequent safe Cancel.446 initial focus overshoot did not save; actual confirmed-focus Enter then list inspection establishes outcome.450 confirms only layout/activation; no file-content claim.

| Test | Status | Observation |
|---|---|
| [ME3-CUA-0431](../../evidence/ME3-CUA-0431/actions.md) | PASS | Tab traverses Skip-content, logo, New research, Ask AI, History, Saved answers, PubMed, Saved publications, Settings, Profile and account control in logical sequence; each has clear green focus outline. |
| [ME3-CUA-0432](../../evidence/ME3-CUA-0432/actions.md) | PASS | Keyboard-only Shift+Tab traverses Profile,Settings,Saved publications,PubMed,Saved answers,History,Ask AI,New research with discernible outline; Enter activates New research. |
| [ME3-CUA-0433](../../evidence/ME3-CUA-0433/actions.md) | PASS | Tab focuses GLP-1 example with visible outline; Enter populates research draft and moves focus to accessible composer without submission. |
| [ME3-CUA-0434](../../evidence/ME3-CUA-0434/actions.md) | PASS | Keyboard-only clearing draft, Tab to examples and Space on SGLT2 example populates correct 57-character question with composer focused; no auto-submit. |
| [ME3-CUA-0435](../../evidence/ME3-CUA-0435/actions.md) | PASS | 390px drawer opens Settings and Profile; preference controls/save and profile fields/save accessible through vertical scroll; no horizontal clipping. No settings changed. |
| [ME3-CUA-0436](../../evidence/ME3-CUA-0436/actions.md) | PASS | 390px inline filters remain within viewport; year2024,typeClinical Trial and sortPublication date adjusted; native selectors close correctly and Search remains visible. Vertical scrolling does not shift page horizontally. |
| [ME3-CUA-0437](../../evidence/ME3-CUA-0437/actions.md) | BLOCKED | Known saved answer18 has one retrieved retracted source; required evidence-heavy saved-answer fixture unavailable. |
| [ME3-CUA-0438](../../evidence/ME3-CUA-0438/actions.md) | PASS | At390px saved PMID6373426 long abstract wraps fully with vertical scrolling; official PMID link opens correct PubMed article; closing source tab returns to intact saved results. |
| [ME3-CUA-0439](../../evidence/ME3-CUA-0439/actions.md) | PASS | 390px collection field/update reachable; PMID6373426 changed to CUA439 mobile collection, success message fully visible and exact value persists after reload; no horizontal clipping. |
| [ME3-CUA-0440](../../evidence/ME3-CUA-0440/actions.md) | BLOCKED | Authenticated synthetic session retained; fresh registration workflow not executed. |
| [ME3-CUA-0441](../../evidence/ME3-CUA-0441/actions.md) | BLOCKED | Current authenticated session captured as precondition only; no keyboard registration executed. |
| [ME3-CUA-0442](../../evidence/ME3-CUA-0442/actions.md) | PASS | Tab reaches composer; Shift+Enter produces visible second line; Enter submits safe unmapped-Chinese question and creates actual thread23 with both lines' text. |
| [ME3-CUA-0443](../../evidence/ME3-CUA-0443/actions.md) | PASS | After setup all in-app actions keyboard-only: Skip-content and Tabs focus composer, Shift+Enter newline, Enter submits and creates thread24 with both input lines. |
| [ME3-CUA-0444](../../evidence/ME3-CUA-0444/actions.md) | FAIL | Enter on focused Delete conversation opens inline confirmation; Escape leaves confirmation and Confirm delete/Cancel controls visible. Thread24 remains intact. |
| [ME3-CUA-0445](../../evidence/ME3-CUA-0445/actions.md) | FAIL | Pure keyboard History→thread24→Delete Enter opens confirmation. Escape leaves it visible; focus remains Delete. No deletion occurred. |
| [ME3-CUA-0446](../../evidence/ME3-CUA-0446/actions.md) | PASS | Keyboard focus visibly reaches Save publication for PMID32356626; Enter saves, feedback/Saved badge appears, keyboard follows View saved publications and exact article exists in list (count4). |
| [ME3-CUA-0447](../../evidence/ME3-CUA-0447/actions.md) | PASS | Keyboard-only after setup: reaches query, retrieves live PMID33713498, tabs to visibly focused Save, Enter saves, keyboard follows reading-list link and exact PMID/title persists in list(count5). |
| [ME3-CUA-0448](../../evidence/ME3-CUA-0448/actions.md) | PASS | At390px Tab focuses menu trigger; Enter opens drawer with Close focused; Escape closes it and visible focus returns to hamburger trigger. |
| [ME3-CUA-0449](../../evidence/ME3-CUA-0449/actions.md) | PASS | Mobile keyboard-only Space opens focused hamburger; Escape closes drawer and returns clearly visible focus to same trigger. |
| [ME3-CUA-0450](../../evidence/ME3-CUA-0450/actions.md) | BLOCKED | 390px saved-answer Export/Markdown controls fully reachable; real activation produces visible Markdown export downloaded notice without clipping. |

Next automatic batch451–470.
