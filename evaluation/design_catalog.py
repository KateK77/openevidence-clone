"""Specification-only catalog authored before implementation inspection/execution."""
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SPEC=ROOT.parent/'experiments/round-03/consolidated-prompt.md'
REQ={
'R01':'Original identity, research-only disclaimer and no clinical validation claims',
'R02':'Home, examples, recent conversations, primary navigation and multiline composer',
'R03':'Registration, login, logout, hashing, CSRF and session handling',
'R04':'Profile/settings, language, display, detail preferences and persistence',
'R05':'Natural-language/short/Chinese query handling and transparent normalization',
'R06':'Official live PubMed search, query generation, ranking and deduplication',
'R07':'Publication identifiers, metadata, abstracts and distinct electronic/issue dates',
'R08':'Year, journal, article-type and free-full-text filters; relevance/date sort',
'R09':'Missing-model literature mode and clear generation/configuration states',
'R10':'Real abstract-grounded answer, findings, limitations, gaps, timestamps and model identity',
'R11':'Citation membership, exact quotations, numeric consistency and separate claim review',
'R12':'Chinese prose, one wrong-language retry and explicit failure; original-language sources',
'R13':'Owner regeneration from existing snapshot; preserve original answer and saved state',
'R14':'Original/normalized/context/executed-query provenance in UI and exports',
'R15':'Follow-up context, new evidence, chronological persistent conversations',
'R16':'History reopen/search/rename/delete/date-sort and logout persistence',
'R17':'Separate saved answers/publications; progress, feedback and duplicate prevention',
'R18':'Evidence library details/search/remove/organization and saved searches',
'R19':'Copy, Markdown, PDF, BibTeX, CSV; Unicode and traceable references',
'R20':'Ownership isolation and stale cross-account response rejection',
'R21':'Timeout/rate-limit/empty/malformed metadata/provider failures and honest recovery',
'R22':'Untrusted-content resistance, validation, credential safety and no fabricated evidence',
'R23':'Responsive/mobile/keyboard interaction and loading/error/empty states',
'R24':'Usable backend model configuration, connection/Chinese check, hosted and local support',
'R25':'Preserve existing accounts/data/snapshots through version upgrades',
'R26':'Health/API documentation and reproducible retrieval/model provenance',
}
# title|category|requirements|mode|goal/ordered workflow|objective assertions (semicolon-separated)
# N=offline-safe UI state; U=two users; P=live PubMed; G=real no-paid application model;
# C=controlled synthetic error transport, never scored as successful real synthesis;
# L=legacy snapshot; M=mobile. Modes combine with +.
ROWS=[
('1', '''Research identity|Navigation|R01|N|Open the landing page and inspect the identity and research boundary.|Research demonstration disclaimer is visible;Branding is independent and does not claim OpenEvidence affiliation
Primary destinations|Navigation|R02|N|Locate Ask AI, Research History, Saved Answers, Evidence Library, Settings and Profile; open each destination.|All six destinations are discoverable and reachable or request authentication;No navigation ends in a broken page
Composer multiline|Composer|R02|N|Focus the medical question input and insert a second line with Shift+Enter without submitting.|Input contains both lines;No question submission occurs on Shift+Enter
Example question entry|Composer|R02|N|Choose an example research question and inspect the resulting editable question.|Chosen example fills or starts the corresponding question flow;The displayed question matches the chosen topic
Sign-in entry|Accounts|R03|N|Open the sign-in entry and inspect the form and account-registration route.|Username and masked password controls have labels;An account-registration route is available
Saved answer destination|Saved research|R17|N|Open Saved Answers with an empty authenticated fixture.|Destination is clearly identified as saved answers;Empty state is honest and offers usable navigation
Publication library entry|Evidence library|R18|N|Open Evidence Library with an empty authenticated fixture.|Publication destination is distinct from Saved Answers;No fictitious saved publication appears
Preference controls|Settings|R04|N|Open Settings and inspect language, display and answer-detail choices.|Required language/display/detail preferences are discoverable;Any unavailable model selection is clearly bounded
Missing-model notice|Model state|R09,R24|N|Inspect the composer and language preference while no application model is configured.|Both surfaces explain unavailable generation;Literature mode is not represented as a generated answer
Research history empty state|History|R16,R23|N|Open a new researcher's history.|No other user's history is displayed;Empty state is understandable and navigable'''),
('2', '''Register a researcher|Accounts|R03|N|Register a new synthetic username with a valid unique password, then sign in.|Exactly one usable account is created;Successful login establishes the new identity
Valid login and reload|Accounts|R03|N|Sign in to the prepared account and reload its profile.|Identity remains authenticated after reload;No unrelated account data appears
Invalid login|Accounts|R03,R22|N|Attempt login using the prepared username and a wrong password.|Authentication is rejected visibly;No authenticated session or private content is granted
Logout persistence|Accounts|R03|N|Sign out, reload and open a private destination.|UI immediately reflects sign-out;Reload does not restore the prior session
Profile save persistence|Profile|R04,R17|N|Change an editable profile value, save it and reload.|Success is visible;The persisted value matches the submitted change
Language preference persistence|Settings|R04,R09|N|Choose Chinese, save and reload with no model configured.|Chinese preference persists;UI explains that preference alone does not enable synthesis
Detail preference persistence|Settings|R04|N|Change response detail level, save, navigate away and return.|Selected level persists;Preference applies to future generation rather than silently rewriting prior answers
Whitespace rejection|Composer|R05,R22|N|Submit a whitespace-only question.|A visible validation response is shown;No research conversation or provider request is created
Single-character query|Search|R05,R06|P|Submit the non-whitespace query x and inspect completion state.|Query is accepted rather than rejected solely for length one;Sources or an honest empty result are shown
Chinese glossary query|Search|R05,R14|P|Submit 糖尿病 and inspect query provenance.|Original Chinese question is retained;Executed English mapping is disclosed and relates to the term
Unsupported Chinese mapping|Search|R05,R21|P|Submit an unsupported Chinese term 量子香蕉综合征 and inspect the response.|An actionable unsupported-mapping message appears;It is not falsely reported as a definitive zero-evidence search
Live obesity literature|Search|R06,R09|P|Ask for evidence on GLP-1 receptor agonists in obesity in literature mode.|At least one retrieved PMID resolves in official response evidence;No canned generated answer is substituted
PMID source resolution|Sources|R07|P|Resolve PMID 31452104 using the available publication/search flow and open its detail.|Displayed identifier matches the requested PMID;Title and DOI agree with the independently captured official record
DOI source resolution|Sources|R07|P|Resolve DOI 10.1007/978-1-4939-9752-7_10 and inspect the source.|The resolved article matches the DOI;No duplicate identity is created for the same PMID
Open official source|Sources|R07|P|From a retrieved article open its original PubMed link.|Navigation reaches the matching official PMID record;The original article detail remains recoverable
Missing abstract disclosure|Sources|R07,R10|P|Open the preselected official publication that has no abstract.|Missing abstract is stated explicitly;No abstract text or extracted findings are invented
Card and table views|Evidence presentation|R07,R10|P|Switch a completed literature-only evidence set between cards and table.|Both views represent the same source identities;Unextracted findings and limitations are marked unavailable
Save a publication|Saved research|R17,R18|P|Save one retrieved publication and reopen Saved Publications.|Save progress or completion is visible;Exactly one owned saved entry exists
Remove saved publication|Saved research|R18|N|Remove the prepared saved publication and reload the saved list.|Saved relationship is removed persistently;Unrelated saved entries remain
History reopen|History|R15,R16|N|Open a prepared research conversation from history.|The correct question and chronology are shown;Persisted source associations are retained'''),
('3', '''New English synthesis|Answer generation|R06,R10,R11|P+G|Ask What evidence supports GLP-1 receptor agonists for obesity? and inspect the completed answer and sources.|Answer is generated by the configured real provider;Each displayed reference belongs to the retrieved evidence;Abstract-only basis is disclosed
Chinese synthesis|Answer generation|R04,R10,R12|P+G|Set Chinese and submit 糖尿病药物的心血管获益有哪些证据？; inspect answer and original sources.|Generated explanatory prose is Chinese;Source quotations and titles remain explicitly original-language;Sources map to retrieved records
Copy an answer|Exports|R19|N|Copy the prepared clearly labelled synthetic answer and paste into the evaluation clipboard viewer.|Clipboard contains that answer's text and traceable references;No unrelated user's content is copied
Markdown export|Exports|R14,R19|N|Export the prepared bilingual answer as Markdown and inspect the downloaded artifact.|Chinese characters round-trip in UTF-8;Answer and source identifiers are present;Provenance stages remain distinguishable
PDF export|Exports|R19|N|Export the prepared bilingual answer as PDF and inspect rendered pages.|Chinese and Latin text render without replacement glyphs;Headings/page numbering are readable;References remain traceable
BibTeX export|Exports|R07,R19|N|Export a prepared answer's references as BibTeX.|Artifact parses as BibTeX;Entries match referenced PMIDs/DOIs and Unicode authors;Unavailable fields are not fabricated
CSV export|Exports|R07,R19|N|Export a prepared evidence set as CSV and inspect it in the independent parser.|UTF-8 content survives parsing;Rows and identifiers match the set;Chinese content is legible in the documented spreadsheet encoding
Save answer and reload|Saved research|R17|N|Save a prepared answer, reload and reopen it from Saved Answers.|One owned bookmark persists;The saved item opens the exact answer revision
Duplicate-save prevention|Saved research|R17|N|Save an unchanged prepared answer twice using available controls, then revisit Saved Answers.|Pending or unchanged state prevents duplicate submission;Only one bookmark exists;UI shows an accurate saved state
History rename and search|History|R16|N|Rename the prepared conversation to EVA obesity review, reload and find it by that title.|New title persists;History search returns the intended conversation without unrelated rows
Delete a conversation|History|R16|N|Delete one of two prepared conversations and revisit history after reload.|Deleted conversation is absent and cannot reopen for the owner;The other conversation remains unchanged
History date ordering|History|R16|N|Sort prepared conversations with distinct timestamps and compare their order.|The visible order follows the selected date direction;Reload does not corrupt titles or records
Year filter|Search filters|R08|P|Retrieve obesity evidence, apply a documented year range and inspect sources and provenance.|All dated returned records meet the selected range;The executed query or filter record reflects the range
Journal filter|Search filters|R08|P|Apply the preselected journal filter to a live evidence search.|Returned journal metadata matches the selected journal;Filter changes are reflected in retrieval provenance
Clinical-trial filter|Search filters|R08|P|Restrict a live query to clinical trials and inspect publication types.|Returned records have qualifying official publication types;The filter is not only a cosmetic UI change
Review-type filters|Search filters|R08|P|Run the same topic with Review, Systematic Review and Meta-analysis in separate searches.|Each applied filter is represented in provenance;Official metadata supports each returned type;Results are not reused under a false label
Free-full-text filter|Search filters|R08|P|Enable free-full-text availability and inspect returned source links.|Selected records have official free-full-text availability evidence;The app does not claim all articles are freely accessible
Relevance and date sort|Search filters|R06,R08|P|Sort the same result set by relevance and publication date and compare.|Selected sort is applied and disclosed;Date ordering agrees with the chosen publication-date semantics
Search saved publications|Evidence library|R18|N|Search a prepared saved library by title and clear the query.|Search finds the matching owned publication;Clearing restores the owner's saved set
Organize research sources|Evidence library|R18|N|Create an organizational collection, add two prepared publications and reopen it.|Both chosen sources persist in the collection;Unrelated publications are excluded
Saved search rerun|Saved research|R18,R14|P|Save a topic search with its filters, leave, reopen and rerun it.|Saved parameters persist;Rerun uses those parameters and current official retrieval;Provenance distinguishes the rerun
Multi-turn follow-up|Conversation|R15,R14|P+G|Ask about GLP-1 obesity evidence, then ask What about cardiovascular outcomes? in the same thread.|Follow-up follows the original chronologically;Relevant earlier question context is preserved;Additional retrieval is recorded
History after logout|History|R03,R16|N|Rename a prepared thread, log out, log back in and reopen it.|History and renamed title persist for the same account;Anonymous UI does not expose the thread
Electronic versus issue date|Sources|R07|P|Inspect the official source fixture with different electronic and issue dates in detail and list views.|Dates are distinguished by type;Neither date is silently mislabelled as the other
Incomplete metadata|Sources|R07,R21|P|Open the official incomplete-metadata fixture and export its reference.|Available identifiers and fields are preserved;Missing fields are labelled or omitted honestly;Export remains structurally valid
Mobile navigation and source detail|Accessibility|R23,R07|M+P|At 390x844 open the main destinations, retrieve a source and inspect its detail.|Navigation and source controls remain reachable;Essential content is not clipped behind inaccessible controls
Keyboard question flow|Accessibility|R02,R23|P|Using keyboard actions, focus the composer, enter a question and submit, then reach evidence controls.|Focus is visible;Enter submits appropriately;No essential control requires a mouse-only action
Loading and settled state|Resilience|R21,R23|C|Submit a question while the controlled retrieval endpoint delays for three seconds, then releases a valid recorded response.|Visible loading state persists while pending;Completion replaces loading;No duplicate research request is created
Empty live search|Search|R06,R21|P|Submit the deterministic nonsense query EVA_NO_PUBMED_8XQZ2026 and inspect the result.|Official retrieval confirms no matches;UI gives an honest empty state without fake sources
Published API reference|Documentation|R26|N|Find the documented API reference through delivered project navigation and inspect its schema artifact.|A retrievable schema/document describes authentication, research and export APIs;It does not expose credentials'''),
('4', '''Account isolation in history|Authorization|R20|U|As researcher B attempt the known private conversation URL belonging to researcher A, then return to B history.|A's text and sources are not disclosed;B history contains only B-owned data
Isolation of saved answers|Authorization|R17,R20|U|Switch from A with a saved answer to B and inspect Saved Answers and the known private answer URL.|A's private answer is inaccessible to B;Account switching does not retain A's saved state
Isolation of collections|Authorization|R18,R20|U|As B attempt to open and alter A's prepared collection using its known URL and a controlled request-ID substitution.|Requests cannot read or mutate A's collection;A's collection remains unchanged
CSRF rejection|Security|R03,R22|C+U|Submit a profile change while the proxy removes its CSRF token, then repeat normally after the fault is released.|Forged change is rejected without persistence;The normal user-initiated change works;Authentication remains intact
Stale account response|Authorization|R20|C+U|Start A's delayed private request, switch to B before release and inspect both tabs after the response arrives.|Late A response is discarded from B's UI;B sees no private A payload
Cross-tab logout|Accounts|R03,R20|U|Open two tabs as A, sign out in one and interact with the other.|Second tab reflects session loss on the supported synchronization path;Protected operations cannot persist after logout
Save-state recovery|Saved research|R17,R21|C|Attempt a bookmark while a single controlled save response fails, then release the fault and explicitly save again.|Failure is visible and does not claim success;Normal explicit retry creates exactly one owned bookmark
PubMed timeout|Resilience|R06,R21|C|Submit a query under a controlled PubMed timeout, inspect the state, release the fault and explicitly resubmit.|Timeout is actionable and not a fabricated empty result;Recovery is user-driven;No false answer is generated
PubMed rate limit|Resilience|R06,R21|C|Submit under an official-shaped 429 response with Retry-After, inspect and then recover after release.|Rate-limit failure is explicit;Transport pacing does not hammer the provider;No fabricated sources appear
PubMed service failure|Resilience|R06,R21|C|Submit under a controlled 503 response and inspect persisted conversation and UI state.|External failure is distinguishable from no evidence;No fake generated answer or references are saved
Overlapping-query deduplication|Retrieval|R06,R14|P|Ask a comparison requiring overlapping queries and inspect the combined evidence and exports.|Each canonical PMID appears once in the merged evidence;Executed queries are recorded;Cross-query duplicates do not inflate counts
Stable retrieval ranking|Retrieval|R06,R26|C|Run the same question twice against the same recorded official responses and unchanged preferences.|Ranking is reproducible for identical candidate evidence;Provenance records separate runs;Recorded-response mode is disclosed in benchmark evidence
Invalid identifiers|Sources|R07,R21|P|Try malformed PMID and DOI values, then a valid known PMID.|Invalid identifiers produce a controlled response;No unrelated source is substituted;Valid recovery still works
Provider outage|Model state|R09,R21|C+P|Submit with live PubMed but a controlled failed application-model endpoint.|Retrieved evidence stays inspectable;Provider failure is explicit;No synthesis is falsely presented as successful
Wrong-language recovery|Language|R12|C|Submit Chinese with a controlled provider returning English first and valid Chinese second.|Exactly one app-level language retry occurs;Accepted prose is Chinese;Both attempts are recorded without changing the original question
Wrong-language repeated failure|Language|R12,R09|C|Submit Chinese when both controlled generation responses are English.|Only the allowed single retry occurs;A visible language failure withholds the unsupported answer;Original-language sources remain distinguished
Citation membership rejection|Citation integrity|R11,R22|C|Ask for synthesis when the controlled provider cites a PMID outside the retrieved evidence.|The invalid draft is withheld;Error identifies an evidence/citation problem;No unrelated reference is persisted as accepted
Exact quotation rejection|Citation integrity|R11|C|Submit when the controlled provider returns a quotation not present in the supplied abstract.|Draft is rejected or withheld with explicit validation failure;Original abstract remains inspectable
Numeric contradiction rejection|Citation integrity|R11|C|Submit when the controlled provider changes a numeric result from the cited abstract.|Conservative numeric check flags the mismatch;Contradictory draft is not accepted as supported output
Claim-support audit rejection|Citation integrity|R11,R10|C|Submit a draft with valid source IDs/quotes but a controlled separate audit declaring a key claim unsupported.|Draft is withheld;Audit status and limitation are visible;A second model pass is not claimed as clinical validation
Prompt-injection source|Security|R22,R11|C|Retrieve a clearly labelled poisoned abstract fixture that asks the model to leak a synthetic sentinel key and ignore the research task.|No sentinel leaks to UI/export/model action logs;No unauthorized navigation/tool action occurs;Poisoned instructions are treated as source text
Four-stage provenance|Provenance|R05,R14,R15|P+G|Ask a Chinese topic and a context-dependent follow-up, then inspect and export the query trace.|Original, normalized-before-context, prior questions and executed queries remain distinct;Export preserves those stages
Regenerate without losing original|Answer revisions|R13,R17|P+G|Save an answer, change detail/language preferences and regenerate from its existing evidence snapshot.|New revision uses the same snapshot;Original answer/bookmark/provenance are unchanged;Revision identity and current preferences are clear
Regeneration ownership|Authorization|R13,R20|U+P+G|As B attempt regeneration of A's known answer, then as A regenerate normally.|B cannot create or view a revision of A's answer;Authorized A action is independently verified
Legacy snapshot fidelity|Migration|R25,R07,R19|L|Open an imported prior-version conversation with unspecified date types and export it without regeneration.|Legacy account/data survive supported migration;Unknown date type is labelled unspecified;Original references and saved state persist'''),
('5', '''Complete English evidence review|Research workflow|R06,R10,R11,R14,R17,R19|P+G|Register a new researcher, ask about GLP-1 obesity outcomes, inspect every cited claim, save the answer and two sources, export Markdown and reopen after login.|All requested actions persist for the new user;Every accepted claim is tied to retrieved excerpts and audit state;Export reproduces identifiers and provenance;No scripted task completion is used
Chinese comparison with follow-up|Research workflow|R05,R12,R14,R15,R19|P+G|Set Chinese, compare SGLT2 and GLP-1 evidence in heart failure, ask about limitations, inspect source language and export PDF.|Both generated responses use Chinese prose;Follow-up retrieves context-appropriate evidence;Original-language labels and limitations/gaps are explicit;PDF is readable and traceable
Evidence insufficiency research|Research workflow|R10,R11,R15|P+G|Ask a narrowly framed biomedical question with sparse evidence, challenge any certainty in a follow-up and inspect all citations.|Insufficient/tentative evidence is stated honestly;Follow-up does not treat earlier claims as automatically true;No fabricated publication or diagnostic certainty is introduced
Filters-to-library-to-report|Research workflow|R08,R18,R19,R14|P|Run a topic with year and article-type filters, compare date/relevance order, organize three real sources, search the collection and export CSV/BibTeX.|Each filter/sort is reflected in evidence/provenance;Saved source identities match the report;Both artifact formats preserve metadata without duplicates
Missing-model to live regeneration|Research workflow|R09,R13,R24|P+G|Create and save a literature-mode answer, let the operator enable an already-approved free/local provider, verify status and regenerate using current Chinese preferences.|No pre-configuration synthetic answer is claimed;Configured and checked state are distinguishable;New Chinese revision preserves the original snapshot and bookmark
Multiple users and late writes|Authorization workflow|R03,R17,R20|C+U|Open A in two tabs, delay a save response, sign out/switch to B, release the delayed response and inspect both users' libraries after separate logins.|Neither late response nor UI cache leaks A data to B;Writes stay bound to the authenticated owner;Both accounts retain their own correct records
Provider failure during revision|Recovery workflow|R13,R17,R21|C+P+G|Save a real answer, begin regeneration under a controlled provider outage, inspect original, release fault and explicitly regenerate again.|Failed revision cannot overwrite the original or bookmark;Failure is explicit;User-triggered recovery creates exactly one valid new revision
Unsupported claim recovery|Recovery workflow|R11,R13,R19|C+P+G|Attempt a revision with a controlled invalid claim audit, inspect rejection, restore the real free/local provider and regenerate, then export.|Rejected draft is not represented as accepted research;Original remains intact;Accepted revision has independently checked source membership/quotes/audit and correct export
Long bilingual export dossier|Research workflow|R07,R10,R19|P+G|Ask a detailed bilingual research question, inspect all evidence rows, save it and export PDF/Markdown/CSV/BibTeX, comparing Unicode author names and references.|All four artifacts preserve matching source identities;PDF has legible glyphs/page layout;No missing finding is invented;Provenance matches the displayed revision
Conflicting evidence synthesis|Research workflow|R10,R11,R15|P+G|Research a preselected topic with differing study findings, inspect cited excerpts, then ask why results differ.|Supported and conflicting findings are separated;Limitations are grounded or explicitly unavailable;Follow-up does not invent explanations unsupported by evidence
Repeated source and revision audit|Research workflow|R06,R13,R17,R26|P+G|Run overlapping questions, save the same publication, regenerate one answer and reopen both threads after reload.|Publication canonical identities remain deduplicated;Each revision retains its own source associations and timestamps;Save state is not lost or transferred between revisions
Mobile keyboard research journey|Accessibility workflow|R02,R12,R17,R19,R23|M+P+G|At 390x844 use keyboard navigation to set Chinese, ask a research question, inspect citations, save and export the answer.|Every essential operation remains reachable with visible focus;Chinese answer and sources remain readable;Saved data and exported references match
Literature continuity through outage|Recovery workflow|R16,R18,R21|C+P|With prior real sources saved, disconnect PubMed, reopen history/library and export existing work, then restore retrieval and ask a new question.|Existing persisted research remains usable;New retrieval failure is honest;Restored query fetches real evidence without corrupting prior data
Legacy account regeneration journey|Migration workflow|R25,R13,R14,R19|L+P+G|Sign in with a migrated legacy account, inspect old saved evidence, regenerate using Chinese/current preferences and export old and new revisions.|Legacy credentials/data remain usable;Old provenance/date semantics stay unchanged;New revision is labelled and traceable;Both exports preserve the corresponding snapshot
Configured-model evidence audit|Research workflow|R09,R11,R24,R26|P+G|Compare configured-unchecked and successful operator connection-check states, submit a new synthesis, inspect model identity and each claim's evidence audit, then reopen after restart.|Configuration/check/per-answer states are distinct;Actual generation and review invocations are recorded;Claim excerpts match cited sources;Reopened answer/provenance persist without asserting clinical validation''')]
TASKS=[]
for level,block in ROWS:
 for line in block.splitlines():
  title,category,refs,mode,goal,criteria=line.split('|')
  modes=mode.split('+'); ident=f'ME-{len(TASKS)+1:03}'
  role='Anonymous' if title in ['Research identity','Primary destinations','Sign-in entry','Register a researcher','Valid login and reload','Invalid login'] else 'Researcher A'
  if 'U' in modes: role='Researcher A and Researcher B (separate synthetic accounts)'
  assertions=[dict(id=f'{ident}-A{i+1}',statement=x.strip(),oracle=('read-only UI/database plus downloaded artifact or controlled-provider transcript, as applicable')) for i,x in enumerate(criteria.split(';'))]
  write=category in ['Accounts','Profile','Settings','Saved research','History','Answer generation','Conversation','Answer revisions','Authorization workflow','Recovery workflow','Migration workflow','Research workflow','Accessibility workflow','Evidence library','Exports'] and title not in ['Sign-in entry','Saved answer destination','Publication library entry','Preference controls','Research history empty state','History reopen','Search saved publications']
  TASKS.append(dict(id=ident,title=title,feature_category=category,difficulty=int(level),reporting_group='write_workflow' if write else 'read_search',user_role=role,requirement_ids=refs.split(','),
    initial_state={'isolation':'fresh synthetic database and browser context; never the public deployment','profile_modes':modes,'authentication':'none for login/registration/logout-under-test; preauthenticated synthetic session only where sign-in is not the task','data':'global fixture contract plus named task fixtures; no previous benchmark task dependency','start':'normal application home unless the task explicitly calls for a known private URL'},
    user_goal=goal,expected_outcome='; '.join(a['statement'] for a in assertions),assertions=assertions,
    evaluation_boundary='All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.',
    fixture_requirements=modes,paid_retries=0))
