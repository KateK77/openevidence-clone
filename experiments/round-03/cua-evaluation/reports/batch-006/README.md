# Batch006: ME3-CUA-0091–0110

13 PASS /2 FAIL /5 BLOCKED. Cumulative through110:57 PASS /4 FAIL /49 BLOCKED;363 NOT_RUN. All473 frozen cases retained.

[Cumulative results](../../results/all_results.csv) · [Complete action trace](action_trace_complete.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture notes](fixture_review.md)

## Findings

107/108 reproduce a date-sort presentation defect on desktop/mobile: Publication date is selected and applied, but visible years begin2028,2028,2026,2027,2027. PMID43018112 (2026) precedes PMID43044620 (2027). No date-metadata limitation explains this to the user. This is an observed UI inconsistency; no backend cause is asserted.

Unicode and inner-spacing persistence passed using unmapped Chinese inputs, without calling a model. Keyword, PMID and DOI lookup, metadata visibility, source links and relevance selection passed. Authors were matched visually against official PubMed. Year2024 filter returned16 records; every card was visually inspected. [All observed PMIDs and years](../../evidence/ME3-CUA-0110/observed_years.json) are manually transcribed from screenshots.

92/95 require isolated controlled latency,93/94 require genuine Chinese IME,97 requires isolated upstream-fault fixture. These unavailable prerequisites are BLOCKED, not simulated or passed.

## Execution and limitations

Application https://medevidence-ai-v3.onrender.com/, deployed SHA c903b65ce3f8f49fe72416ca8948d215a0690a49; read-only Render deployment check in preceding batch. Chrome screenshot/pointer/keyboard only for scored observations. Exact Chrome build/CUA model unavailable. Source inspection bounded no-provider submissions only. No app/test edits, production configuration changes or paid synthesis. All rows outside91–110 preserved. UTC action timestamps correspond to user-local November21,2026.

Original JPEGs retained; canonical PNGs are conversions only. Requested1440x900/390x844 differ from some tool-returned1425x891/375x812 captures. Transient screenshots can lag actions; settled captures retained. A96 scroll timeout moved the viewport and was recovered by screenshot. Copy-answer failed with explicit clipboard-unavailable message; its stale clipboard value was not accepted, and native field selection/copy verified spacing. A110 full-page screenshot timed out and later produced a229x900 downscaled preview; only readable viewport captures were used for the year verdict.

