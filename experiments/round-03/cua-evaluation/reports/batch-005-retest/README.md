# Batch005 retest: ME3-CUA-0071–0090

## Result

8 PASS / 2 FAIL / 10 BLOCKED. Cumulative through90:44 PASS /2 FAIL /44 BLOCKED;383 NOT_RUN. No blocked scenario counts as passed.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace_complete.jsonl) · [Screenshot manifest](screenshot_manifest.json) · [Fixture review](fixture_review.md)

## Scope and provenance

User authorized all frozen tests and direct GitHub checkpoint uploads every20. Prior remote checkpoint c220b5fa575d0a0e51052d2fff4af23f0a2f926c contained only1–70. Prior chat claimed71–90 were done, but artifacts were not present remotely; those historical totals are not used as evidence. This batch retests71–90. Existing1–70 rows and91–473 rows preserved. Application and frozen tests not modified.

Live Render deployment dep-dbtbu4p9aqoc73akvgl0 was read using authorized My Workspace; tested SHA c903b65ce3f8f49fe72416ca8948d215a0690a49. UI interactions used real connected Chrome screenshots and pointer/keyboard; no DOM/Playwright/API assertions. Source inspection bounded no-provider execution only. Exact CUA model and Chrome build are not exposed. Timestamps are UTC; local user date November21,2026.

## Findings

Both86 desktop and87 mobile reproduce one defect: unsupported Chinese term produces a translation-limit body but an Evidence gap badge in both conversation and detail. New conversations /thread/11 and /thread/12 retain reproductions.

74,75,81 legitimately exercise validation using an unmapped Chinese term: empty normalized query bypasses retrieval/model. Actual saved conversations, exact counters and clipboard verification establish trimming,2000-character acceptance and draft recovery. These passes do not assert model generation.

10 blocked cases lack controlled latency/no-provider fixtures or fee authorization. Real PubMed lookup observations for82–85,90 are retained as partial evidence; lookup does not prove research provenance.

## Capture limitations

Raw JPEG screenshots are preserved; before.png/after.png are faithful conversions, with dimensions and hashes in the manifest. Extension sometimes returns scaled375x812 or1425x891 images for requested390x844/1440x900; no pixels were resized. Immediate screenshots can precede UI settlement. Extra captures document settled state, coordinate retargeting and scroll recovery. One early75 capture write exceeded shell argument length; later before_settled capture was saved with chunked writes. Complete in-memory action trace includes that attempted operation; no missing screenshot has been fabricated.

## Cases

