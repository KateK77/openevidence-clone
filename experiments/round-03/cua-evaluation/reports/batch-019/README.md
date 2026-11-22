# Batch019: ME3-CUA-0351–0370

17 PASS / 1 FAIL / 2 BLOCKED. Cumulative through370:177 PASS /14 FAIL /179 BLOCKED;103 NOT_RUN.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

351–357 real desktop/mobile bookmark removal and duplicate-save guards passed.358/359 lack controlled persistence-failure/recovery fixtures.360–364 saved-publication title filters, clear recovery and empty states passed.365/366 collection names save and filter correctly;367 existing member assignment and368 removal preserve standalone bookmarks.369 FAIL: a prepared two-member collection has no visible Delete collection/confirmation workflow.370 exact query/year/type/sort retained in saved-search list.

## Integrity

Read-only Render verification identifies unchanged live c903b65ce3f8f49fe72416ca8948d215a0690a49. No app/frozen-test/config modifications or paid synthesis. Actual Chrome screenshots and pointer/keyboard actions only for scoring. Original JPEGs retained; canonical PNGs faithfully converted without resizing/cropping/annotation. Transient captures do not establish success. Collection names are per-publication string fields in this UI; no independent collection directory or deletion control was observed. Duplicate guard tests attempted the already-Saved control; they do not claim two accepted save API calls.

Current synthetic state: Saved answers16/18; saved publications6373426,33551565,39878158. CUA365 desktop collection contains6373426/39878158 after369 preparation; CUA366 mobile collection contains33551565. One saved search diabetes/year2024/Clinical Trial/pub date. Eleven conversations unchanged.

## Cases