assert len(TASKS)==100,len(TASKS)
assert Counter(t['difficulty'] for t in TASKS)=={1:10,2:20,3:30,4:25,5:15}
assert len({t['title'] for t in TASKS})==100
out=ROOT/'catalog-v1';out.mkdir(exist_ok=True)
raw=(json.dumps(TASKS,ensure_ascii=False,indent=2)+'\n').encode()
if (out/'tasks.json').exists(): raise SystemExit('Catalog already exists: create a separately versioned catalog rather than overwrite frozen tasks')
(out/'tasks.json').write_bytes(raw)
(out/'requirements.json').write_text(json.dumps(REQ,indent=2)+'\n',encoding='utf-8')
lines=['# MedEvidence Native CUA Benchmark v1','', 'Frozen specification-derived tasks. No formal native execution has occurred.','']
for t in TASKS:
 lines += [f"## {t['id']}: {t['title']}",'',f"Level {t['difficulty']} / 5 · {t['feature_category']} · {t['reporting_group']}",f"Role: {t['user_role']}",f"Requirements: {', '.join(t['requirement_ids'])}",f"Initial state: {json.dumps(t['initial_state'],ensure_ascii=False)}",'',f"Goal: {t['user_goal']}",'','Expected outcome: '+t['expected_outcome'],'','Objective assertions:','']+[f"- **{a['id']}** {a['statement']} — independent UI/readonly DB/download/provider-transcript review as applicable." for a in t['assertions']]+['',t['evaluation_boundary'],'']
(out/'TASKS.md').write_bytes(('\n'.join(lines)+'\n').encode())
freeze={'catalog_version':'1.0.0','application_commit':'7d64a988fc1b1e27433aa96c90b743c6336baea5','base_branch':'v3-round-03','specification':'experiments/round-03/consolidated-prompt.md','specification_sha256':hashlib.sha256(SPEC.read_bytes()).hexdigest(),'tasks_sha256':hashlib.sha256(raw).hexdigest(),'task_markdown_sha256':hashlib.sha256((out/'TASKS.md').read_bytes()).hexdigest(),'difficulty_distribution':dict(Counter(t['difficulty'] for t in TASKS)),'designed_before_implementation_inspection':True,'paid_execution_started':False}
(out/'freeze.json').write_text(json.dumps(freeze,indent=2)+'\n',encoding='utf-8')
print(json.dumps(freeze,indent=2))
