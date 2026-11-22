# Batch014: ME3-CUA-0251–0270

11 PASS /1 FAIL /8 BLOCKED. Cumulative through270:115 PASS /11 FAIL /144 BLOCKED;203 NOT_RUN.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md) · [Correction audit](corrections.md)

251 FAIL reproduces250 mobile: original question/status visible but creation time only calendar date, no fuller timestamp on hover. Stored full timestamp does exist in copied Markdown; this does not repair the page-display failure.

254 copy passed with visible feedback and actual clipboard artifact.257/258 URL refresh/reopen retained exact answer/source/status and full copied timestamp.257 first copy failed visibly; stale clipboard was explicitly excluded, provisional local pass withdrawn, and actual successful retry completed before final status. See corrections.md; no committed result rewritten.260 explicit unextracted limitations,261 card/table identity,262/263 exact-answer bookmark return,265 source-original language,266 honest missing abstract,267/268 correct owning-conversation backlink passed.

266 fixture prepared through normal CUA: real PMID33551565 has no abstract; bare query1/quoted query0 verified. Fixed-code read-only cost review established no_abstracts return before model invocation. Created owned thread17/answer19, no AI generation. Scored actions13 onward inspect actual answer card/table fallback. Existing answer18 remains saved;19 remains unsaved; preferences Chinese/Detailed/Compact.

252/253 lack specific literature-only outcome;255/256 require multiple-source stored answer (available answers each have one);259/264 require independent no-provider mode;269 requires controlled generation failure;270 requires multiple long claim excerpts, not only a long raw source abstract. All BLOCKED with specific reasons.

## Integrity

Connected Chrome screenshots/pointer/keyboard only. Tested/live SHA c903b65ce3f8f49fe72416ca8948d215a0690a49 reconfirmed read-only via Render. No app/frozen-test/configuration edits or paid model calls. Original JPEGs retained and canonical PNGs faithfully converted without resize/crop/annotation; manifest records dimensions/SHA256. Copied Markdown artifacts retained for254/257/258. Missing fixtures are not product failures. Prior outcomes preserved.

