# Batch024: ME3-CUA-0451–0470

{'BLOCKED': 9, 'PASS': 9, 'FAIL': 2}. Cumulative: {'PASS': 210, 'BLOCKED': 242, 'FAIL': 18, 'NOT_RUN': 3}

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

9 PASS /2 FAIL /9 BLOCKED.455/456: title saves, but focus does not visibly return to a meaningful history control; next Tab reaches answer link. Keyboard/mobile/public retrieval/documentation cases pass. Missing separate account, reauthentication credentials, unavailable provider instance and permitted PDF viewer remain blocked.

## Integrity

Live application SHA unchanged. No application/frozen-test/configuration modifications or paid synthesis. Thread24 renamed CUA455 focus return test and thread23 renamed CUA456 keyboard focus test. Save persistence verified in History; no claim that saving itself failed. Public shared demo accounts visible in linked documentation are not disposable isolated fixtures and were not used. Documentation statements are external evidence only, not proof of hosting internals. Browser screenshots can lag; settled captures govern conclusions. Raw transient captures retained except two intermediate documentation captures containing published shared-demo credentials; see0469/actions.md.

| Test | Status | Observation |
|---|---|---|
| [ME3-CUA-0451](../../evidence/ME3-CUA-0451/actions.md) | BLOCKED | Mobile authenticated accountA state captured; identity switch not executed. |
| [ME3-CUA-0452](../../evidence/ME3-CUA-0452/actions.md) | BLOCKED | Current mobile saved answer captured, not a provider-error workflow. |
| [ME3-CUA-0453](../../evidence/ME3-CUA-0453/actions.md) | PASS | At 390px, Tab traversed visible drawer controls, wrapping to Close; Escape returned to menu trigger. Tab then reached account, notice, settings, composer, examples, recent items and visible footer; Shift+Tab reversed with visible outlines. No off-screen trap or horizontal clipping. |
| [ME3-CUA-0454](../../evidence/ME3-CUA-0454/actions.md) | PASS | Keyboard-only at 390px: menu opened with Enter; reverse Shift+Tab reached Profile, Settings and Saved publications with visible outlines. Escape restored trigger, Tab traversed composer and recent items to visible footer; reverse focus remained visible without clipping/trap. |
| [ME3-CUA-0455](../../evidence/ME3-CUA-0455/actions.md) | FAIL | Keyboard opened inline Rename, edited thread24 to CUA455 focus return test and saved. Title and History row updated. Immediately after save no visible focus returned to Rename/history; next Tab went directly to View answer and evidence. Four reverse Tabs manually recovered History; edited row remained accessible. |
| [ME3-CUA-0456](../../evidence/ME3-CUA-0456/actions.md) | FAIL | Keyboard-only reproduced on thread23: title saved as CUA456 keyboard focus test; after Save, no visible focus returned to Rename/history and next Tab reached View answer and evidence. Manual reverse navigation returned to History with renamed row present. |
| [ME3-CUA-0457](../../evidence/ME3-CUA-0457/actions.md) | PASS | At 390px direct saved answer18 loaded; expanded Abstract & publication details for PMID32356626, scrolled readable metadata and source abstract with no clipping, then followed Conversation backlink to thread16 showing CUA342 synchronized thread16. No blank panel; synthesis unavailability shown honestly. |
| [ME3-CUA-0458](../../evidence/ME3-CUA-0458/actions.md) | PASS | Actual desktop Chrome loaded documented public HTTPS host; title MedEvidence AI 3.0, branded workspace and Research demonstration—not for clinical use plus synthetic-information notice visibly present. Real authenticated navigation/composer rendered. |
| [ME3-CUA-0459](../../evidence/ME3-CUA-0459/actions.md) | PASS | At 390px public HTTPS homepage loaded MedEvidence AI 3.0 title, responsive workspace, readable research-only and synthetic-data disclaimers, menu and composer without horizontal clipping. |
| [ME3-CUA-0460](../../evidence/ME3-CUA-0460/actions.md) | BLOCKED | Public homepage is currently authenticated as synthetic account me3cua_20261120_batch004; account control displayed instead of Sign in. |
| [ME3-CUA-0461](../../evidence/ME3-CUA-0461/actions.md) | BLOCKED | Profile shows existing synthetic account and saved first name; no fresh account created. |
| [ME3-CUA-0462](../../evidence/ME3-CUA-0462/actions.md) | BLOCKED | Hosted History shows actual synthetic research threads including renamed CUA455/456, script-literal415 and PMID thread16. |
| [ME3-CUA-0463](../../evidence/ME3-CUA-0463/actions.md) | PASS | Public app search for PMID33551565 returned one live publication, ADA's Standards of Medical Care in Diabetes, with metadata and honest no-abstract notice. Expanded details and opened official PubMed; matching title, PMID33551565 and DOI10.2337/cd21-pe01 visibly verified. |
| [ME3-CUA-0464](../../evidence/ME3-CUA-0464/actions.md) | BLOCKED | Public saved-publication list renders five account-bound synthetic bookmarks; current-session saved state visible. |
| [ME3-CUA-0465](../../evidence/ME3-CUA-0465/actions.md) | BLOCKED | Settings visibly reports Configured—not checked; server model gemini-3.5-flash-lite. No provider call issued. |
| [ME3-CUA-0466](../../evidence/ME3-CUA-0466/actions.md) | BLOCKED | Mobile Settings shows Configured—not checked and gemini-3.5-flash-lite, with provider-quota warning readable. |
| [ME3-CUA-0467](../../evidence/ME3-CUA-0467/actions.md) | PASS | At 390px opened hosted mobile drawer, navigated Search PubMed with readable search/filter controls, reopened menu and navigated Profile; identity, editable fields and session controls reachable via vertical scroll without horizontal clipping. |
| [ME3-CUA-0468](../../evidence/ME3-CUA-0468/actions.md) | BLOCKED | Public Home visibly says research demonstration—not for clinical use and use synthetic information only. Publication and PDF warning scenario is only partially observable. |
| [ME3-CUA-0469](../../evidence/ME3-CUA-0469/actions.md) | PASS | Followed actual app Demo accounts & usage limits link to public repository README. Visible Try the public demo section states Render Free sleeps, wake may take around a minute, availability depends on quotas and is not always-on; public provider allowance30/day and200 total described. No unlimited-uptime promise. Documentation evidence only, not hosting-internal verification. |
| [ME3-CUA-0470](../../evidence/ME3-CUA-0470/actions.md) | PASS | Followed hosting details link to docs/public-demo.md and visually read Free-tier limits and expiration. Documentation distinguishes Neon no fixed30-day expiry from observed December1 quota-cycle boundary, explicitly not database deletion date; Render sleep/quota/no uptime guarantee also stated. Documentation wording only, not an audit of database internals. |

Next final partial batch471–473.
