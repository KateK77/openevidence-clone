# Batch009: ME3-CUA-0151–0170

4 PASS /0 FAIL /16 BLOCKED. Cumulative through170:85 PASS /9 FAIL /76 BLOCKED;303 NOT_RUN. All473 frozen cases retained.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture review](fixture_review.md)

## Findings

151 whitespace-only draft displayed7/2,000 with disabled Ask AI; submission attempt did not create a retrieval state or new empty conversation. All10 original history entries remained.159 source snapshot was prepared through the normal UI, saved, reopened and inspected with original abstract, PMID and retrieval provenance.164/165 real long abstract in Search PubMed was expanded and navigated to its last sentence and footer controls on desktop/mobile, with no clipping or unsupported AI-review claim.

## Fixture and scoring limits

159 uses PMID32356626, explicitly marked Retracted Publication. Both actual planned queries were checked before research submission: bare PMID yielded1 retracted record and quoted PMID yielded0. Fixed-source inspection established an all-ineligible-abstract set returns before the model call. The resulting saved record is /answer/18 (thread/16). It is not an accepted AI answer and no retracted medical conclusion is endorsed. Fixture preparation precedes scored Saved answers reopening (trace17 onward).

155–157 remain blocked: the newly prepared excluded-source outcome is not the required two-topic / legitimate literature-only outcome and does not retroactively change those results.158 requires same-account sign-out/sign-in credentials unavailable in this resumed session.159 does not prove accepted-generation source use.164/165 cover source-excerpt UI, not generation truncation or model comprehension. Official PMID39878158 was inspected independently; its structured abstract extends over multiple pages. Screenshot164/17 is named tail_matches by the capture call but actually shows the official record header; it is identity evidence only, and the app tail is14/18.

152/153 require isolated upstream failure.154/163 require controlled provider failure.160 requires isolated controlled zero-result research response.161/168–170 require deliberately absent provider configuration.162 requires controlled canonical metadata update.166 requires isolated untrusted source text.167 requires overlapping result sets. None of these special fixtures were supplied; configured production was not altered. Screenshots on BLOCKED rows document available preconditions only.

## Execution

Actual connected Google Chrome screenshots, pointer, keyboard and navigation; no DOM/API substitute for scoring. Tested live SHA c903b65ce3f8f49fe72416ca8948d215a0690a49 reconfirmed through read-only Render deployment list. No application/frozen-test/configuration changes and no paid model probe/generation. Screenshot dimensions may reflect extension scaling1425x891 or375x812; source popup initially1265x523. Canonical PNGs faithfully convert originals, without crop/resize/annotation; actual dimensions and SHA256 recorded. Later settled screenshots govern transient captures.

