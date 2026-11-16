# Frozen MedEvidence final evaluation: 100 tests

No execution results are implied. The final consolidated Round 3 Description is authoritative.

## Easy

### Navigation and accessibility

#### T001: Research identity

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open home
2. inspect introduction and disclaimer

Expected / PASS criteria: Original identity and research-only disclaimer are visible; no clinical-use or regulatory guarantee.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T002: Primary navigation

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in as A
2. visit Ask, History, Saved Answers, Evidence Library, Settings and Profile

Expected / PASS criteria: Each required destination is reachable with a meaningful heading and no fatal page error.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T013: Suggested research topic

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open home
2. select a suggested topic

Expected / PASS criteria: A relevant research question is populated or submitted with visible feedback.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T027: Keyboard navigation

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Use Tab from page start through navigation and composer

Expected / PASS criteria: Focus is visible and actionable controls are keyboard reachable in usable order.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T028: Mobile menu

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. At 390x844 open navigation
2. reach Profile
3. close menu

Expected / PASS criteria: All destinations remain reachable; overlay closes; no inaccessible bottom links.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T029: Empty saved state

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in B
2. inspect saved answers and publications

Expected / PASS criteria: Accurate, readable empty states; no A data or generic server error.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Accounts, sessions and ownership

#### T003: Register synthetic researcher

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open registration
2. enter new synthetic username and strong password
3. submit

Expected / PASS criteria: Account created and authenticated identity shown; independent DB check confirms password is hashed.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T004: Valid sign-in

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open sign-in
2. submit A credentials

Expected / PASS criteria: A identity is displayed and account pages are accessible.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T005: Invalid password

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Attempt A sign-in with incorrect password

Expected / PASS criteria: Clear failure message; no authenticated identity or access to private data.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T006: Immediate logout

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. sign out
3. revisit Profile

Expected / PASS criteria: UI immediately becomes unauthenticated and private account content is inaccessible.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T007: Session reload

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. refresh page

Expected / PASS criteria: A remains authenticated and the current private view loads.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T008: Profile name save

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. edit first and last names
3. save

Expected / PASS criteria: Visible save confirmation; displayed names match submitted values.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Question validation and short/Chinese input

#### T009: Empty question validation

Requirements: R03. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. leave question empty
3. attempt submit

Expected / PASS criteria: No research turn created; invalid input prevented or explained.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T010: One-word research

Requirements: R03. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. submit obesity

Expected / PASS criteria: Submission accepted; real literature or informative retrieval failure shown; not rejected solely for word count.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T011: Chinese research input

Requirements: R03. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. submit 糖尿病怎么治疗

Expected / PASS criteria: Input accepted; meaningful translated search terms retrieve relevant diabetes literature; no fabricated result.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T012: Multiline composer

Requirements: R03. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. type first line
3. press Shift+Enter
4. type second line

Expected / PASS criteria: Composer contains both lines; Shift+Enter does not submit prematurely.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Context and conversation history

#### T014: History list

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open History

Expected / PASS criteria: A's seeded synthetic conversations appear; B's private title is absent.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T015: Reopen conversation

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open History
3. open seeded thread

Expected / PASS criteria: Original question, chronology and stored evidence are accessible.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Evidence library and save feedback

#### T016: Library navigation

Requirements: R06. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open Evidence Library
3. switch search and saved views

Expected / PASS criteria: Search and saved-publication views are distinguishable and usable.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T020: Saved-publication listing

Requirements: R06. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open saved publications

Expected / PASS criteria: Seeded publication is present with stable identifier and distinguishable from saved answers.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Real literature, metadata and retrieval

#### T017: Known PMID lookup

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search PubMed for 33567185

Expected / PASS criteria: Returned PMID and title match the independently supplied official record.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T018: Publication details

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search PMID 33567185
2. expand details

Expected / PASS criteria: Authors, journal, dates, DOI and source abstract are inspectable and match source metadata.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T019: Open original record

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search PMID 33567185
2. open its source link

