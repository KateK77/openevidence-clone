# Batch016: ME3-CUA-0291–0310

9 PASS /0 FAIL /11 BLOCKED. Cumulative through310:126 PASS /12 FAIL /172 BLOCKED;163 NOT_RUN.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

292/293 exact original-question display,294/295 separate actual queries desktop/mobile,296 labelled retrieval time,302 pipeline identifier passed on real saved source-backed answer18.299 separates previous question from executed queries in prepared two-turn thread15.309 adds third related unsupported-Chinese question; answer20 correctly lists A150 then B150 question text chronologically. These context checks use real translation-limited system outcomes; no successful model synthesis or retrieval on those turns inferred.

310 fresh unsupported term creates thread18/answer21. Normalized field explicitly says No reliable mapping and unmapped Chinese terms; notice distinguishes translation limitation from absent studies. PASS is limited to the required normalization/provenance fields. Existing top-level Evidence gap badge defect from86/87 remains; this report does not assert it is fixed.

291 missing controlled failed revision;297/298 and305–308 would require configured model submissions without approved usage;300 missing separate per-query PMID fixture;301 missing controlled overlap fixture;303 lacks accepted answer;304 lacks no-provider instance. Each BLOCKED reason retained.

## Integrity

Live tested SHA c903b65ce3f8f49fe72416ca8948d215a0690a49 verified through read-only Render deployment. No app/frozen-test/config edits or paid generation. Real connected-Chrome visual CUA only; offline code reads used solely for no-cost branch preparation. Canonical PNGs preserve original capture dimensions, without crop/resize/annotation. Before/after may be identical for inspection-only or blocked cases; action traces disclose actual actions. Saved answers16/18 unchanged; new20/21 unsaved. Chinese/Detailed/Compact preferences retained.

## Cases

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0291](../../evidence/ME3-CUA-0291/actions.md) | BLOCKED | No accepted-original plus controlled withheld/failed revision fixture available for copy/export leakage verification. |
| [ME3-CUA-0292](../../evidence/ME3-CUA-0292/actions.md) | PASS | Answer18 expanded Retrieval provenance labels Original question and exactly retains submitted 32356626, separately from normalized text and executed searches. |
| [ME3-CUA-0293](../../evidence/ME3-CUA-0293/actions.md) | PASS | At390px, collapsed/reopened provenance retains exact original32356626 under Original question; fields wrap within page, with no essential content clipped. |
| [ME3-CUA-0294](../../evidence/ME3-CUA-0294/actions.md) | PASS | Successfully retrieved real PMID32356626 answer shows actual executed queries32356626(1PMID) and quoted32356626(0PMIDs), separately from Original question and normalized-before-context fields. |
| [ME3-CUA-0295](../../evidence/ME3-CUA-0295/actions.md) | PASS | 390px provenance distinguishes original/normalized/prior-question fields from actual executed32356626 and quoted32356626 queries with1/0PMID counts; wrapped explanation and counts readable, no page-wide overflow. |
| [ME3-CUA-0296](../../evidence/ME3-CUA-0296/actions.md) | PASS | Answer18 Retrieval provenance labels Retrieved at11/21/2026,11:55:20PM with run question32356626 and1/0 query counts; readable and tied to current answer. |
| [ME3-CUA-0297](../../evidence/ME3-CUA-0297/actions.md) | BLOCKED | Required supported-Chinese AskAI submission may invoke configured model; existing PubMed-library search lacks full answer normalization provenance. |
| [ME3-CUA-0298](../../evidence/ME3-CUA-0298/actions.md) | BLOCKED | Required supported-Chinese AskAI submission may invoke configured model; existing PubMed-library search lacks full answer normalization provenance. |
| [ME3-CUA-0299](../../evidence/ME3-CUA-0299/actions.md) | PASS | Prepared two-turn thread15: second answer17 Original question B150 shown; Previous questions separately contains exact A150 first question. Executed PubMed queries separately states none recorded because unsupported mapping. This verifies context-field separation on real translation-limited outcomes; no successful retrieval/generation claimed. |
| [ME3-CUA-0300](../../evidence/ME3-CUA-0300/actions.md) | BLOCKED | Existing answer18 has two queries but only one nonempty result; required prepared separate per-query PMID evidence lists unavailable. |
| [ME3-CUA-0301](../../evidence/ME3-CUA-0301/actions.md) | BLOCKED | No controlled overlapping query result sets with traceable shared PMID supplied; existing query counts1/0 do not exercise deduplication. |
| [ME3-CUA-0303](../../evidence/ME3-CUA-0303/actions.md) | BLOCKED | Real accepted English/Standard model answer absent; cannot verify generation-preference snapshot using system fallback. |
| [ME3-CUA-0304](../../evidence/ME3-CUA-0304/actions.md) | BLOCKED | Independent no-provider instance absent; current server configured. |
| [ME3-CUA-0305](../../evidence/ME3-CUA-0305/actions.md) | BLOCKED | Specified diabetes question and limitations follow-up can invoke configured model; no approved budget. |
| [ME3-CUA-0306](../../evidence/ME3-CUA-0306/actions.md) | BLOCKED | Mobile specified diabetes/limitations generation flow lacks approved usage or independent no-provider fixture. |
| [ME3-CUA-0307](../../evidence/ME3-CUA-0307/actions.md) | BLOCKED | Specified diabetes follow-up generation has not been executed because approved model usage unavailable; generic unsupported-term context cannot prove diabetes retrieval relevance. |
| [ME3-CUA-0308](../../evidence/ME3-CUA-0308/actions.md) | BLOCKED | Required diabetes-to-new-asthma research generation can invoke configured model; no approved usage for either topic. |
| [ME3-CUA-0302](../../evidence/ME3-CUA-0302/actions.md) | PASS | Owned saved source-backed answer18 shows Pipeline round-03 within Retrieval provenance, adjacent exact original question, retrieved-at time and executed query counts. No secret values exposed. |
| [ME3-CUA-0309](../../evidence/ME3-CUA-0309/actions.md) | PASS | Submitted third related unsupported-Chinese question C309 in prepared two-turn thread15; answer20 provenance lists exact prior A150 then B150 questions chronologically, separate from normalized field/empty executed queries. No prior answer prose represented as context facts. Safe translation-limited outcomes; no model or PubMed generation claimed. |
| [ME3-CUA-0310](../../evidence/ME3-CUA-0310/actions.md) | PASS | Fresh unsupported glossary term脊髓空洞症 submitted, thread18/answer21 created. Provenance preserves original, explicitly shows No reliable mapping / unmapped Chinese terms, translation limitation not absence of studies, and no executed queries. This case scopes normalized/mapping fields; separate Evidence gap badge defect from86/87 persists and is not considered repaired. |

Next case311; next automatic batch311–330.