## Cases

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0151](../../evidence/ME3-CUA-0151/actions.md) | PASS | Entered seven whitespace characters (spaces/newline); count displayed 7/2,000 and Ask AI stayed disabled. Clicking it caused no submission or retrieval state. History before and after contained the identical ten titled conversations, with no empty question. |
| [ME3-CUA-0152](../../evidence/ME3-CUA-0152/actions.md) | BLOCKED | Inspected the current public application's history and reviewed documented fixture requirements. No isolated safe PubMed failure/throttle endpoint is supplied; no error was injected. |
| [ME3-CUA-0153](../../evidence/ME3-CUA-0153/actions.md) | BLOCKED | Viewed the current public history at mobile viewport. No controlled retrieval error or retry was executed. |
| [ME3-CUA-0154](../../evidence/ME3-CUA-0154/actions.md) | BLOCKED | Settings visibly reports AI synthesis configured and AI connection Configured · not checked (server model gemini-3.5-flash-lite). No provider probe or forced failure was run. |
| [ME3-CUA-0155](../../evidence/ME3-CUA-0155/actions.md) | BLOCKED | Verified configured AI mode. Available test conversations are unsupported-Chinese no-source outcomes; no two topic-specific source-bearing answers are available. |
| [ME3-CUA-0156](../../evidence/ME3-CUA-0156/actions.md) | BLOCKED | Inspected model mode before attempting a source-bearing literature-only research turn. Existing translation-limit turns do not supply citations. |
| [ME3-CUA-0157](../../evidence/ME3-CUA-0157/actions.md) | BLOCKED | Mobile settings shows AI synthesis configured. No citation-bearing literature-only research turn was submitted or reloaded. |
| [ME3-CUA-0158](../../evidence/ME3-CUA-0158/actions.md) | BLOCKED | Prepared the no-abstract PMID33551565 query boundary: quoted numeric search returned zero, and earlier bare-PMID lookup had one no-abstract record. The current account remains signed in; sign-out was not attempted. |
| [ME3-CUA-0159](../../evidence/ME3-CUA-0159/actions.md) | PASS | Prepared an owned saved excluded-source outcome using verified retracted PMID32356626, with no eligible abstracts for generation. Reopened it from Saved answers (/answer/18), expanded publication details and retrieval provenance: original abstract, PMID/DOI, original/normalized question, bare query1 PMID and quoted query0 PMIDs are inspectable. Saved state persisted across navigation. This tests retrieved-source persistence, not accepted AI synthesis. |
| [ME3-CUA-0160](../../evidence/ME3-CUA-0160/actions.md) | BLOCKED | Current saved outcome has one retracted publication, not a controlled zero-source response. The unique zero-result Search PubMed example from138/139 does not constitute the required isolated research fixture. |
| [ME3-CUA-0161](../../evidence/ME3-CUA-0161/actions.md) | BLOCKED | Settings confirms AI synthesis configured; normal publication saving would not exercise no-model operation. |
| [ME3-CUA-0162](../../evidence/ME3-CUA-0162/actions.md) | BLOCKED | A saved source snapshot now exists (/answer/18), but no documented isolated canonical-metadata update fixture exists. |
| [ME3-CUA-0163](../../evidence/ME3-CUA-0163/actions.md) | BLOCKED | Saved excluded-source result exists, but configured provider is not checked and no safe forced-follow-up generation failure is supplied. |
| [ME3-CUA-0164](../../evidence/ME3-CUA-0164/actions.md) | PASS | Retrieved real PMID39878158 in Search PubMed, expanded its structured long source abstract and navigated to all sections through Authors conclusions and final review-status sentence. Desktop text wraps within card; footer PMID/save controls remain reachable. Labels say Source abstract, with no assertion that AI reviewed it. Official PubMed identity and abstract were separately inspected; this is source-text UI coverage, not AI truncation/generation validation. |
| [ME3-CUA-0165](../../evidence/ME3-CUA-0165/actions.md) | PASS | At390x844 reran PMID39878158 search, collapsed and expanded details, and scrolled through the structured long abstract to the final review-status sentence and PMID/save controls. Text stayed inside the card with no page-wide horizontal overflow or inaccessible tail. Source abstract label is explicit; no AI-review claim appears. |
| [ME3-CUA-0166](../../evidence/ME3-CUA-0166/actions.md) | BLOCKED | Inspected available real-publication UI. No isolated instruction-like abstract fixture is provided; the ordinary Cochrane abstract is not an adversarial source. |
| [ME3-CUA-0167](../../evidence/ME3-CUA-0167/actions.md) | BLOCKED | Available saved research has two queries with counts1 and0, not overlapping PMID sets. Controlled per-query overlapping evidence fixture is unavailable. |
| [ME3-CUA-0168](../../evidence/ME3-CUA-0168/actions.md) | BLOCKED | Desktop settings is visibly configured, not an absent-provider instance. |
| [ME3-CUA-0169](../../evidence/ME3-CUA-0169/actions.md) | BLOCKED | Mobile settings shows AI synthesis configured. Unconfigured state was not induced. |
| [ME3-CUA-0170](../../evidence/ME3-CUA-0170/actions.md) | BLOCKED | Homepage says AI synthesis configured and uses Ask AI. This is expected configured mode, not the required no-model composer. |

## Continuation

Next frozen case171; next batch171–190. Automatic upload every20 remains authorized.