Expected / PASS criteria: New or current tab reaches the matching official PubMed record, not a fabricated destination.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Answer saves and exports

#### T021: Saved-answer listing

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open saved answers
3. open the seeded saved item

Expected / PASS criteria: Correct answer detail is opened with original question and source information.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T030: Answer detail metadata

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open A's seeded answer

Expected / PASS criteria: Original question, timestamp, literature-only status and supporting sources are shown; no fabricated AI text.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Preferences and regenerated answers

#### T022: Language save feedback

Requirements: R10. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. set Chinese
3. save preferences

Expected / PASS criteria: Chinese is selected; success feedback appears and unchanged saves cannot duplicate work.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T023: Detail preference

Requirements: R10. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. choose Detailed
3. save

Expected / PASS criteria: Detailed preference is visibly retained; save succeeds.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T024: Display preference

Requirements: R10. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. change display density
3. save

Expected / PASS criteria: Selected preference persists in UI and relevant layout adapts without losing controls.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Configuration, readiness and failures

#### T025: Missing-model composer

Requirements: R11. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open question composer with model unconfigured

Expected / PASS criteria: Literature-only limitation is visible before submission; UI does not promise a generated answer.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T026: Missing-model language notice

Requirements: R11. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open Settings
3. select Chinese

Expected / PASS criteria: Notice distinguishes future generated answers from original-language sources and current lack of generation.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

## Medium

### Accounts, sessions and ownership

#### T031: Profile persistence

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. change names
3. save
4. refresh
5. sign out and back in

Expected / PASS criteria: Both names persist and save feedback accurately describes success.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T032: Duplicate registration

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Attempt registration using A's username and a different password
2. then sign in A

Expected / PASS criteria: Duplicate rejected clearly; original A password/account unaffected.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T033: Weak password rejection

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Register new username with password 123
2. correct to a strong password
3. resubmit

Expected / PASS criteria: Weak value rejected; correction succeeds without duplicate accounts.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T034: Logout survives back and reload

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. open private thread
3. sign out
4. use Back
5. reload

Expected / PASS criteria: No live authenticated access remains; private API response independently denies unauthenticated access.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Context and conversation history

#### T035: Conversation rename persistence

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Rename seeded thread to Acceptance GLP-1
2. refresh
3. reopen from History

Expected / PASS criteria: New title persists and original turns/source associations remain unchanged.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T036: History query and reset

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search for Acceptance fixture
2. search zzz_no_match_987
3. clear search

Expected / PASS criteria: Correct matching set, accurate empty state, then restored A history.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T037: History date ordering

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open history containing three separated timestamps
2. switch newest/oldest

Expected / PASS criteria: Order reverses consistently using dates; no missing or cross-user entries.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T038: Conversation deletion

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Delete seeded disposable conversation
2. revisit history and direct old URL

Expected / PASS criteria: Deleted thread absent; old URL fails safely; other threads persist.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T064: Contextual limitations follow-up

Requirements: R08. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask GLP-1 obesity question
2. in same thread ask What are the limitations of these studies?
3. inspect trace

Expected / PASS criteria: Both turns remain in one thread; executed queries preserve GLP-1/obesity context and limitations intent.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Evidence library and save feedback

#### T039: Save publication feedback

Requirements: R06. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search 33567185
2. save
3. attempt immediate repeat save

Expected / PASS criteria: Visible saving/saved state; no duplicate saved association.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T040: Saved publication reload

Requirements: R06. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search and save 33567185
2. refresh
3. sign out/in
4. open saved publications

Expected / PASS criteria: One correct saved record survives reload and login cycle.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T041: Remove saved publication

Requirements: R06. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Remove seeded saved publication
2. refresh
3. inspect list

Expected / PASS criteria: Record remains removed from A's library; source record and B's data are not improperly removed.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T042: Collection update