| ID | Status | Observation |
|---|---|---|
| [ME3-CUA-0071](../../evidence/ME3-CUA-0071/actions.md) | PASS | Typed diabetes: 8/2,000; appended space-hyphen-space-test, newline and 中文: 18/2,000. Exact counter updates observed. No submission. |
| [ME3-CUA-0072](../../evidence/ME3-CUA-0072/actions.md) | PASS | Activated SGLT2 & heart failure topic. Composer populated 'What evidence supports SGLT2 inhibitors in heart failure?' (57/2,000). Remained unsent on home. |
| [ME3-CUA-0073](../../evidence/ME3-CUA-0073/actions.md) | PASS | At 390x844 activated GLP-1 & weight management. Composer populated 'What is the evidence for GLP-1 receptor agonists in obesity treatment?' without submitting. Draft, action and navigation fit mobile viewport. |
| [ME3-CUA-0074](../../evidence/ME3-CUA-0074/actions.md) | PASS | Submitted '   脊髓空洞症 treatment evidence   ' (30 characters); reopened saved conversation from history. Saved question retained medical terms. Selected/copied its auto-created title through UI: exactly '脊髓空洞症 treatment evidence' (24 characters; no outer spaces). No rename saved. Unsupported terminology safely avoided model generation; this pass concerns trimming only. |
| [ME3-CUA-0075](../../evidence/ME3-CUA-0075/actions.md) | PASS | Pasted exactly 2,000 characters through clipboard; UI counter read 2000/2,000. Submitted and reached persisted research conversation with entire question ending 'foll?' and terminology-limitation outcome, without a length-validation error. No live synthesis claimed. Scroll timeout recovered by fresh screenshot; no submission repeated. |
| [ME3-CUA-0076](../../evidence/ME3-CUA-0076/actions.md) | PASS | Pasted 2,001 characters, counter 2001/2,000. Submission produced 'question: Ensure this field has no more than 2000 characters.' Reopened history: same four pre-existing conversations, no additional research item. |
| [ME3-CUA-0077](../../evidence/ME3-CUA-0077/actions.md) | PASS | At requested 390x844 viewport pasted 2,001 characters and submitted; readable length error shown. Opened Research history and observed same four baseline conversations, no new item. Initial screenshot downscaling/scroll timeout recovered; final history capture is 390x844. No horizontal overflow in settled mobile UI. |
| [ME3-CUA-0078](../../evidence/ME3-CUA-0078/actions.md) | BLOCKED | Inspected unchanged public configured service and reviewed documented fixture/setup options. No controlled-delay fixture is available; did not attempt uncontrolled duplicate provider requests. |
| [ME3-CUA-0079](../../evidence/ME3-CUA-0079/actions.md) | BLOCKED | Prepared valid SGLT2 heart-failure draft on configured public research composer. No submission performed; measurable live retrieval/generation pending stages remain untested. |
| [ME3-CUA-0080](../../evidence/ME3-CUA-0080/actions.md) | BLOCKED | Inspected valid 57-character draft and configured synthesis notice in mobile composer. Did not submit. No pending progress or eventual model outcome claimed. |
| [ME3-CUA-0081](../../evidence/ME3-CUA-0081/actions.md) | PASS | Entered 2,002-character multiline draft; submit rejected with explicit length error. Removed only final X and newline using keyboard; clipboard copy verified remaining 2,000 characters exactly equal original draft, so unrelated text unchanged. Second submission succeeded to a saved research conversation. This validates input recovery, not AI synthesis. |
| [ME3-CUA-0082](../../evidence/ME3-CUA-0082/actions.md) | BLOCKED | Submitted 糖尿病 on Search PubMed; 16 relevant publications returned, original Chinese input retained. Opened first PMID 15137354 and visually matched title and PMID on official PubMed. The lookup page exposes no separate original/normalized/executed-query provenance fields. |
| [ME3-CUA-0083](../../evidence/ME3-CUA-0083/actions.md) | BLOCKED | At mobile viewport entered 糖尿病 and activated Search PubMed. Chinese draft and 16-publication result list retained; full original/normalized/executed-query provenance not exposed by lookup workflow. |
| [ME3-CUA-0084](../../evidence/ME3-CUA-0084/actions.md) | BLOCKED | Partial CUA: submitted '   糖尿病   ' through the real literature search; 16 diabetes publications remain visible. Search UI exposes no original/normalized executed-query provenance. Full research submission was not performed. |
| [ME3-CUA-0085](../../evidence/ME3-CUA-0085/actions.md) | BLOCKED | Actual literature lookup for SGLT2 heart failure returned 16 publications; first visible title Heart Failure With Reduced Ejection Fraction: A Review. Input retained. No normalized/executed-query provenance visible in lookup UI. |
| [ME3-CUA-0086](../../evidence/ME3-CUA-0086/actions.md) | FAIL | Submitted verified unsupported glossary term 脊髓空洞症. New conversation /thread/11 and answer detail visibly label result Evidence gap / 0 PubMed records. Body correctly explains mapping limitation and recommends English medical keywords or PMID; says not evidence that no studies exist. |
| [ME3-CUA-0087](../../evidence/ME3-CUA-0087/actions.md) | FAIL | Mobile-pointer submission of verified unsupported 脊髓空洞症 created /thread/12. Conversation and answer detail show Evidence gap / 0 PubMed records alongside mapping-limitation text and actionable English keywords/PMID guidance. Requested Chrome viewport390x844; tool image375x812 preserved without resizing. |
| [ME3-CUA-0088](../../evidence/ME3-CUA-0088/actions.md) | BLOCKED | Inspected desktop Workspace settings. AI synthesis configured and saved language English are visible. Required deliberately unconfigured independent instance absent; did not alter service configuration or claim unavailable generation. |
| [ME3-CUA-0089](../../evidence/ME3-CUA-0089/actions.md) | BLOCKED | Mobile Workspace settings visibly show AI synthesis configured and English preference. Missing required independent no-provider fixture; no supported-term generation submitted. |
| [ME3-CUA-0090](../../evidence/ME3-CUA-0090/actions.md) | BLOCKED | Actual literature query GLP-1 receptor agonists returned16 publications; first visible title Mechanisms of action and therapeutic applications of GLP-1 and dual GIP/GLP-1 receptor agonists. Original hyphenated input retained, but no normalized-query field in lookup. |

## Continuation

Next frozen item: ME3-CUA-0091. Continue91–110 and upload after20. Keep all473 cases and report blockers honestly.
