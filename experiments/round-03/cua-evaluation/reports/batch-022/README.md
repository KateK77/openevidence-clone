# Batch022: ME3-CUA-0411–0430

{'PASS': 5, 'BLOCKED': 15}. Cumulative: {'PASS': 187, 'BLOCKED': 229, 'FAIL': 14, 'NOT_RUN': 43}

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

411 mobile validation,413/414 nonexistent links and recovery,415 harmless literal script-like question/title roundtrip,430 mobile menu open/close PASS. Other cases BLOCKED by missing controlled source/provider/quota, second account or file-viewing fixtures. No cross-user security pass inferred from own-account checks.

## Integrity

Unchanged live SHA c903b65ce3f8f49fe72416ca8948d215a0690a49 verified read-only. No app/test/config changes or paid synthesis. Only synthetic thread22 added; 12 owned conversations now. Canonical screenshots faithfully convert originals;412 initial loading capture excluded;430 viewport transition excluded. BLOCKED evidence is precondition-only.

| Test | Status | Observation |
|---|---|
| [ME3-CUA-0411](../../evidence/ME3-CUA-0411/actions.md) | PASS | At390px actual2001-character submission returns fully readable question length validation. No key, cookie, backend trace or SQL exception visible; message fits viewport. |
| [ME3-CUA-0412](../../evidence/ME3-CUA-0412/actions.md) | BLOCKED | Current unchanged app captured; no controlled publication containing HTML-looking abstract text available. |
| [ME3-CUA-0413](../../evidence/ME3-CUA-0413/actions.md) | PASS | Authenticated nonexistent /answer/999999999 displays No Turn matches the given query, no trace/unrelated answer. Sidebar Research history successfully recovers to owned list. |
| [ME3-CUA-0414](../../evidence/ME3-CUA-0414/actions.md) | PASS | Authenticated /thread/999999999 returns No Conversation matches the given query, no unrelated thread. Visible Research history backlink recovers correctly. |
| [ME3-CUA-0415](../../evidence/ME3-CUA-0415/actions.md) | PASS | Submitted harmless <script>text</script> plus unmappedChinese CUA415 through real UI. Thread22 title/question and reopened History entry preserve literal angle-bracket markup as readable text; no unexpected navigation or visible execution. |
| [ME3-CUA-0416](../../evidence/ME3-CUA-0416/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0417](../../evidence/ME3-CUA-0417/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0418](../../evidence/ME3-CUA-0418/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0419](../../evidence/ME3-CUA-0419/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0420](../../evidence/ME3-CUA-0420/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0421](../../evidence/ME3-CUA-0421/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0422](../../evidence/ME3-CUA-0422/actions.md) | BLOCKED | Precondition-only capture of owned synthetic thread22; required cross-owner/controlled fixture workflow unavailable. |
| [ME3-CUA-0423](../../evidence/ME3-CUA-0423/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0424](../../evidence/ME3-CUA-0424/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0425](../../evidence/ME3-CUA-0425/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0426](../../evidence/ME3-CUA-0426/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0427](../../evidence/ME3-CUA-0427/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0428](../../evidence/ME3-CUA-0428/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0429](../../evidence/ME3-CUA-0429/actions.md) | BLOCKED | Precondition-only view of owned synthetic thread22; required fixture-dependent workflow not executed. |
| [ME3-CUA-0430](../../evidence/ME3-CUA-0430/actions.md) | PASS | At390x844 menu opens showing all primary/Settings/Profile destinations and visible Close; Close dismisses overlay leaving thread22 readable with no page-wide horizontal clipping. |

Next automatic batch431–450.