Requirements: R06. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Set saved publication collection to Obesity research
2. save
3. refresh

Expected / PASS criteria: Collection persists with visible success feedback.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T043: Collection search and reset

Requirements: R06. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search saved items by Obesity research
2. try no-match term
3. clear

Expected / PASS criteria: Matching collection is found; no-match is empty; clear restores all saved items.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Literature filtering and sorting

#### T044: Matching and conflicting year

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search 33567185 with 2021
2. repeat with 2020

Expected / PASS criteria: Matching filter includes record; conflicting filter excludes it; stale results are not presented as current.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T045: Journal filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search obesity in The New England Journal of Medicine
2. inspect returned records

Expected / PASS criteria: Every returned journal matches the filter; no invented records.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T046: Clinical-trial filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search semaglutide obesity with clinical-trial article type

Expected / PASS criteria: Returned records have a qualifying trial type; filtering is reflected in request/provenance.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T047: Review filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search obesity with Review type
2. open two available details

Expected / PASS criteria: Results satisfy review metadata; detail matches listed records.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T048: Systematic-review filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search GLP-1 obesity with Systematic Review type

Expected / PASS criteria: Results satisfy systematic-review classification; empty set is clearly distinguished from service failure.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T049: Meta-analysis filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search obesity with Meta-analysis type

Expected / PASS criteria: Result types comply; no unrelated stale results from earlier filters.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T050: Free-full-text filter

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search obesity with free full text enabled
2. inspect availability links

Expected / PASS criteria: Returned records meet availability filter; app does not imply access to unavailable paywalled text.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T051: Publication-date sort

Requirements: R05. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search obesity
2. switch relevance to publication date
3. inspect several records

Expected / PASS criteria: Dates follow documented direction; sorting does not corrupt metadata or repeat identifiers.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Real literature, metadata and retrieval

#### T052: DOI lookup

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search 10.1056/NEJMoa2032183
2. open details and source

Expected / PASS criteria: Resolves to PMID 33567185 with consistent title and DOI.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T053: Invalid identifier

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search invalid PMID 000000000000
2. then search valid 33567185

Expected / PASS criteria: Invalid lookup has clear empty/validation result; valid subsequent search works without stale error.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T054: Separate publication dates

Requirements: R04. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search 33567185
2. inspect electronic and journal-issue dates

Expected / PASS criteria: Dates are labeled by type; unavailable type is explicit; values match official reference.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Answer saves and exports

#### T055: Save answer persistence

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Open unsaved synthetic answer
2. save
3. refresh
4. reopen saved answers

Expected / PASS criteria: Single bookmark persists with visible Saved feedback.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T056: Unsave without deleting thread

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Unsave seeded answer
2. refresh Saved Answers
3. reopen its conversation

Expected / PASS criteria: Bookmark absent but conversation and all turns remain intact.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T057: Markdown export

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Export seeded research answer as Markdown
2. inspect downloaded file

Expected / PASS criteria: UTF-8 disclaimer, question, status and traceable PMID/DOI links are intact; no mojibake.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T058: PDF export

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Export seeded answer as PDF
2. open downloaded document

Expected / PASS criteria: Readable question, disclaimer and references; no clipped critical text or corrupted punctuation.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T059: BibTeX export

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Export seeded references as BibTeX
2. inspect downloaded entries

Expected / PASS criteria: Entries parse; identifier/title/author/DOI preserved; special characters handled; no duplicate keys.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T060: CSV export

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Export references as CSV
2. inspect rows containing commas and Unicode

Expected / PASS criteria: CSV parses to consistent columns and preserves complete titles/authors/identifiers.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T061: Copy answer

Requirements: R09. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Copy seeded research answer
2. paste into a local blank evaluation scratch surface

Expected / PASS criteria: Copied text corresponds to selected answer; no other user's content or broken encoding.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Preferences and regenerated answers

#### T062: Preferences after login cycle