| Test | Status | Observation |
|---|---|
| [ME3-CUA-0351](../../evidence/ME3-CUA-0351/actions.md) | PASS | Removed independently saved PMID33551565; matching filter becomes explicit no saved publications, total2. Browser refresh resets filter and shows remaining Minnesota6373426 and Electronic-cigarettes39878158 records; removed ADA record absent. No confirmation shown. |
| [ME3-CUA-0352](../../evidence/ME3-CUA-0352/actions.md) | PASS | At390x844 removed PMID6373426 from two-bookmark list. After actual refresh list count1 shows unchanged Electronic cigarettes for smoking cessation PMID39878158; Minnesota removed. Remove/status readable and no horizontal overflow. |
| [ME3-CUA-0353](../../evidence/ME3-CUA-0353/actions.md) | PASS | Opened saved answer18, Unsave, reloaded Saved answers: only20/16 remain. Direct original/answer/18 still opens original32356626 response and1source with Save answer control. Bookmark removal does not delete answer. |
| [ME3-CUA-0354](../../evidence/ME3-CUA-0354/actions.md) | PASS | At390x844 unsaved answer20 C309. Reloaded Saved answers shows only answer16/A150. Original/answer/20 still accessible with unchanged translation-limit response and Save answer control; no horizontal overflow. |
| [ME3-CUA-0355](../../evidence/ME3-CUA-0355/actions.md) | PASS | Saved unsaved PMID33551565 once. Save control becomes Saved; clicked same Saved control without unsave, no new-save feedback or count increment. Reading list total2 contains exact ADA PMID33551565 once plus prior39878158. UI prevents second save. |
| [ME3-CUA-0356](../../evidence/ME3-CUA-0356/actions.md) | PASS | Saved exact answer18, attempted same save again via Saved control without any unsave. UI exposes Saved rather than another Save operation. Saved answers contains32356626 once plus priorA150; no duplicate exact-answer row or new success feedback. |
| [ME3-CUA-0357](../../evidence/ME3-CUA-0357/actions.md) | PASS | Saved previously unsaved real PMID6373426. Actual immediate screenshot shows Saving...; settled state Saved plus completion feedback and count2→3. Clicking unchanged Saved does not restart save; reading list contains correct single record. Pending and final states retained. |
| [ME3-CUA-0358](../../evidence/ME3-CUA-0358/actions.md) | BLOCKED | Ordinary bookmark persistence works in current demo, but no isolated controlled answer-save failure/recovery fixture is available. |
| [ME3-CUA-0359](../../evidence/ME3-CUA-0359/actions.md) | BLOCKED | Real publication saved successfully in357; controlled persistence error and recoverable condition are unavailable in the current shared demo. |
| [ME3-CUA-0360](../../evidence/ME3-CUA-0360/actions.md) | PASS | Fixture genuinely saved distinct papers via UI345/355/357. In current3-paper reading list, unique title substring smoking cessation yields only Electronic cigarettes for smoking cessation PMID39878158; unrelated ADA/Minnesota hidden. |
| [ME3-CUA-0361](../../evidence/ME3-CUA-0361/actions.md) | PASS | At390x844 using genuinely UI-saved three-paper fixture, unique title substring Standards of Medical Care reduces list to exact ADA PMID33551565, other owned titles hidden. Readable filter/card/status and no horizontal overflow. |
| [ME3-CUA-0362](../../evidence/ME3-CUA-0362/actions.md) | PASS | Applied Minnesota restrictive filter showing only6373426. Cleared text without submit/reload: previously hidden ADA33551565 and Electronic cigarettes39878158 cards reappear immediately while Minnesota remains. |
| [ME3-CUA-0363](../../evidence/ME3-CUA-0363/actions.md) | PASS | At390x844 applied smoking cessation filter showing only39878158. Clearing restores Minnesota6373426 and ADA33551565 alongside Electronic cigarettes without submit/reload. All cards readable via vertical scroll, no horizontal overflow. |
| [ME3-CUA-0364](../../evidence/ME3-CUA-0364/actions.md) | PASS | Nonexistent CUA364 zephyrquartz nonexistent filter yields explicit No saved publications found and instruction to clear filter. Editable filter remains; clearing restores list. No dedicated reset button, working text-clear recovery path. |
| [ME3-CUA-0365](../../evidence/ME3-CUA-0365/actions.md) | PASS | In owned Saved publications created name CUA365 desktop collection through article Collection/Update collection control. Readable Saved/Changes saved successfully; collection-name filter returns member PMID6373426 only, and name survives reload. App represents collections inline and through filtering, not a separate directory. |
| [ME3-CUA-0366](../../evidence/ME3-CUA-0366/actions.md) | PASS | At390x844 created CUA366 mobile collection on independently saved33551565 using Collection/Update collection. Saved/Changes saved successfully readable; filtering by exact collection name returns only ADA member. Inline collection representation, no separate directory. Controls/status fit mobile. |
| [ME3-CUA-0367](../../evidence/ME3-CUA-0367/actions.md) | PASS | Existing independently saved39878158 assigned to CUA365 desktop collection via Collection update. Opened collection through name filter: only6373426 and39878158 members, each once, with matching names. Canonical saved-publication count remains3, no duplicate bookmark. |
| [ME3-CUA-0368](../../evidence/ME3-CUA-0368/actions.md) | PASS | Clearing PMID39878158 Collection and updating removed it from CUA365 desktop collection; main Saved publications still shows the same article as Saved with blank Collection. PMID6373426 remains in the collection. |
| [ME3-CUA-0369](../../evidence/ME3-CUA-0369/actions.md) | FAIL | Prepared CUA365 desktop collection containing PMID6373426 and39878158. Inspected top, bottom and filtered collection view: only per-article Collection input/Update collection and Remove from library are exposed; no collection Delete or confirmation workflow. |
| [ME3-CUA-0370](../../evidence/ME3-CUA-0370/actions.md) | PASS | Searched real PubMed for diabetes, year2024, Clinical Trial, Publication date (16 publications). Saved search list shows one diabetes entry with sort:pub date, year:2024, article_type:Clinical Trial matching selected parameters. |

Next automatic batch371–390.