## Cases

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0091](../../evidence/ME3-CUA-0091/actions.md) | PASS | Submitted mixed Unicode question 脊髓空洞症 MRI / CSF：影像与随访？. Reopened it from Research history and then answer detail. Chinese characters, Latin MRI/CSF and punctuation remain readable without loss. Safe unmapped-term route; no synthesis asserted. |
| [ME3-CUA-0092](../../evidence/ME3-CUA-0092/actions.md) | BLOCKED | Inspected configured research composer; no controlled pending request started. |
| [ME3-CUA-0093](../../evidence/ME3-CUA-0093/actions.md) | BLOCKED | Chrome composer visible, but genuine Chinese IME composition session cannot be established through available browser controls. No paste/direct type was counted as IME. |
| [ME3-CUA-0094](../../evidence/ME3-CUA-0094/actions.md) | BLOCKED | Chrome composer visible, but genuine Chinese IME composition session cannot be established through available browser controls. No paste/direct type was counted as IME. |
| [ME3-CUA-0095](../../evidence/ME3-CUA-0095/actions.md) | BLOCKED | Composer inspected; rapid Enter not executed without controllable latency. |
| [ME3-CUA-0096](../../evidence/ME3-CUA-0096/actions.md) | PASS | Submitted two-part query with three outer spaces and intentional double inner spaces: 脊髓空洞症: MRI  findings;  CSF flow?. Reopened original-question provenance: wording and punctuation retained. Read-only Rename field and native Ctrl+C returned exactly trimmed original including both double spaces. No title saved. Copy answer reported clipboard unavailable; its stale clipboard content was discarded, and native selection copy used instead. |
| [ME3-CUA-0097](../../evidence/ME3-CUA-0097/actions.md) | BLOCKED | Returned to research composer; no injected upstream error attempted. |
| [ME3-CUA-0098](../../evidence/ME3-CUA-0098/actions.md) | PASS | Searched diabetes in live literature UI:16 publications. Visible records include Diagnosis and Management of Central Diabetes Insipidus in Adults (2022, PMID35771962), Nephrogenic diabetes insipidus: a comprehensive overview (2022, PMID35146976), and Diabetes or endocrinopathy admitted in the COVID-19 ward (2020, PMID32383239), each with source link. Results differ meaningfully from prior GLP-1 query. |
| [ME3-CUA-0099](../../evidence/ME3-CUA-0099/actions.md) | PASS | Mobile: entered diabetes and submitted Search PubMed;16 publications. First two cards show complete wrapped titles,2022 dates, metadata, PMID35771962 and35146976 links. Results/control widths fit; page scrolling reveals required links without horizontal overflow. Requested390x844; original scaled capture retained. |
| [ME3-CUA-0100](../../evidence/ME3-CUA-0100/actions.md) | PASS | Entered known PMID15137354 and searched: exactly1 publication, matching Pathophysiology of diabetes mellitus, Critical care nursing quarterly,2004. Expanded actual details show Richard A Guthrie/Diana W Guthrie, DOI10.1097/00002727-200404000-00003, abstract and matching PMID source link. |
| [ME3-CUA-0101](../../evidence/ME3-CUA-0101/actions.md) | PASS | Mobile entered PMID15137354, submitted search and obtained1 matching publication. Collapsed/reopened its details via pointer. Title and2004 journal metadata matched fixture; long abstract and DOI wrapped legibly, PMID15137354 source link accessible at bottom without horizontal overflow. |
| [ME3-CUA-0102](../../evidence/ME3-CUA-0102/actions.md) | PASS | Searched exact DOI10.1097/00002727-200404000-00003 from documented record:1 matching Pathophysiology of diabetes mellitus publication,2004, PMID15137354. Opened result details; same DOI, journal and authors displayed. |
| [ME3-CUA-0103](../../evidence/ME3-CUA-0103/actions.md) | PASS | Executed diabetes keyword search and expanded first publication. Title Diagnosis and Management of Central Diabetes Insipidus in Adults, The Journal of clinical endocrinology and metabolism,2022 match card and details. Details give2022 Sep28 and DOI10.1210/clinem/dgac381; card links PMID35771962. |
| [ME3-CUA-0104](../../evidence/ME3-CUA-0104/actions.md) | PASS | Mobile keyword search diabetes: opened first publication after explicitly collapsing/reopening. Full title wraps readably; journal The Journal of clinical endocrinology and metabolism wraps within card;2022 card year matches2022 Sep28 detail. Authors, DOI and abstract visible without horizontal overflow. |
| [ME3-CUA-0105](../../evidence/ME3-CUA-0105/actions.md) | PASS | Opened publication details for PMID35771962. Five authors displayed: Maria Tomkins, Sarah Lawless, Julie Martin-Grace, Mark Sherlock, Chris J Thompson. Opened official PubMed source and visually matched all five author names and PMID. |
| [ME3-CUA-0106](../../evidence/ME3-CUA-0106/actions.md) | PASS | Activated source link PMID35771962 from expanded publication. Opened tab URL https://pubmed.ncbi.nlm.nih.gov/35771962/; visible official PubMed title and PMID match application card. |
| [ME3-CUA-0107](../../evidence/ME3-CUA-0107/actions.md) | FAIL | Selected Publication date for diabetes, clicked Search and observed loading then16 results. Displayed order begins2028 (PMID43062408),2028 (43062407),2026 (43018112),then2027 (43044620 and43008771). Actual order_scroll2 screenshot shows adjacent2026/2027 reversal; no date-field limitation explained. |
| [ME3-CUA-0108](../../evidence/ME3-CUA-0108/actions.md) | FAIL | Mobile selected Publication date and submitted diabetes search; observed Searching then16 results. Adjacent readable cards show PMID43018112 year2026 above PMID43044620 year2027, reproducing desktop order discrepancy. No date metadata limitation explanation visible. |
| [ME3-CUA-0109](../../evidence/ME3-CUA-0109/actions.md) | PASS | Switched diabetes from Publication date to Relevance and applied search. Loading observed, then16 results. Relevance visibly retained; first publication changed from Skeletal phenotype... (PMID43062408) to Diagnosis and Management of Central Diabetes Insipidus in Adults (PMID35771962), matching original relevance result. |
| [ME3-CUA-0110](../../evidence/ME3-CUA-0110/actions.md) | PASS | Set year2024 for diabetes and applied search. Inspected all16 returned cards across screenshots:15 display2024 and PMID39845881 displays2025; none earlier than2024. Returned to top and verified filter2024 remains visible. Manually transcribed all PMIDs/years in observed_years.json. Full-page screenshot timed out and returned a downscaled preview later; year verdict uses readable viewport captures only. |

## Continuation

Next frozen case111; next batch111–130. User authorized automatic uploads every20; no further per-batch approval required.