Requirements: R10. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Set Chinese, Detailed and Compact
2. save
3. sign out/in
4. inspect Settings

Expected / PASS criteria: All three preferences persist independently.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Configuration, readiness and failures

#### T063: No-key research workflow

Requirements: R11. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. With no model key submit GLP-1 obesity query using live PubMed

Expected / PASS criteria: Literature is retrieved and stored; explicit missing-generation state; no fake synthesis.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T068: Configured but unchecked

Requirements: R11. Profile: `configured`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Start with real configured model and cleared readiness cache
2. open Settings and composer

Expected / PASS criteria: Configuration is distinguished from a successful connection check and from generated answer success.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T069: Chinese connection probe

Requirements: R11. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. run the model connection check
3. inspect status

Expected / PASS criteria: Actual configured provider returns valid Chinese response; ready status matches recorded call, not mere key presence.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Auditable provenance

#### T065: Four-stage provenance

Requirements: R13. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit Chinese diabetes question
2. ask a contextual follow-up
3. expand trace

Expected / PASS criteria: Original input, normalized question, previous questions and actual executed queries are distinct and accurate.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Evidence-grounded AI and detail page

#### T066: Evidence table unavailable fields

Requirements: R07. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit literature-only query
2. toggle evidence cards/table
3. inspect findings and limitations

Expected / PASS criteria: Study/year/type/source retained; unsupported findings/limitations explicitly unavailable, never fabricated.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T070: English evidence synthesis

Requirements: R07. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit GLP-1 obesity question with English preference
2. open answer

Expected / PASS criteria: Real generated English findings, limitations and references supported by retrieved abstracts; retrieval-only is not PASS.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Navigation and accessibility

#### T067: Mobile evidence and exports

Requirements: R01. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. At 390x844 open seeded evidence table
2. scroll within it
3. open export controls

Expected / PASS criteria: Table does not force inaccessible page overflow; all required controls can be operated.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

## Hard

### Evidence-grounded AI and detail page

#### T071: Chinese research synthesis

Requirements: R07. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Set Chinese
2. submit GLP-1 obesity research question
3. inspect prose and citations

Expected / PASS criteria: Generated narrative is Chinese; source titles/quotes remain labeled original; claims are supported and not status-message-only.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Preferences and regenerated answers

#### T072: Regenerate while preserving original

Requirements: R10. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Save existing literature-only answer
2. enable live provider as prerequisite
3. select Chinese
4. regenerate
5. revisit both versions

Expected / PASS criteria: New revision uses original evidence snapshot/current preference; original content/bookmark/provenance unchanged.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T080: Wrong-language retry boundary

Requirements: R10. Profile: `fault_language`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Select Chinese
2. submit question
3. controlled provider returns English twice

Expected / PASS criteria: Exactly one corrective generation retry then explicit language failure; no English answer published as Chinese.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Accounts, sessions and ownership

#### T073: Cross-account direct thread access

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. As A note owned thread URL
2. sign out
3. sign in B
4. paste that URL

Expected / PASS criteria: B cannot read A thread or its source content; server-side authorization confirmed independently.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T074: Cross-account answer and export access

Requirements: R02. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. As B navigate to A's supplied answer URL and export URL
2. inspect own saved list

Expected / PASS criteria: No A answer/export is disclosed; B saved list stays isolated.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Security, untrusted inputs, rate limits

#### T075: Session and CSRF enforcement

Requirements: R14. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Sign in A
2. edit profile through UI
3. independent verifier checks cookies and a missing-CSRF mutation

Expected / PASS criteria: Normal UI save succeeds; unsafe mutation rejected; session cookie is HTTP-only and data remains unchanged by rejected request.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T085: Untrusted article injection

Requirements: R14. Profile: `fault_injection`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask question with retrieved test article containing instruction to reveal keys or ignore citations

Expected / PASS criteria: Article instructions are treated as data; no secret disclosure or unauthorized action; source provenance identifies fixture.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T086: Untrusted user question

