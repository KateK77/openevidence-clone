"""Design source. Run only before execution; frozen artifacts are the authority."""
import json, hashlib, subprocess
from pathlib import Path
from collections import Counter
HERE=Path(__file__).resolve().parent
REQ={
 'R01':('Navigation and accessibility','Original sections 1, 5; V2 item 9'),
 'R02':('Accounts, sessions and ownership','Original sections 13, 19; V3 item 8'),
 'R03':('Question validation and short/Chinese input','Original sections 5, 6; V2 items 3, 4'),
 'R04':('Real literature, metadata and retrieval','Original sections 7, 8; V2 item 8'),
 'R05':('Literature filtering and sorting','Original section 12'),
 'R06':('Evidence library and save feedback','Original section 11; V2 items 5, 6'),
 'R07':('Evidence-grounded AI and detail page','Original sections 6, 9; V3 items 5, 6'),
 'R08':('Context and conversation history','Original sections 10, 14; V3 items 7, 8'),
 'R09':('Answer saves and exports','Original sections 9, 15; V2 items 5, 7'),
 'R10':('Preferences and regenerated answers','Original section 16; V3 items 3, 4'),
 'R11':('Configuration, readiness and failures','Original section 20; V3 items 1, 2'),
 'R12':('Citation and claim verification','Original sections 6, 8, 19; V3 items 5, 6'),
 'R13':('Auditable provenance','Original section 17; V3 item 7'),
 'R14':('Security, untrusted inputs, rate limits','Original sections 13, 19, 21'),
 'R15':('Public persistence and research-only identity','Authorized public hosting follow-up; Original sections 1, 19'),
}
# Difficulty, requirement, profile, title | expected user workflow | objective criteria.
# Profile describes prerequisites, never a replacement for a required live service.
DATA=r'''
Easy|R01|offline|Research identity|Open home; inspect introduction and disclaimer|Original identity and research-only disclaimer are visible; no clinical-use or regulatory guarantee.
Easy|R01|offline|Primary navigation|Sign in as A; visit Ask, History, Saved Answers, Evidence Library, Settings and Profile|Each required destination is reachable with a meaningful heading and no fatal page error.
Easy|R02|offline|Register synthetic researcher|Open registration; enter new synthetic username and strong password; submit|Account created and authenticated identity shown; independent DB check confirms password is hashed.
Easy|R02|offline|Valid sign-in|Open sign-in; submit A credentials|A identity is displayed and account pages are accessible.
Easy|R02|offline|Invalid password|Attempt A sign-in with incorrect password|Clear failure message; no authenticated identity or access to private data.
Easy|R02|offline|Immediate logout|Sign in A; sign out; revisit Profile|UI immediately becomes unauthenticated and private account content is inaccessible.
Easy|R02|offline|Session reload|Sign in A; refresh page|A remains authenticated and the current private view loads.
Easy|R02|offline|Profile name save|Sign in A; edit first and last names; save|Visible save confirmation; displayed names match submitted values.
Easy|R03|offline|Empty question validation|Sign in A; leave question empty; attempt submit|No research turn created; invalid input prevented or explained.
Easy|R03|pubmed|One-word research|Sign in A; submit obesity|Submission accepted; real literature or informative retrieval failure shown; not rejected solely for word count.
Easy|R03|pubmed|Chinese research input|Sign in A; submit 糖尿病怎么治疗|Input accepted; meaningful translated search terms retrieve relevant diabetes literature; no fabricated result.
Easy|R03|offline|Multiline composer|Sign in A; type first line; press Shift+Enter; type second line|Composer contains both lines; Shift+Enter does not submit prematurely.
Easy|R01|offline|Suggested research topic|Open home; select a suggested topic|A relevant research question is populated or submitted with visible feedback.
Easy|R08|offline|History list|Sign in A; open History|A's seeded synthetic conversations appear; B's private title is absent.
Easy|R08|offline|Reopen conversation|Sign in A; open History; open seeded thread|Original question, chronology and stored evidence are accessible.
Easy|R06|offline|Library navigation|Sign in A; open Evidence Library; switch search and saved views|Search and saved-publication views are distinguishable and usable.
Easy|R04|pubmed|Known PMID lookup|Search PubMed for 33567185|Returned PMID and title match the independently supplied official record.
Easy|R04|pubmed|Publication details|Search PMID 33567185; expand details|Authors, journal, dates, DOI and source abstract are inspectable and match source metadata.
Easy|R04|pubmed|Open original record|Search PMID 33567185; open its source link|New or current tab reaches the matching official PubMed record, not a fabricated destination.
Easy|R06|offline|Saved-publication listing|Sign in A; open saved publications|Seeded publication is present with stable identifier and distinguishable from saved answers.
Easy|R09|offline|Saved-answer listing|Sign in A; open saved answers; open the seeded saved item|Correct answer detail is opened with original question and source information.
Easy|R10|offline|Language save feedback|Sign in A; set Chinese; save preferences|Chinese is selected; success feedback appears and unchanged saves cannot duplicate work.
Easy|R10|offline|Detail preference|Sign in A; choose Detailed; save|Detailed preference is visibly retained; save succeeds.
Easy|R10|offline|Display preference|Sign in A; change display density; save|Selected preference persists in UI and relevant layout adapts without losing controls.
Easy|R11|offline|Missing-model composer|Open question composer with model unconfigured|Literature-only limitation is visible before submission; UI does not promise a generated answer.
Easy|R11|offline|Missing-model language notice|Sign in A; open Settings; select Chinese|Notice distinguishes future generated answers from original-language sources and current lack of generation.
Easy|R01|offline|Keyboard navigation|Use Tab from page start through navigation and composer|Focus is visible and actionable controls are keyboard reachable in usable order.
Easy|R01|offline|Mobile menu|At 390x844 open navigation; reach Profile; close menu|All destinations remain reachable; overlay closes; no inaccessible bottom links.
Easy|R01|offline|Empty saved state|Sign in B; inspect saved answers and publications|Accurate, readable empty states; no A data or generic server error.
Easy|R09|offline|Answer detail metadata|Open A's seeded answer|Original question, timestamp, literature-only status and supporting sources are shown; no fabricated AI text.
Medium|R02|offline|Profile persistence|Sign in A; change names; save; refresh; sign out and back in|Both names persist and save feedback accurately describes success.
Medium|R02|offline|Duplicate registration|Attempt registration using A's username and a different password; then sign in A|Duplicate rejected clearly; original A password/account unaffected.
Medium|R02|offline|Weak password rejection|Register new username with password 123; correct to a strong password; resubmit|Weak value rejected; correction succeeds without duplicate accounts.
Medium|R02|offline|Logout survives back and reload|Sign in A; open private thread; sign out; use Back; reload|No live authenticated access remains; private API response independently denies unauthenticated access.
Medium|R08|offline|Conversation rename persistence|Rename seeded thread to Acceptance GLP-1; refresh; reopen from History|New title persists and original turns/source associations remain unchanged.
Medium|R08|offline|History query and reset|Search for Acceptance fixture; search zzz_no_match_987; clear search|Correct matching set, accurate empty state, then restored A history.
Medium|R08|offline|History date ordering|Open history containing three separated timestamps; switch newest/oldest|Order reverses consistently using dates; no missing or cross-user entries.
Medium|R08|offline|Conversation deletion|Delete seeded disposable conversation; revisit history and direct old URL|Deleted thread absent; old URL fails safely; other threads persist.
Medium|R06|pubmed|Save publication feedback|Search 33567185; save; attempt immediate repeat save|Visible saving/saved state; no duplicate saved association.
Medium|R06|pubmed|Saved publication reload|Search and save 33567185; refresh; sign out/in; open saved publications|One correct saved record survives reload and login cycle.
Medium|R06|offline|Remove saved publication|Remove seeded saved publication; refresh; inspect list|Record remains removed from A's library; source record and B's data are not improperly removed.
Medium|R06|offline|Collection update|Set saved publication collection to Obesity research; save; refresh|Collection persists with visible success feedback.
Medium|R06|offline|Collection search and reset|Search saved items by Obesity research; try no-match term; clear|Matching collection is found; no-match is empty; clear restores all saved items.
Medium|R05|pubmed|Matching and conflicting year|Search 33567185 with 2021; repeat with 2020|Matching filter includes record; conflicting filter excludes it; stale results are not presented as current.
Medium|R05|pubmed|Journal filter|Search obesity in The New England Journal of Medicine; inspect returned records|Every returned journal matches the filter; no invented records.
Medium|R05|pubmed|Clinical-trial filter|Search semaglutide obesity with clinical-trial article type|Returned records have a qualifying trial type; filtering is reflected in request/provenance.
Medium|R05|pubmed|Review filter|Search obesity with Review type; open two available details|Results satisfy review metadata; detail matches listed records.
Medium|R05|pubmed|Systematic-review filter|Search GLP-1 obesity with Systematic Review type|Results satisfy systematic-review classification; empty set is clearly distinguished from service failure.
Medium|R05|pubmed|Meta-analysis filter|Search obesity with Meta-analysis type|Result types comply; no unrelated stale results from earlier filters.
Medium|R05|pubmed|Free-full-text filter|Search obesity with free full text enabled; inspect availability links|Returned records meet availability filter; app does not imply access to unavailable paywalled text.
Medium|R05|pubmed|Publication-date sort|Search obesity; switch relevance to publication date; inspect several records|Dates follow documented direction; sorting does not corrupt metadata or repeat identifiers.
Medium|R04|pubmed|DOI lookup|Search 10.1056/NEJMoa2032183; open details and source|Resolves to PMID 33567185 with consistent title and DOI.
Medium|R04|pubmed|Invalid identifier|Search invalid PMID 000000000000; then search valid 33567185|Invalid lookup has clear empty/validation result; valid subsequent search works without stale error.
Medium|R04|pubmed|Separate publication dates|Search 33567185; inspect electronic and journal-issue dates|Dates are labeled by type; unavailable type is explicit; values match official reference.
Medium|R09|offline|Save answer persistence|Open unsaved synthetic answer; save; refresh; reopen saved answers|Single bookmark persists with visible Saved feedback.
Medium|R09|offline|Unsave without deleting thread|Unsave seeded answer; refresh Saved Answers; reopen its conversation|Bookmark absent but conversation and all turns remain intact.
Medium|R09|offline|Markdown export|Export seeded research answer as Markdown; inspect downloaded file|UTF-8 disclaimer, question, status and traceable PMID/DOI links are intact; no mojibake.
Medium|R09|offline|PDF export|Export seeded answer as PDF; open downloaded document|Readable question, disclaimer and references; no clipped critical text or corrupted punctuation.
Medium|R09|offline|BibTeX export|Export seeded references as BibTeX; inspect downloaded entries|Entries parse; identifier/title/author/DOI preserved; special characters handled; no duplicate keys.
Medium|R09|offline|CSV export|Export references as CSV; inspect rows containing commas and Unicode|CSV parses to consistent columns and preserves complete titles/authors/identifiers.
Medium|R09|offline|Copy answer|Copy seeded research answer; paste into a local blank evaluation scratch surface|Copied text corresponds to selected answer; no other user's content or broken encoding.
Medium|R10|offline|Preferences after login cycle|Set Chinese, Detailed and Compact; save; sign out/in; inspect Settings|All three preferences persist independently.
Medium|R11|pubmed|No-key research workflow|With no model key submit GLP-1 obesity query using live PubMed|Literature is retrieved and stored; explicit missing-generation state; no fake synthesis.
Medium|R08|pubmed|Contextual limitations follow-up|Ask GLP-1 obesity question; in same thread ask What are the limitations of these studies?; inspect trace|Both turns remain in one thread; executed queries preserve GLP-1/obesity context and limitations intent.
Medium|R13|pubmed|Four-stage provenance|Submit Chinese diabetes question; ask a contextual follow-up; expand trace|Original input, normalized question, previous questions and actual executed queries are distinct and accurate.
Medium|R07|pubmed|Evidence table unavailable fields|Submit literature-only query; toggle evidence cards/table; inspect findings and limitations|Study/year/type/source retained; unsupported findings/limitations explicitly unavailable, never fabricated.
Medium|R01|offline|Mobile evidence and exports|At 390x844 open seeded evidence table; scroll within it; open export controls|Table does not force inaccessible page overflow; all required controls can be operated.
Medium|R11|configured|Configured but unchecked|Start with real configured model and cleared readiness cache; open Settings and composer|Configuration is distinguished from a successful connection check and from generated answer success.
Medium|R11|live|Chinese connection probe|Sign in A; run the model connection check; inspect status|Actual configured provider returns valid Chinese response; ready status matches recorded call, not mere key presence.
Medium|R07|live|English evidence synthesis|Submit GLP-1 obesity question with English preference; open answer|Real generated English findings, limitations and references supported by retrieved abstracts; retrieval-only is not PASS.
Hard|R07|live|Chinese research synthesis|Set Chinese; submit GLP-1 obesity research question; inspect prose and citations|Generated narrative is Chinese; source titles/quotes remain labeled original; claims are supported and not status-message-only.
Hard|R10|live|Regenerate while preserving original|Save existing literature-only answer; enable live provider as prerequisite; select Chinese; regenerate; revisit both versions|New revision uses original evidence snapshot/current preference; original content/bookmark/provenance unchanged.
Hard|R02|offline|Cross-account direct thread access|As A note owned thread URL; sign out; sign in B; paste that URL|B cannot read A thread or its source content; server-side authorization confirmed independently.
Hard|R02|offline|Cross-account answer and export access|As B navigate to A's supplied answer URL and export URL; inspect own saved list|No A answer/export is disclosed; B saved list stays isolated.
Hard|R14|offline|Session and CSRF enforcement|Sign in A; edit profile through UI; independent verifier checks cookies and a missing-CSRF mutation|Normal UI save succeeds; unsafe mutation rejected; session cookie is HTTP-only and data remains unchanged by rejected request.
Hard|R12|fault_membership|Reject nonexistent citation|Ask a research question while test provider returns a citation outside retrieved PMIDs; open answer|Unsupported draft withheld; verification failure explicit; authentic sources still accessible.
Hard|R12|fault_quote|Reject altered quotation|Ask a research question with controlled provider draft containing a fabricated abstract quote|Draft fails exact-quotation validation; fabricated quotation not presented as verified.
Hard|R12|fault_numeric|Reject unsupported numeric claim|Submit question with controlled provider output asserting a number absent from supporting source|Unsupported numerical claim rejected; verification failure does not masquerade as successful synthesis.
Hard|R12|fault_review|Reject contradicted claim|Submit question with exact quote but contradictory interpretation; reviewer rejects support|App withholds unsupported draft even though PMID and quote are valid.
Hard|R10|fault_language|Wrong-language retry boundary|Select Chinese; submit question; controlled provider returns English twice|Exactly one corrective generation retry then explicit language failure; no English answer published as Chinese.
Hard|R11|fault_auth|Provider credential failure|Submit question against provider returning 401/403; inspect status and sources|Clear provider access failure; no secret exposed; retrieved sources and history remain usable.
Hard|R11|fault_quota|Provider quota exhaustion|Submit question against provider returning 429; navigate to sources/history|Quota limitation explained; no automatic billing/fallback or endless retry; evidence persists.
Hard|R11|fault_timeout|Model timeout|Submit question while model endpoint stalls beyond configured timeout; reopen thread|Bounded wait ends with explicit timeout; no false answer; retrieved evidence retained.
Hard|R04|fault_pubmed|Literature service failure and recovery|Search while PubMed fails; restore dependency; submit same query once manually|Failure is distinguishable from no results; UI recovers and successful new result is attributable to restored retrieval.
Hard|R14|fault_injection|Untrusted article injection|Ask question with retrieved test article containing instruction to reveal keys or ignore citations|Article instructions are treated as data; no secret disclosure or unauthorized action; source provenance identifies fixture.
Hard|R14|pubmed|Untrusted user question|Submit a question asking for invented PMID and instructions to ignore source checking|No fabricated citation is endorsed; response is evidence-grounded, explicit failure or justified refusal.
Hard|R08|pubmed|Follow-up topic switch|Ask GLP-1 obesity; follow up on SGLT2 heart failure; inspect both source lists and queries|New evidence is retrieved for changed topic; original references preserved; context does not force irrelevant old topic.
Hard|R13|live|Audit generated claims|Generate supported response; open every cited excerpt; inspect model, timestamp and abstract scope|All displayed claims/citations can be traced to actual source text; automated review is not labeled clinical validation.
Hard|R14|offline|Markup rendering safety|Rename a synthetic conversation to <img src=x onerror=alert(1)>; reopen history and exports|Input rejected or rendered safely as text; no script executes; no unauthorized data changes.
Hard|R08|offline|History management isolation|As A clear own history using available management workflow; sign in B; reopen B thread|A history removed as requested; B history and saved sources preserved; stale A links deny access.
Expert|R07|live|Complete evidence research lifecycle|Register researcher; select Chinese/Detailed; ask GLP-1 obesity; follow up on limitations; inspect all citations; save answer and two publications; group sources; export Markdown/PDF; sign out/in and reopen|Every step completes with genuine Chinese synthesis, supported citations, intact source provenance, persistent saves and readable exports.
Expert|R02|live|Two-researcher confidentiality lifecycle|A generates/saves research and notes URLs; B creates separate research; B tries A URLs and export; A returns to original work|Both accounts retain own work; no cross-account disclosure/modification; denied accesses do not destroy originals.
Expert|R10|live_transition|Missing-model to live revision lifecycle|Create/bookmark literature-only turn; operator configures provider without changing app; choose Chinese; regenerate; export both versions; reload history|Honest pre-configuration state; new real Chinese revision; original evidence snapshot/bookmark and exported status preserved.
Expert|R12|live|Conflicting evidence comparison|Ask comparison of SGLT2 and GLP-1 in heart failure; inspect study populations/designs; ask about applicability and uncertainty; audit cited excerpts|Distinct interventions and populations not conflated; uncertainty/limitations supported; no unsupported superiority or diagnostic certainty.
Expert|R12|fault_sequence|Verification failure and explicit recovery|Generate a controlled unsupported claim; inspect rejection; restore genuine provider; manually regenerate; inspect source snapshots and both turns|Initial failure retained; no unverified draft leaked; new answer independently supported; recovery does not overwrite audit trail.
Expert|R15|hosted|Public availability and persistence|On authorized test deployment register/save research; operator restarts service; revisit HTTPS site on separate browser context; sign in and reopen sources/preferences|Site works independent of developer workstation; data survives service restart; HTTPS sessions secure; no paid-plan change.
Expert|R01|live|Mobile complete research workflow|At 390x844 register/sign in; ask Chinese question; follow up; expand sources/table; save/export; navigate Profile and sign out|All workflow steps accessible at narrow width; generated Chinese content intact; no inaccessible controls or privacy leakage.
Expert|R14|fault_rate|Rate-limit isolation and recovery|Use UI to submit enough synthetic requests to reach configured rate limit; inspect bounded error; wait allowed interval; submit once; inspect saved work|Rate limit visible and enforced; successful recovery after interval; no automatic paid retries or lost existing records.
Expert|R09|live|Cross-format provenance reconciliation|Generate answer with findings/limitations and multiple references; export Markdown, PDF, BibTeX, CSV; compare IDs, authors, DOI, quotes and dates across all formats|No reference corruption/duplication or mismatched IDs; answer formats preserve provenance and verification status; structured exports parse.
Expert|R08|live|Long research thread and reproducibility|Ask GLP-1 obesity; follow up on limitations, population, conflicting evidence and a related intervention; rename/search thread; logout/login; inspect chronological turns and exports|All five turns persist in order with relevant context/retrieval, correct source-to-turn associations and honest evidence gaps; no assumption earlier claims are automatically true.
'''
def build():
    if (HERE/'freeze.json').exists(): raise SystemExit('Suite already frozen; never overwrite it after inspection/execution.')
    tests=[]
    for line in DATA.strip().splitlines():
        difficulty,req,profile,title,workflow,criteria=line.split('|')
        tests.append({'id':f'T{len(tests)+1:03}','difficulty':difficulty,'functional_category':REQ[req][0],
          'requirement_ids':[req],'title':title,'task':title+': '+workflow+'.',
          'preconditions':{'profile':profile,'accounts':'Synthetic A and B; fresh isolated database per test; no real patient data.',
            'data':'See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.'},
          'expected_workflow':[x.strip() for x in workflow.split(';')],
          'expected_result':criteria,'pass_fail_criteria':[x.strip().rstrip('.') for x in criteria.split(';')],
          'verification':'Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.'})
    assert Counter(t['difficulty'] for t in tests)=={'Easy':30,'Medium':40,'Hard':20,'Expert':10},Counter(t['difficulty'] for t in tests)
    assert len({t['title'] for t in tests})==100
    write=lambda p,v:(HERE/p).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write('requirements.json',{k:{'requirement':v[0],'source_section':v[1]} for k,v in REQ.items()})
    write('final_test_cases_100.json',{'specification':'FINAL_DESCRIPTION.md','tests':tests})
    text='# Frozen MedEvidence final evaluation: 100 tests\n\nNo execution results are implied. The final consolidated Round 3 Description is authoritative.\n'
    for difficulty in ['Easy','Medium','Hard','Expert']:
        text+='\n## '+difficulty+'\n'
        for category in dict.fromkeys(t['functional_category'] for t in tests if t['difficulty']==difficulty):
            text+='\n### '+category+'\n'
            for t in tests:
                if t['difficulty']!=difficulty or t['functional_category']!=category:continue
                text+=f'\n#### {t["id"]}: {t["title"]}\n\nRequirements: {", ".join(t["requirement_ids"])}. Profile: `{t["preconditions"]["profile"]}`.\n\nPreconditions: {t["preconditions"]["accounts"]} {t["preconditions"]["data"]}\n\n'
                text+='\n'.join(f'{i}. {s}' for i,s in enumerate(t['expected_workflow'],1))
                text+='\n\nExpected / PASS criteria: '+t['expected_result']+'\n\n'+t['verification']+'\n'
    (HERE/'FINAL_TEST_CASES.md').write_text(text,encoding='utf-8')
    write('final_results_100.json',{'execution_started':False,'paid_requests':0,'estimated_api_cost_usd':0,'tests':[{'id':t['id'],'difficulty':t['difficulty'],'status':'NOT_RUN','reason':'Paid native CUA execution has not been approved.','model_requests':0,'actions':0,'input_tokens':0,'output_tokens':0,'estimated_cost_usd':0,'evidence':[]} for t in tests]})
    files=['FINAL_DESCRIPTION.md','requirements.json','final_test_cases_100.json','FINAL_TEST_CASES.md','FIXTURES.md']
    write('freeze.json',{'application_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=HERE,text=True).strip(), 'files':{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest() for p in files},'distribution':dict(Counter(t['difficulty'] for t in tests)),'no_paid_execution':True})
if __name__=='__main__':build()
