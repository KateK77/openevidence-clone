# Batch011: ME3-CUA-0191–0210

12 PASS /0 FAIL /8 BLOCKED. Cumulative through210:99 PASS /9 FAIL /102 BLOCKED;263 NOT_RUN.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json)

Language, detail and density options are selectable in desktop/mobile. Chinese persists after save/reload in both viewports; Detailed persists after navigation. Compact visibly reduces saved-answer row height and retains the same item after reload. Chinese preference leaves the real English title/abstract of PMID6373426 unchanged.

Blocked: successful/failed probe fault states191/192; reauthentication193; two-account global quota194; approved actual draft/review usage195; independent no-provider export196; second-account preference isolation208; previously accepted generated answer209. Existing excluded-source answer18 is not accepted AI prose. No credentials were reset and no paid probes/generation were invoked.

## Evidence and integrity

Connected Chrome visual pointer/keyboard checks only. App remains c903b65ce3f8f49fe72416ca8948d215a0690a49, reconfirmed read-only through Render. Application and frozen tests unchanged. All earlier/out-of-batch outcomes preserved. Canonical PNGs faithfully convert original JPEGs without resize/crop/annotation; manifest records dimensions and SHA256. Transient screenshots retained and later settled screenshots govern. BLOCKED captures show real preconditions only. Current synthetic account preferences: Chinese / Detailed / Compact.

## Cases

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0191](../../evidence/ME3-CUA-0191/actions.md) | BLOCKED | Current provider has no successful probe in this account; no controlled failed-generation fixture supplied. |
| [ME3-CUA-0192](../../evidence/ME3-CUA-0192/actions.md) | BLOCKED | An owned saved source-bearing excluded-source result exists, but no test-safe failed model-check endpoint is available. |
| [ME3-CUA-0193](../../evidence/ME3-CUA-0193/actions.md) | BLOCKED | The current synthetic test account is signed in. Same-account reauthentication credential is unavailable in the resumed context; sign-out not performed. |
| [ME3-CUA-0194](../../evidence/ME3-CUA-0194/actions.md) | BLOCKED | Only one authenticated synthetic account and normal shared provider configuration are available. |
| [ME3-CUA-0195](../../evidence/ME3-CUA-0195/actions.md) | BLOCKED | Earlier expanded setup guide states synthesis plus review normally uses two calls and language retry can add one; no approved draft/review generation executed. |
| [ME3-CUA-0196](../../evidence/ME3-CUA-0196/actions.md) | BLOCKED | Available instance is configured; no independent no-model literature-only record exists. |
| [ME3-CUA-0197](../../evidence/ME3-CUA-0197/actions.md) | PASS | Desktop Settings shows Answer language with current English. Opened native selector and chose its next option; Chinese became visible as the draft selection. Both supported values and selected state were directly observed; not saved in this case. |
| [ME3-CUA-0198](../../evidence/ME3-CUA-0198/actions.md) | PASS | At390x844 Answer language selector displayed Chinese draft; opening it and moving up selected English. Label/value remain readable and within viewport. Both supported choices were visibly selectable; original stored English restored without saving. |
| [ME3-CUA-0199](../../evidence/ME3-CUA-0199/actions.md) | PASS | Opened desktop native detail selector. HOME selected Concise; successive Down presses selected Standard then Detailed; further Down stayed Detailed. Exactly the three documented options are selectable, with visible current value. Draft not saved. |
| [ME3-CUA-0200](../../evidence/ME3-CUA-0200/actions.md) | PASS | At390x844 native detail selector offered Concise (HOME), Standard (next), Detailed (next), and remained Detailed on further Down. All labels/values readable and within screen. Returned draft to stored Standard afterward. |
| [ME3-CUA-0201](../../evidence/ME3-CUA-0201/actions.md) | PASS | Desktop Display density visibly offered current Comfortable and selectable Compact. Both names are legible; Compact selected as unsaved draft. |
| [ME3-CUA-0202](../../evidence/ME3-CUA-0202/actions.md) | PASS | At390x844 Display density shows Compact and selecting preceding option shows Comfortable. Label and both selected values are legible within the viewport; restored stored Comfortable without saving. |
| [ME3-CUA-0203](../../evidence/ME3-CUA-0203/actions.md) | PASS | Changed language from English to Chinese and saved; after full Settings reload, Chinese remained selected for the same account. Standard detail and Comfortable density retained. Persistence confirmed beyond the save toast. |
| [ME3-CUA-0204](../../evidence/ME3-CUA-0204/actions.md) | PASS | Prepared a saved English baseline through mobile UI, then selected Chinese, saved and reloaded Settings. Chinese remains selected and configured-language notice uses Chinese. Controls/status remain readable at390x844; no toast-only inference. |
| [ME3-CUA-0205](../../evidence/ME3-CUA-0205/actions.md) | PASS | Selected Detailed, saved, navigated to Research Home and back to Settings. Detailed remains selected and Chinese language unchanged, with no unsaved changes. Persistence verified after route navigation. |
| [ME3-CUA-0206](../../evidence/ME3-CUA-0206/actions.md) | PASS | Captured Comfortable saved-answer row, chose Compact and saved. Reloaded Saved answers: same item remains and row height visibly decreased (about56 to44 screenshot pixels at matching1440x900 capture). Reloaded Settings confirms Compact, Chinese and Detailed retained. No data loss or toast-only inference. |
| [ME3-CUA-0207](../../evidence/ME3-CUA-0207/actions.md) | PASS | Prepared a saved Comfortable baseline at390x844 and captured Saved answers. Selected Compact and saved, then loaded/reloaded the answer list: same row remained and height decreased about48 to42 pixels in matching390x844 captures. Reloaded Settings confirms Compact with Chinese/Detailed retained. Controls/status readable. |
| [ME3-CUA-0208](../../evidence/ME3-CUA-0208/actions.md) | BLOCKED | Account A is now saved Chinese/Detailed/Compact. A second independently authenticated synthetic account and A reauthentication credentials are not available in resumed context. |
| [ME3-CUA-0209](../../evidence/ME3-CUA-0209/actions.md) | BLOCKED | Chinese preference is saved. Owned saved answer18 is an excluded-source system outcome, not a previously accepted generated English answer. |
| [ME3-CUA-0210](../../evidence/ME3-CUA-0210/actions.md) | PASS | With saved Chinese answer preference (capture01), searched real PubMed PMID6373426 and expanded article details. Original English title and complete source abstract remained English; identity PMID6373426 and publication metadata retained. No model generation invoked. |

## Continuation

Next case211; next batch211–230. Automatic uploads every20 remain authorized.