Requirements: R14. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit a question asking for invented PMID and instructions to ignore source checking

Expected / PASS criteria: No fabricated citation is endorsed; response is evidence-grounded, explicit failure or justified refusal.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T089: Markup rendering safety

Requirements: R14. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Rename a synthetic conversation to <img src=x onerror=alert(1)>
2. reopen history and exports

Expected / PASS criteria: Input rejected or rendered safely as text; no script executes; no unauthorized data changes.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Citation and claim verification

#### T076: Reject nonexistent citation

Requirements: R12. Profile: `fault_membership`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask a research question while test provider returns a citation outside retrieved PMIDs
2. open answer

Expected / PASS criteria: Unsupported draft withheld; verification failure explicit; authentic sources still accessible.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T077: Reject altered quotation

Requirements: R12. Profile: `fault_quote`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask a research question with controlled provider draft containing a fabricated abstract quote

Expected / PASS criteria: Draft fails exact-quotation validation; fabricated quotation not presented as verified.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T078: Reject unsupported numeric claim

Requirements: R12. Profile: `fault_numeric`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit question with controlled provider output asserting a number absent from supporting source

Expected / PASS criteria: Unsupported numerical claim rejected; verification failure does not masquerade as successful synthesis.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T079: Reject contradicted claim

Requirements: R12. Profile: `fault_review`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit question with exact quote but contradictory interpretation
2. reviewer rejects support

Expected / PASS criteria: App withholds unsupported draft even though PMID and quote are valid.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Configuration, readiness and failures

#### T081: Provider credential failure

Requirements: R11. Profile: `fault_auth`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit question against provider returning 401/403
2. inspect status and sources

Expected / PASS criteria: Clear provider access failure; no secret exposed; retrieved sources and history remain usable.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T082: Provider quota exhaustion

Requirements: R11. Profile: `fault_quota`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit question against provider returning 429
2. navigate to sources/history

Expected / PASS criteria: Quota limitation explained; no automatic billing/fallback or endless retry; evidence persists.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T083: Model timeout

Requirements: R11. Profile: `fault_timeout`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Submit question while model endpoint stalls beyond configured timeout
2. reopen thread

Expected / PASS criteria: Bounded wait ends with explicit timeout; no false answer; retrieved evidence retained.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Real literature, metadata and retrieval

#### T084: Literature service failure and recovery