## Cases

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0251](../../evidence/ME3-CUA-0251/actions.md) | FAIL | At390x844 original question32356626 and recorded Evidence gap outcome are readable. Creation information remains date-only Nov21,2026; hover adds no time. No clipped essential controls observed. |
| [ME3-CUA-0252](../../evidence/ME3-CUA-0252/actions.md) | BLOCKED | Current stored result18 is excluded-source Evidence gap, not a recorded literature-only outcome. Its abstract was inspected elsewhere but cannot establish this specific precondition. |
| [ME3-CUA-0253](../../evidence/ME3-CUA-0253/actions.md) | BLOCKED | Mobile current stored outcome18 is Evidence gap with excluded source, not a recorded literature-only answer. |
| [ME3-CUA-0254](../../evidence/ME3-CUA-0254/actions.md) | PASS | Clicked Copy answer. Visible Answer copied as Markdown feedback appeared; actual clipboard contains matching question32356626, insufficient status, sourcePMID32356626 and provenance, saved as copied_answer.md. Reload retained same question/status/source count/Saved state; no research mutation. |
| [ME3-CUA-0255](../../evidence/ME3-CUA-0255/actions.md) | BLOCKED | Owned saved answer18 currently has exactly1 retrieved publication. Frozen steps require a result with multiple sources. |
| [ME3-CUA-0256](../../evidence/ME3-CUA-0256/actions.md) | BLOCKED | Available owned saved result has only1 source, not required multiple-source result. |
| [ME3-CUA-0257](../../evidence/ME3-CUA-0257/actions.md) | PASS | Saved /answer/18 URL, refreshed, navigated away and reopened it. Same question32356626, Evidence gap, Saved state and sourcePMID32356626 retained. First post-reopen copy reported clipboard unavailable; retry visibly succeeded and fresh clipboard exact Date2026-11-22T05:55:21.441685+00:00 matches254. Date-only page limitation remains250; stored identity/time persistence passes. |
| [ME3-CUA-0258](../../evidence/ME3-CUA-0258/actions.md) | PASS | At390x844 refreshed and reopened saved /answer/18 URL after navigating away. Same question/status/Saved state and sole source retained. Successful mobile Copy provides identical full stored Date2026-11-22T05:55:21.441685+00:00 and PMID32356626. Controls and scrolled body readable; page date-only defect remains251. |
| [ME3-CUA-0259](../../evidence/ME3-CUA-0259/actions.md) | BLOCKED | Current configured-server result is excluded-source Evidence gap, not required no-provider literature-only result. |
| [ME3-CUA-0260](../../evidence/ME3-CUA-0260/actions.md) | PASS | Opened Evidence table for owned source-backed outcome18. Limitations column explicitly says Unavailable: not extracted from the supplied abstracts; findings Unavailable: not synthesized. No fabricated study weakness presented. |
| [ME3-CUA-0261](../../evidence/ME3-CUA-0261/actions.md) | PASS | Opened source card then switched to Evidence table for same stored answer18. Both show identical Cardiovascular Disease, Drug Therapy, and Mortality in Covid-19 title, year2020 and source link labelled PMID32356626. Same sole stored source and retracted type, no neighbor substitution. |
| [ME3-CUA-0262](../../evidence/ME3-CUA-0262/actions.md) | PASS | Prepared unsaved baseline on owned answer18, clicked Save answer, navigated Saved answers and opened the saved row. Returns exact /answer/18 with same original question32356626 and stored outcome, not generic /thread. Saved state persists through navigation. |
| [ME3-CUA-0263](../../evidence/ME3-CUA-0263/actions.md) | PASS | At390x844 prepared unsaved baseline, clicked Save answer, used mobile navigation Saved answers and opened row32356626. Exact /answer/18 reopened with same stored question/outcome/Saved state. Required controls readable and no page-wide horizontal overflow. |
| [ME3-CUA-0264](../../evidence/ME3-CUA-0264/actions.md) | BLOCKED | Current deployment configured and existing saved outcome is excluded-source insufficiency, not independent no-provider mode. |
| [ME3-CUA-0265](../../evidence/ME3-CUA-0265/actions.md) | PASS | Chinese preference already saved and current detail notice displayed in Chinese. Expanded stored real English sourcePMID32356626: original structured English abstract remains unchanged, not translated/paraphrased. No model call invoked. |
| [ME3-CUA-0266](../../evidence/ME3-CUA-0266/actions.md) | PASS | Prepared real no-abstract PMID33551565 via normal UI after verifying both pipeline queries and pre-model no_abstracts guard. Scored owned answer19/thread17: expanded source explicitly says No abstract is available for this record; table marks findings/limitations unavailable, retains title/year/PMID and no fabricated quote. No model call needed. |
| [ME3-CUA-0267](../../evidence/ME3-CUA-0267/actions.md) | PASS | From owned answer18 clicked Conversation. Correct /thread/16 opens, question32356626 is turn01 with matching Evidence gap, English preference and one PubMed record, followed by continue composer. Correct original chronological association. |
| [ME3-CUA-0268](../../evidence/ME3-CUA-0268/actions.md) | PASS | At390x844 Conversation backlink from answer18 opens exact /thread/16. Matching question32356626 is turn01 with stored status/date and source count, followed by continue composer. Controls and wrapped status readable without page-wide horizontal overflow. |
| [ME3-CUA-0269](../../evidence/ME3-CUA-0269/actions.md) | BLOCKED | Owned outcomes18/19 are source-exclusion insufficiency, not failed provider generation/review. |
| [ME3-CUA-0270](../../evidence/ME3-CUA-0270/actions.md) | BLOCKED | Real long source abstract was available in earlier164/165, but no controlled answer with multiple long claim excerpts exists. |

## Continuation

Next case271; next batch271–290. Automatic uploads every20 remain authorized.