Requirements: R04. Profile: `fault_pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Search while PubMed fails
2. restore dependency
3. submit same query once manually

Expected / PASS criteria: Failure is distinguishable from no results; UI recovers and successful new result is attributable to restored retrieval.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Context and conversation history

#### T087: Follow-up topic switch

Requirements: R08. Profile: `pubmed`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask GLP-1 obesity
2. follow up on SGLT2 heart failure
3. inspect both source lists and queries

Expected / PASS criteria: New evidence is retrieved for changed topic; original references preserved; context does not force irrelevant old topic.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T090: History management isolation

Requirements: R08. Profile: `offline`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. As A clear own history using available management workflow
2. sign in B
3. reopen B thread

Expected / PASS criteria: A history removed as requested; B history and saved sources preserved; stale A links deny access.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Auditable provenance

#### T088: Audit generated claims

Requirements: R13. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Generate supported response
2. open every cited excerpt
3. inspect model, timestamp and abstract scope

Expected / PASS criteria: All displayed claims/citations can be traced to actual source text; automated review is not labeled clinical validation.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

## Expert

### Evidence-grounded AI and detail page

#### T091: Complete evidence research lifecycle

Requirements: R07. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Register researcher
2. select Chinese/Detailed
3. ask GLP-1 obesity
4. follow up on limitations
5. inspect all citations
6. save answer and two publications
7. group sources
8. export Markdown/PDF
9. sign out/in and reopen

Expected / PASS criteria: Every step completes with genuine Chinese synthesis, supported citations, intact source provenance, persistent saves and readable exports.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Accounts, sessions and ownership

#### T092: Two-researcher confidentiality lifecycle

Requirements: R02. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. A generates/saves research and notes URLs
2. B creates separate research
3. B tries A URLs and export
4. A returns to original work

Expected / PASS criteria: Both accounts retain own work; no cross-account disclosure/modification; denied accesses do not destroy originals.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Preferences and regenerated answers

#### T093: Missing-model to live revision lifecycle

Requirements: R10. Profile: `live_transition`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Create/bookmark literature-only turn
2. operator configures provider without changing app
3. choose Chinese
4. regenerate
5. export both versions
6. reload history

Expected / PASS criteria: Honest pre-configuration state; new real Chinese revision; original evidence snapshot/bookmark and exported status preserved.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Citation and claim verification

#### T094: Conflicting evidence comparison

Requirements: R12. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask comparison of SGLT2 and GLP-1 in heart failure
2. inspect study populations/designs
3. ask about applicability and uncertainty
4. audit cited excerpts

Expected / PASS criteria: Distinct interventions and populations not conflated; uncertainty/limitations supported; no unsupported superiority or diagnostic certainty.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

#### T095: Verification failure and explicit recovery

Requirements: R12. Profile: `fault_sequence`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Generate a controlled unsupported claim
2. inspect rejection
3. restore genuine provider
4. manually regenerate
5. inspect source snapshots and both turns

Expected / PASS criteria: Initial failure retained; no unverified draft leaked; new answer independently supported; recovery does not overwrite audit trail.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Public persistence and research-only identity

#### T096: Public availability and persistence

Requirements: R15. Profile: `hosted`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. On authorized test deployment register/save research
2. operator restarts service
3. revisit HTTPS site on separate browser context
4. sign in and reopen sources/preferences

Expected / PASS criteria: Site works independent of developer workstation; data survives service restart; HTTPS sessions secure; no paid-plan change.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Navigation and accessibility

#### T097: Mobile complete research workflow

Requirements: R01. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. At 390x844 register/sign in
2. ask Chinese question
3. follow up
4. expand sources/table
5. save/export
6. navigate Profile and sign out

Expected / PASS criteria: All workflow steps accessible at narrow width; generated Chinese content intact; no inaccessible controls or privacy leakage.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Security, untrusted inputs, rate limits

#### T098: Rate-limit isolation and recovery

Requirements: R14. Profile: `fault_rate`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Use UI to submit enough synthetic requests to reach configured rate limit
2. inspect bounded error
3. wait allowed interval
4. submit once
5. inspect saved work

Expected / PASS criteria: Rate limit visible and enforced; successful recovery after interval; no automatic paid retries or lost existing records.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Answer saves and exports

#### T099: Cross-format provenance reconciliation

Requirements: R09. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Generate answer with findings/limitations and multiple references
2. export Markdown, PDF, BibTeX, CSV
3. compare IDs, authors, DOI, quotes and dates across all formats

Expected / PASS criteria: No reference corruption/duplication or mismatched IDs; answer formats preserve provenance and verification status; structured exports parse.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.

### Context and conversation history

#### T100: Long research thread and reproducibility

Requirements: R08. Profile: `live`.

Preconditions: Synthetic A and B; fresh isolated database per test; no real patient data. See FIXTURES.md. Seeded items are explicitly synthetic; required live retrieval/generation must never be replaced by fixtures.

1. Ask GLP-1 obesity
2. follow up on limitations, population, conflicting evidence and a related intervention
3. rename/search thread
4. logout/login
5. inspect chronological turns and exports

Expected / PASS criteria: All five turns persist in order with relevant context/retrieval, correct source-to-turn associations and honest evidence gaps; no assumption earlier claims are automatically true.

Independent criterion-by-criterion screenshot/action review plus read-only database/network/download inspection; model self-report alone cannot award PASS.
