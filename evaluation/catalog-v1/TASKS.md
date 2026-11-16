# MedEvidence Native CUA Benchmark v1

Frozen specification-derived tasks. No formal native execution has occurred.

## ME-001: Research identity

Level 1 / 5 · Navigation · read_search
Role: Anonymous
Requirements: R01
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open the landing page and inspect the identity and research boundary.

Expected outcome: Research demonstration disclaimer is visible; Branding is independent and does not claim OpenEvidence affiliation

Objective assertions:

- **ME-001-A1** Research demonstration disclaimer is visible — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-001-A2** Branding is independent and does not claim OpenEvidence affiliation — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-002: Primary destinations

Level 1 / 5 · Navigation · read_search
Role: Anonymous
Requirements: R02
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Locate Ask AI, Research History, Saved Answers, Evidence Library, Settings and Profile; open each destination.

Expected outcome: All six destinations are discoverable and reachable or request authentication; No navigation ends in a broken page

Objective assertions:

- **ME-002-A1** All six destinations are discoverable and reachable or request authentication — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-002-A2** No navigation ends in a broken page — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-003: Composer multiline

Level 1 / 5 · Composer · read_search
Role: Researcher A
Requirements: R02
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Focus the medical question input and insert a second line with Shift+Enter without submitting.

Expected outcome: Input contains both lines; No question submission occurs on Shift+Enter

Objective assertions:

- **ME-003-A1** Input contains both lines — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-003-A2** No question submission occurs on Shift+Enter — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-004: Example question entry

Level 1 / 5 · Composer · read_search
Role: Researcher A
Requirements: R02
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Choose an example research question and inspect the resulting editable question.

Expected outcome: Chosen example fills or starts the corresponding question flow; The displayed question matches the chosen topic

Objective assertions:

- **ME-004-A1** Chosen example fills or starts the corresponding question flow — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-004-A2** The displayed question matches the chosen topic — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-005: Sign-in entry

Level 1 / 5 · Accounts · read_search
Role: Anonymous
Requirements: R03
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open the sign-in entry and inspect the form and account-registration route.

Expected outcome: Username and masked password controls have labels; An account-registration route is available

Objective assertions:

- **ME-005-A1** Username and masked password controls have labels — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-005-A2** An account-registration route is available — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-006: Saved answer destination

Level 1 / 5 · Saved research · read_search
Role: Researcher A
Requirements: R17
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open Saved Answers with an empty authenticated fixture.

Expected outcome: Destination is clearly identified as saved answers; Empty state is honest and offers usable navigation

Objective assertions:

- **ME-006-A1** Destination is clearly identified as saved answers — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-006-A2** Empty state is honest and offers usable navigation — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-007: Publication library entry

Level 1 / 5 · Evidence library · read_search
Role: Researcher A
Requirements: R18
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open Evidence Library with an empty authenticated fixture.

Expected outcome: Publication destination is distinct from Saved Answers; No fictitious saved publication appears

Objective assertions:

- **ME-007-A1** Publication destination is distinct from Saved Answers — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-007-A2** No fictitious saved publication appears — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-008: Preference controls

Level 1 / 5 · Settings · read_search
Role: Researcher A
Requirements: R04
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open Settings and inspect language, display and answer-detail choices.

Expected outcome: Required language/display/detail preferences are discoverable; Any unavailable model selection is clearly bounded

Objective assertions:

- **ME-008-A1** Required language/display/detail preferences are discoverable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-008-A2** Any unavailable model selection is clearly bounded — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-009: Missing-model notice

Level 1 / 5 · Model state · read_search
Role: Researcher A
Requirements: R09, R24
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Inspect the composer and language preference while no application model is configured.

Expected outcome: Both surfaces explain unavailable generation; Literature mode is not represented as a generated answer

Objective assertions:

- **ME-009-A1** Both surfaces explain unavailable generation — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-009-A2** Literature mode is not represented as a generated answer — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-010: Research history empty state

Level 1 / 5 · History · read_search
Role: Researcher A
Requirements: R16, R23
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open a new researcher's history.

Expected outcome: No other user's history is displayed; Empty state is understandable and navigable

Objective assertions:

- **ME-010-A1** No other user's history is displayed — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-010-A2** Empty state is understandable and navigable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-011: Register a researcher

Level 2 / 5 · Accounts · write_workflow
Role: Anonymous
Requirements: R03
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Register a new synthetic username with a valid unique password, then sign in.

Expected outcome: Exactly one usable account is created; Successful login establishes the new identity

Objective assertions:

- **ME-011-A1** Exactly one usable account is created — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-011-A2** Successful login establishes the new identity — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-012: Valid login and reload

Level 2 / 5 · Accounts · write_workflow
Role: Anonymous
Requirements: R03
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Sign in to the prepared account and reload its profile.

Expected outcome: Identity remains authenticated after reload; No unrelated account data appears

Objective assertions:

- **ME-012-A1** Identity remains authenticated after reload — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-012-A2** No unrelated account data appears — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-013: Invalid login

Level 2 / 5 · Accounts · write_workflow
Role: Anonymous
Requirements: R03, R22
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Attempt login using the prepared username and a wrong password.

Expected outcome: Authentication is rejected visibly; No authenticated session or private content is granted

Objective assertions:

- **ME-013-A1** Authentication is rejected visibly — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-013-A2** No authenticated session or private content is granted — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-014: Logout persistence

Level 2 / 5 · Accounts · write_workflow
Role: Researcher A
Requirements: R03
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Sign out, reload and open a private destination.

Expected outcome: UI immediately reflects sign-out; Reload does not restore the prior session

Objective assertions:

- **ME-014-A1** UI immediately reflects sign-out — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-014-A2** Reload does not restore the prior session — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-015: Profile save persistence

Level 2 / 5 · Profile · write_workflow
Role: Researcher A
Requirements: R04, R17
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Change an editable profile value, save it and reload.

Expected outcome: Success is visible; The persisted value matches the submitted change

Objective assertions:

- **ME-015-A1** Success is visible — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-015-A2** The persisted value matches the submitted change — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-016: Language preference persistence

Level 2 / 5 · Settings · write_workflow
Role: Researcher A
Requirements: R04, R09
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Choose Chinese, save and reload with no model configured.

Expected outcome: Chinese preference persists; UI explains that preference alone does not enable synthesis

Objective assertions:

- **ME-016-A1** Chinese preference persists — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-016-A2** UI explains that preference alone does not enable synthesis — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-017: Detail preference persistence

Level 2 / 5 · Settings · write_workflow
Role: Researcher A
Requirements: R04
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Change response detail level, save, navigate away and return.

Expected outcome: Selected level persists; Preference applies to future generation rather than silently rewriting prior answers

Objective assertions:

- **ME-017-A1** Selected level persists — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-017-A2** Preference applies to future generation rather than silently rewriting prior answers — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-018: Whitespace rejection

Level 2 / 5 · Composer · read_search
Role: Researcher A
Requirements: R05, R22
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit a whitespace-only question.

Expected outcome: A visible validation response is shown; No research conversation or provider request is created

Objective assertions:

- **ME-018-A1** A visible validation response is shown — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-018-A2** No research conversation or provider request is created — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-019: Single-character query

Level 2 / 5 · Search · read_search
Role: Researcher A
Requirements: R05, R06
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit the non-whitespace query x and inspect completion state.

Expected outcome: Query is accepted rather than rejected solely for length one; Sources or an honest empty result are shown

Objective assertions:

- **ME-019-A1** Query is accepted rather than rejected solely for length one — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-019-A2** Sources or an honest empty result are shown — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-020: Chinese glossary query

Level 2 / 5 · Search · read_search
Role: Researcher A
Requirements: R05, R14
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit 糖尿病 and inspect query provenance.

Expected outcome: Original Chinese question is retained; Executed English mapping is disclosed and relates to the term

Objective assertions:

- **ME-020-A1** Original Chinese question is retained — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-020-A2** Executed English mapping is disclosed and relates to the term — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-021: Unsupported Chinese mapping

Level 2 / 5 · Search · read_search
Role: Researcher A
Requirements: R05, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit an unsupported Chinese term 量子香蕉综合征 and inspect the response.

Expected outcome: An actionable unsupported-mapping message appears; It is not falsely reported as a definitive zero-evidence search

Objective assertions:

- **ME-021-A1** An actionable unsupported-mapping message appears — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-021-A2** It is not falsely reported as a definitive zero-evidence search — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-022: Live obesity literature

Level 2 / 5 · Search · read_search
Role: Researcher A
Requirements: R06, R09
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask for evidence on GLP-1 receptor agonists in obesity in literature mode.

Expected outcome: At least one retrieved PMID resolves in official response evidence; No canned generated answer is substituted

Objective assertions:

- **ME-022-A1** At least one retrieved PMID resolves in official response evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-022-A2** No canned generated answer is substituted — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-023: PMID source resolution

Level 2 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Resolve PMID 31452104 using the available publication/search flow and open its detail.

Expected outcome: Displayed identifier matches the requested PMID; Title and DOI agree with the independently captured official record

Objective assertions:

- **ME-023-A1** Displayed identifier matches the requested PMID — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-023-A2** Title and DOI agree with the independently captured official record — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-024: DOI source resolution

Level 2 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Resolve DOI 10.1007/978-1-4939-9752-7_10 and inspect the source.

Expected outcome: The resolved article matches the DOI; No duplicate identity is created for the same PMID

Objective assertions:

- **ME-024-A1** The resolved article matches the DOI — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-024-A2** No duplicate identity is created for the same PMID — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-025: Open official source

Level 2 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: From a retrieved article open its original PubMed link.

Expected outcome: Navigation reaches the matching official PMID record; The original article detail remains recoverable

Objective assertions:

- **ME-025-A1** Navigation reaches the matching official PMID record — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-025-A2** The original article detail remains recoverable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-026: Missing abstract disclosure

Level 2 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07, R10
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open the preselected official publication that has no abstract.

Expected outcome: Missing abstract is stated explicitly; No abstract text or extracted findings are invented

Objective assertions:

- **ME-026-A1** Missing abstract is stated explicitly — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-026-A2** No abstract text or extracted findings are invented — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-027: Card and table views

Level 2 / 5 · Evidence presentation · read_search
Role: Researcher A
Requirements: R07, R10
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Switch a completed literature-only evidence set between cards and table.

Expected outcome: Both views represent the same source identities; Unextracted findings and limitations are marked unavailable

Objective assertions:

- **ME-027-A1** Both views represent the same source identities — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-027-A2** Unextracted findings and limitations are marked unavailable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-028: Save a publication

Level 2 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R17, R18
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save one retrieved publication and reopen Saved Publications.

Expected outcome: Save progress or completion is visible; Exactly one owned saved entry exists

Objective assertions:

- **ME-028-A1** Save progress or completion is visible — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-028-A2** Exactly one owned saved entry exists — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-029: Remove saved publication

Level 2 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R18
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Remove the prepared saved publication and reload the saved list.

Expected outcome: Saved relationship is removed persistently; Unrelated saved entries remain

Objective assertions:

- **ME-029-A1** Saved relationship is removed persistently — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-029-A2** Unrelated saved entries remain — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-030: History reopen

Level 2 / 5 · History · read_search
Role: Researcher A
Requirements: R15, R16
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open a prepared research conversation from history.

Expected outcome: The correct question and chronology are shown; Persisted source associations are retained

Objective assertions:

- **ME-030-A1** The correct question and chronology are shown — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-030-A2** Persisted source associations are retained — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-031: New English synthesis

Level 3 / 5 · Answer generation · write_workflow
Role: Researcher A
Requirements: R06, R10, R11
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask What evidence supports GLP-1 receptor agonists for obesity? and inspect the completed answer and sources.

Expected outcome: Answer is generated by the configured real provider; Each displayed reference belongs to the retrieved evidence; Abstract-only basis is disclosed

Objective assertions:

- **ME-031-A1** Answer is generated by the configured real provider — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-031-A2** Each displayed reference belongs to the retrieved evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-031-A3** Abstract-only basis is disclosed — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-032: Chinese synthesis

Level 3 / 5 · Answer generation · write_workflow
Role: Researcher A
Requirements: R04, R10, R12
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Set Chinese and submit 糖尿病药物的心血管获益有哪些证据？; inspect answer and original sources.

Expected outcome: Generated explanatory prose is Chinese; Source quotations and titles remain explicitly original-language; Sources map to retrieved records

Objective assertions:

- **ME-032-A1** Generated explanatory prose is Chinese — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-032-A2** Source quotations and titles remain explicitly original-language — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-032-A3** Sources map to retrieved records — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-033: Copy an answer

Level 3 / 5 · Exports · write_workflow
Role: Researcher A
Requirements: R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Copy the prepared clearly labelled synthetic answer and paste into the evaluation clipboard viewer.

Expected outcome: Clipboard contains that answer's text and traceable references; No unrelated user's content is copied

Objective assertions:

- **ME-033-A1** Clipboard contains that answer's text and traceable references — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-033-A2** No unrelated user's content is copied — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-034: Markdown export

Level 3 / 5 · Exports · write_workflow
Role: Researcher A
Requirements: R14, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Export the prepared bilingual answer as Markdown and inspect the downloaded artifact.

Expected outcome: Chinese characters round-trip in UTF-8; Answer and source identifiers are present; Provenance stages remain distinguishable

Objective assertions:

- **ME-034-A1** Chinese characters round-trip in UTF-8 — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-034-A2** Answer and source identifiers are present — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-034-A3** Provenance stages remain distinguishable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-035: PDF export

Level 3 / 5 · Exports · write_workflow
Role: Researcher A
Requirements: R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Export the prepared bilingual answer as PDF and inspect rendered pages.

Expected outcome: Chinese and Latin text render without replacement glyphs; Headings/page numbering are readable; References remain traceable

Objective assertions:

- **ME-035-A1** Chinese and Latin text render without replacement glyphs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-035-A2** Headings/page numbering are readable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-035-A3** References remain traceable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-036: BibTeX export

Level 3 / 5 · Exports · write_workflow
Role: Researcher A
Requirements: R07, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Export a prepared answer's references as BibTeX.

Expected outcome: Artifact parses as BibTeX; Entries match referenced PMIDs/DOIs and Unicode authors; Unavailable fields are not fabricated

Objective assertions:

- **ME-036-A1** Artifact parses as BibTeX — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-036-A2** Entries match referenced PMIDs/DOIs and Unicode authors — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-036-A3** Unavailable fields are not fabricated — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-037: CSV export

Level 3 / 5 · Exports · write_workflow
Role: Researcher A
Requirements: R07, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Export a prepared evidence set as CSV and inspect it in the independent parser.

Expected outcome: UTF-8 content survives parsing; Rows and identifiers match the set; Chinese content is legible in the documented spreadsheet encoding

Objective assertions:

- **ME-037-A1** UTF-8 content survives parsing — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-037-A2** Rows and identifiers match the set — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-037-A3** Chinese content is legible in the documented spreadsheet encoding — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-038: Save answer and reload

Level 3 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R17
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save a prepared answer, reload and reopen it from Saved Answers.

Expected outcome: One owned bookmark persists; The saved item opens the exact answer revision

Objective assertions:

- **ME-038-A1** One owned bookmark persists — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-038-A2** The saved item opens the exact answer revision — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-039: Duplicate-save prevention

Level 3 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R17
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save an unchanged prepared answer twice using available controls, then revisit Saved Answers.

Expected outcome: Pending or unchanged state prevents duplicate submission; Only one bookmark exists; UI shows an accurate saved state

Objective assertions:

- **ME-039-A1** Pending or unchanged state prevents duplicate submission — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-039-A2** Only one bookmark exists — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-039-A3** UI shows an accurate saved state — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-040: History rename and search

Level 3 / 5 · History · write_workflow
Role: Researcher A
Requirements: R16
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Rename the prepared conversation to EVA obesity review, reload and find it by that title.

Expected outcome: New title persists; History search returns the intended conversation without unrelated rows

Objective assertions:

- **ME-040-A1** New title persists — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-040-A2** History search returns the intended conversation without unrelated rows — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-041: Delete a conversation

Level 3 / 5 · History · write_workflow
Role: Researcher A
Requirements: R16
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Delete one of two prepared conversations and revisit history after reload.

Expected outcome: Deleted conversation is absent and cannot reopen for the owner; The other conversation remains unchanged

Objective assertions:

- **ME-041-A1** Deleted conversation is absent and cannot reopen for the owner — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-041-A2** The other conversation remains unchanged — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-042: History date ordering

Level 3 / 5 · History · write_workflow
Role: Researcher A
Requirements: R16
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Sort prepared conversations with distinct timestamps and compare their order.

Expected outcome: The visible order follows the selected date direction; Reload does not corrupt titles or records

Objective assertions:

- **ME-042-A1** The visible order follows the selected date direction — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-042-A2** Reload does not corrupt titles or records — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-043: Year filter

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Retrieve obesity evidence, apply a documented year range and inspect sources and provenance.

Expected outcome: All dated returned records meet the selected range; The executed query or filter record reflects the range

Objective assertions:

- **ME-043-A1** All dated returned records meet the selected range — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-043-A2** The executed query or filter record reflects the range — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-044: Journal filter

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Apply the preselected journal filter to a live evidence search.

Expected outcome: Returned journal metadata matches the selected journal; Filter changes are reflected in retrieval provenance

Objective assertions:

- **ME-044-A1** Returned journal metadata matches the selected journal — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-044-A2** Filter changes are reflected in retrieval provenance — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-045: Clinical-trial filter

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Restrict a live query to clinical trials and inspect publication types.

Expected outcome: Returned records have qualifying official publication types; The filter is not only a cosmetic UI change

Objective assertions:

- **ME-045-A1** Returned records have qualifying official publication types — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-045-A2** The filter is not only a cosmetic UI change — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-046: Review-type filters

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Run the same topic with Review, Systematic Review and Meta-analysis in separate searches.

Expected outcome: Each applied filter is represented in provenance; Official metadata supports each returned type; Results are not reused under a false label

Objective assertions:

- **ME-046-A1** Each applied filter is represented in provenance — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-046-A2** Official metadata supports each returned type — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-046-A3** Results are not reused under a false label — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-047: Free-full-text filter

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Enable free-full-text availability and inspect returned source links.

Expected outcome: Selected records have official free-full-text availability evidence; The app does not claim all articles are freely accessible

Objective assertions:

- **ME-047-A1** Selected records have official free-full-text availability evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-047-A2** The app does not claim all articles are freely accessible — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-048: Relevance and date sort

Level 3 / 5 · Search filters · read_search
Role: Researcher A
Requirements: R06, R08
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Sort the same result set by relevance and publication date and compare.

Expected outcome: Selected sort is applied and disclosed; Date ordering agrees with the chosen publication-date semantics

Objective assertions:

- **ME-048-A1** Selected sort is applied and disclosed — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-048-A2** Date ordering agrees with the chosen publication-date semantics — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-049: Search saved publications

Level 3 / 5 · Evidence library · read_search
Role: Researcher A
Requirements: R18
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Search a prepared saved library by title and clear the query.

Expected outcome: Search finds the matching owned publication; Clearing restores the owner's saved set

Objective assertions:

- **ME-049-A1** Search finds the matching owned publication — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-049-A2** Clearing restores the owner's saved set — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-050: Organize research sources

Level 3 / 5 · Evidence library · write_workflow
Role: Researcher A
Requirements: R18
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Create an organizational collection, add two prepared publications and reopen it.

Expected outcome: Both chosen sources persist in the collection; Unrelated publications are excluded

Objective assertions:

- **ME-050-A1** Both chosen sources persist in the collection — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-050-A2** Unrelated publications are excluded — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-051: Saved search rerun

Level 3 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R18, R14
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save a topic search with its filters, leave, reopen and rerun it.

Expected outcome: Saved parameters persist; Rerun uses those parameters and current official retrieval; Provenance distinguishes the rerun

Objective assertions:

- **ME-051-A1** Saved parameters persist — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-051-A2** Rerun uses those parameters and current official retrieval — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-051-A3** Provenance distinguishes the rerun — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-052: Multi-turn follow-up

Level 3 / 5 · Conversation · write_workflow
Role: Researcher A
Requirements: R15, R14
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask about GLP-1 obesity evidence, then ask What about cardiovascular outcomes? in the same thread.

Expected outcome: Follow-up follows the original chronologically; Relevant earlier question context is preserved; Additional retrieval is recorded

Objective assertions:

- **ME-052-A1** Follow-up follows the original chronologically — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-052-A2** Relevant earlier question context is preserved — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-052-A3** Additional retrieval is recorded — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-053: History after logout

Level 3 / 5 · History · write_workflow
Role: Researcher A
Requirements: R03, R16
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Rename a prepared thread, log out, log back in and reopen it.

Expected outcome: History and renamed title persist for the same account; Anonymous UI does not expose the thread

Objective assertions:

- **ME-053-A1** History and renamed title persist for the same account — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-053-A2** Anonymous UI does not expose the thread — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-054: Electronic versus issue date

Level 3 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Inspect the official source fixture with different electronic and issue dates in detail and list views.

Expected outcome: Dates are distinguished by type; Neither date is silently mislabelled as the other

Objective assertions:

- **ME-054-A1** Dates are distinguished by type — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-054-A2** Neither date is silently mislabelled as the other — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-055: Incomplete metadata

Level 3 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open the official incomplete-metadata fixture and export its reference.

Expected outcome: Available identifiers and fields are preserved; Missing fields are labelled or omitted honestly; Export remains structurally valid

Objective assertions:

- **ME-055-A1** Available identifiers and fields are preserved — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-055-A2** Missing fields are labelled or omitted honestly — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-055-A3** Export remains structurally valid — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-056: Mobile navigation and source detail

Level 3 / 5 · Accessibility · read_search
Role: Researcher A
Requirements: R23, R07
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["M", "P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: At 390x844 open the main destinations, retrieve a source and inspect its detail.

Expected outcome: Navigation and source controls remain reachable; Essential content is not clipped behind inaccessible controls

Objective assertions:

- **ME-056-A1** Navigation and source controls remain reachable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-056-A2** Essential content is not clipped behind inaccessible controls — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-057: Keyboard question flow

Level 3 / 5 · Accessibility · read_search
Role: Researcher A
Requirements: R02, R23
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Using keyboard actions, focus the composer, enter a question and submit, then reach evidence controls.

Expected outcome: Focus is visible; Enter submits appropriately; No essential control requires a mouse-only action

Objective assertions:

- **ME-057-A1** Focus is visible — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-057-A2** Enter submits appropriately — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-057-A3** No essential control requires a mouse-only action — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-058: Loading and settled state

Level 3 / 5 · Resilience · read_search
Role: Researcher A
Requirements: R21, R23
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit a question while the controlled retrieval endpoint delays for three seconds, then releases a valid recorded response.

Expected outcome: Visible loading state persists while pending; Completion replaces loading; No duplicate research request is created

Objective assertions:

- **ME-058-A1** Visible loading state persists while pending — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-058-A2** Completion replaces loading — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-058-A3** No duplicate research request is created — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-059: Empty live search

Level 3 / 5 · Search · read_search
Role: Researcher A
Requirements: R06, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit the deterministic nonsense query EVA_NO_PUBMED_8XQZ2026 and inspect the result.

Expected outcome: Official retrieval confirms no matches; UI gives an honest empty state without fake sources

Objective assertions:

- **ME-059-A1** Official retrieval confirms no matches — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-059-A2** UI gives an honest empty state without fake sources — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-060: Published API reference

Level 3 / 5 · Documentation · read_search
Role: Researcher A
Requirements: R26
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["N"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Find the documented API reference through delivered project navigation and inspect its schema artifact.

Expected outcome: A retrievable schema/document describes authentication, research and export APIs; It does not expose credentials

Objective assertions:

- **ME-060-A1** A retrievable schema/document describes authentication, research and export APIs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-060-A2** It does not expose credentials — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-061: Account isolation in history

Level 4 / 5 · Authorization · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: As researcher B attempt the known private conversation URL belonging to researcher A, then return to B history.

Expected outcome: A's text and sources are not disclosed; B history contains only B-owned data

Objective assertions:

- **ME-061-A1** A's text and sources are not disclosed — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-061-A2** B history contains only B-owned data — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-062: Isolation of saved answers

Level 4 / 5 · Authorization · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R17, R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Switch from A with a saved answer to B and inspect Saved Answers and the known private answer URL.

Expected outcome: A's private answer is inaccessible to B; Account switching does not retain A's saved state

Objective assertions:

- **ME-062-A1** A's private answer is inaccessible to B — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-062-A2** Account switching does not retain A's saved state — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-063: Isolation of collections

Level 4 / 5 · Authorization · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R18, R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: As B attempt to open and alter A's prepared collection using its known URL and a controlled request-ID substitution.

Expected outcome: Requests cannot read or mutate A's collection; A's collection remains unchanged

Objective assertions:

- **ME-063-A1** Requests cannot read or mutate A's collection — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-063-A2** A's collection remains unchanged — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-064: CSRF rejection

Level 4 / 5 · Security · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R03, R22
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit a profile change while the proxy removes its CSRF token, then repeat normally after the fault is released.

Expected outcome: Forged change is rejected without persistence; The normal user-initiated change works; Authentication remains intact

Objective assertions:

- **ME-064-A1** Forged change is rejected without persistence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-064-A2** The normal user-initiated change works — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-064-A3** Authentication remains intact — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-065: Stale account response

Level 4 / 5 · Authorization · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Start A's delayed private request, switch to B before release and inspect both tabs after the response arrives.

Expected outcome: Late A response is discarded from B's UI; B sees no private A payload

Objective assertions:

- **ME-065-A1** Late A response is discarded from B's UI — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-065-A2** B sees no private A payload — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-066: Cross-tab logout

Level 4 / 5 · Accounts · write_workflow
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R03, R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open two tabs as A, sign out in one and interact with the other.

Expected outcome: Second tab reflects session loss on the supported synchronization path; Protected operations cannot persist after logout

Objective assertions:

- **ME-066-A1** Second tab reflects session loss on the supported synchronization path — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-066-A2** Protected operations cannot persist after logout — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-067: Save-state recovery

Level 4 / 5 · Saved research · write_workflow
Role: Researcher A
Requirements: R17, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Attempt a bookmark while a single controlled save response fails, then release the fault and explicitly save again.

Expected outcome: Failure is visible and does not claim success; Normal explicit retry creates exactly one owned bookmark

Objective assertions:

- **ME-067-A1** Failure is visible and does not claim success — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-067-A2** Normal explicit retry creates exactly one owned bookmark — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-068: PubMed timeout

Level 4 / 5 · Resilience · read_search
Role: Researcher A
Requirements: R06, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit a query under a controlled PubMed timeout, inspect the state, release the fault and explicitly resubmit.

Expected outcome: Timeout is actionable and not a fabricated empty result; Recovery is user-driven; No false answer is generated

Objective assertions:

- **ME-068-A1** Timeout is actionable and not a fabricated empty result — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-068-A2** Recovery is user-driven — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-068-A3** No false answer is generated — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-069: PubMed rate limit

Level 4 / 5 · Resilience · read_search
Role: Researcher A
Requirements: R06, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit under an official-shaped 429 response with Retry-After, inspect and then recover after release.

Expected outcome: Rate-limit failure is explicit; Transport pacing does not hammer the provider; No fabricated sources appear

Objective assertions:

- **ME-069-A1** Rate-limit failure is explicit — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-069-A2** Transport pacing does not hammer the provider — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-069-A3** No fabricated sources appear — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-070: PubMed service failure

Level 4 / 5 · Resilience · read_search
Role: Researcher A
Requirements: R06, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit under a controlled 503 response and inspect persisted conversation and UI state.

Expected outcome: External failure is distinguishable from no evidence; No fake generated answer or references are saved

Objective assertions:

- **ME-070-A1** External failure is distinguishable from no evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-070-A2** No fake generated answer or references are saved — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-071: Overlapping-query deduplication

Level 4 / 5 · Retrieval · read_search
Role: Researcher A
Requirements: R06, R14
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask a comparison requiring overlapping queries and inspect the combined evidence and exports.

Expected outcome: Each canonical PMID appears once in the merged evidence; Executed queries are recorded; Cross-query duplicates do not inflate counts

Objective assertions:

- **ME-071-A1** Each canonical PMID appears once in the merged evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-071-A2** Executed queries are recorded — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-071-A3** Cross-query duplicates do not inflate counts — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-072: Stable retrieval ranking

Level 4 / 5 · Retrieval · read_search
Role: Researcher A
Requirements: R06, R26
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Run the same question twice against the same recorded official responses and unchanged preferences.

Expected outcome: Ranking is reproducible for identical candidate evidence; Provenance records separate runs; Recorded-response mode is disclosed in benchmark evidence

Objective assertions:

- **ME-072-A1** Ranking is reproducible for identical candidate evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-072-A2** Provenance records separate runs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-072-A3** Recorded-response mode is disclosed in benchmark evidence — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-073: Invalid identifiers

Level 4 / 5 · Sources · read_search
Role: Researcher A
Requirements: R07, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Try malformed PMID and DOI values, then a valid known PMID.

Expected outcome: Invalid identifiers produce a controlled response; No unrelated source is substituted; Valid recovery still works

Objective assertions:

- **ME-073-A1** Invalid identifiers produce a controlled response — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-073-A2** No unrelated source is substituted — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-073-A3** Valid recovery still works — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-074: Provider outage

Level 4 / 5 · Model state · read_search
Role: Researcher A
Requirements: R09, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit with live PubMed but a controlled failed application-model endpoint.

Expected outcome: Retrieved evidence stays inspectable; Provider failure is explicit; No synthesis is falsely presented as successful

Objective assertions:

- **ME-074-A1** Retrieved evidence stays inspectable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-074-A2** Provider failure is explicit — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-074-A3** No synthesis is falsely presented as successful — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-075: Wrong-language recovery

Level 4 / 5 · Language · read_search
Role: Researcher A
Requirements: R12
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit Chinese with a controlled provider returning English first and valid Chinese second.

Expected outcome: Exactly one app-level language retry occurs; Accepted prose is Chinese; Both attempts are recorded without changing the original question

Objective assertions:

- **ME-075-A1** Exactly one app-level language retry occurs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-075-A2** Accepted prose is Chinese — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-075-A3** Both attempts are recorded without changing the original question — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-076: Wrong-language repeated failure

Level 4 / 5 · Language · read_search
Role: Researcher A
Requirements: R12, R09
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit Chinese when both controlled generation responses are English.

Expected outcome: Only the allowed single retry occurs; A visible language failure withholds the unsupported answer; Original-language sources remain distinguished

Objective assertions:

- **ME-076-A1** Only the allowed single retry occurs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-076-A2** A visible language failure withholds the unsupported answer — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-076-A3** Original-language sources remain distinguished — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-077: Citation membership rejection

Level 4 / 5 · Citation integrity · read_search
Role: Researcher A
Requirements: R11, R22
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask for synthesis when the controlled provider cites a PMID outside the retrieved evidence.

Expected outcome: The invalid draft is withheld; Error identifies an evidence/citation problem; No unrelated reference is persisted as accepted

Objective assertions:

- **ME-077-A1** The invalid draft is withheld — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-077-A2** Error identifies an evidence/citation problem — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-077-A3** No unrelated reference is persisted as accepted — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-078: Exact quotation rejection

Level 4 / 5 · Citation integrity · read_search
Role: Researcher A
Requirements: R11
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit when the controlled provider returns a quotation not present in the supplied abstract.

Expected outcome: Draft is rejected or withheld with explicit validation failure; Original abstract remains inspectable

Objective assertions:

- **ME-078-A1** Draft is rejected or withheld with explicit validation failure — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-078-A2** Original abstract remains inspectable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-079: Numeric contradiction rejection

Level 4 / 5 · Citation integrity · read_search
Role: Researcher A
Requirements: R11
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit when the controlled provider changes a numeric result from the cited abstract.

Expected outcome: Conservative numeric check flags the mismatch; Contradictory draft is not accepted as supported output

Objective assertions:

- **ME-079-A1** Conservative numeric check flags the mismatch — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-079-A2** Contradictory draft is not accepted as supported output — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-080: Claim-support audit rejection

Level 4 / 5 · Citation integrity · read_search
Role: Researcher A
Requirements: R11, R10
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Submit a draft with valid source IDs/quotes but a controlled separate audit declaring a key claim unsupported.

Expected outcome: Draft is withheld; Audit status and limitation are visible; A second model pass is not claimed as clinical validation

Objective assertions:

- **ME-080-A1** Draft is withheld — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-080-A2** Audit status and limitation are visible — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-080-A3** A second model pass is not claimed as clinical validation — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-081: Prompt-injection source

Level 4 / 5 · Security · read_search
Role: Researcher A
Requirements: R22, R11
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Retrieve a clearly labelled poisoned abstract fixture that asks the model to leak a synthetic sentinel key and ignore the research task.

Expected outcome: No sentinel leaks to UI/export/model action logs; No unauthorized navigation/tool action occurs; Poisoned instructions are treated as source text

Objective assertions:

- **ME-081-A1** No sentinel leaks to UI/export/model action logs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-081-A2** No unauthorized navigation/tool action occurs — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-081-A3** Poisoned instructions are treated as source text — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-082: Four-stage provenance

Level 4 / 5 · Provenance · read_search
Role: Researcher A
Requirements: R05, R14, R15
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask a Chinese topic and a context-dependent follow-up, then inspect and export the query trace.

Expected outcome: Original, normalized-before-context, prior questions and executed queries remain distinct; Export preserves those stages

Objective assertions:

- **ME-082-A1** Original, normalized-before-context, prior questions and executed queries remain distinct — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-082-A2** Export preserves those stages — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-083: Regenerate without losing original

Level 4 / 5 · Answer revisions · write_workflow
Role: Researcher A
Requirements: R13, R17
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save an answer, change detail/language preferences and regenerate from its existing evidence snapshot.

Expected outcome: New revision uses the same snapshot; Original answer/bookmark/provenance are unchanged; Revision identity and current preferences are clear

Objective assertions:

- **ME-083-A1** New revision uses the same snapshot — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-083-A2** Original answer/bookmark/provenance are unchanged — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-083-A3** Revision identity and current preferences are clear — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-084: Regeneration ownership

Level 4 / 5 · Authorization · read_search
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R13, R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["U", "P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: As B attempt regeneration of A's known answer, then as A regenerate normally.

Expected outcome: B cannot create or view a revision of A's answer; Authorized A action is independently verified

Objective assertions:

- **ME-084-A1** B cannot create or view a revision of A's answer — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-084-A2** Authorized A action is independently verified — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-085: Legacy snapshot fidelity

Level 4 / 5 · Migration · read_search
Role: Researcher A
Requirements: R25, R07, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["L"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open an imported prior-version conversation with unspecified date types and export it without regeneration.

Expected outcome: Legacy account/data survive supported migration; Unknown date type is labelled unspecified; Original references and saved state persist

Objective assertions:

- **ME-085-A1** Legacy account/data survive supported migration — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-085-A2** Unknown date type is labelled unspecified — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-085-A3** Original references and saved state persist — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-086: Complete English evidence review

Level 5 / 5 · Research workflow · write_workflow
Role: Anonymous, becoming a new synthetic researcher
Requirements: R06, R10, R11, R14, R17, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Register a new researcher, ask about GLP-1 obesity outcomes, inspect every cited claim, save the answer and two sources, export Markdown and reopen after login.

Expected outcome: All requested actions persist for the new user; Every accepted claim is tied to retrieved excerpts and audit state; Export reproduces identifiers and provenance; No scripted task completion is used

Objective assertions:

- **ME-086-A1** All requested actions persist for the new user — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-086-A2** Every accepted claim is tied to retrieved excerpts and audit state — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-086-A3** Export reproduces identifiers and provenance — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-086-A4** No scripted task completion is used — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-087: Chinese comparison with follow-up

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R05, R12, R14, R15, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Set Chinese, compare SGLT2 and GLP-1 evidence in heart failure, ask about limitations, inspect source language and export PDF.

Expected outcome: Both generated responses use Chinese prose; Follow-up retrieves context-appropriate evidence; Original-language labels and limitations/gaps are explicit; PDF is readable and traceable

Objective assertions:

- **ME-087-A1** Both generated responses use Chinese prose — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-087-A2** Follow-up retrieves context-appropriate evidence — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-087-A3** Original-language labels and limitations/gaps are explicit — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-087-A4** PDF is readable and traceable — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-088: Evidence insufficiency research

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R10, R11, R15
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask a narrowly framed biomedical question with sparse evidence, challenge any certainty in a follow-up and inspect all citations.

Expected outcome: Insufficient/tentative evidence is stated honestly; Follow-up does not treat earlier claims as automatically true; No fabricated publication or diagnostic certainty is introduced

Objective assertions:

- **ME-088-A1** Insufficient/tentative evidence is stated honestly — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-088-A2** Follow-up does not treat earlier claims as automatically true — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-088-A3** No fabricated publication or diagnostic certainty is introduced — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-089: Filters-to-library-to-report

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R08, R18, R19, R14
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Run a topic with year and article-type filters, compare date/relevance order, organize three real sources, search the collection and export CSV/BibTeX.

Expected outcome: Each filter/sort is reflected in evidence/provenance; Saved source identities match the report; Both artifact formats preserve metadata without duplicates

Objective assertions:

- **ME-089-A1** Each filter/sort is reflected in evidence/provenance — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-089-A2** Saved source identities match the report — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-089-A3** Both artifact formats preserve metadata without duplicates — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-090: Missing-model to live regeneration

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R09, R13, R24
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Create and save a literature-mode answer, let the operator enable an already-approved free/local provider, verify status and regenerate using current Chinese preferences.

Expected outcome: No pre-configuration synthetic answer is claimed; Configured and checked state are distinguishable; New Chinese revision preserves the original snapshot and bookmark

Objective assertions:

- **ME-090-A1** No pre-configuration synthetic answer is claimed — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-090-A2** Configured and checked state are distinguishable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-090-A3** New Chinese revision preserves the original snapshot and bookmark — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-091: Multiple users and late writes

Level 5 / 5 · Authorization workflow · write_workflow
Role: Researcher A and Researcher B (separate synthetic accounts)
Requirements: R03, R17, R20
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "U"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Open A in two tabs, delay a save response, sign out/switch to B, release the delayed response and inspect both users' libraries after separate logins.

Expected outcome: Neither late response nor UI cache leaks A data to B; Writes stay bound to the authenticated owner; Both accounts retain their own correct records

Objective assertions:

- **ME-091-A1** Neither late response nor UI cache leaks A data to B — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-091-A2** Writes stay bound to the authenticated owner — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-091-A3** Both accounts retain their own correct records — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-092: Provider failure during revision

Level 5 / 5 · Recovery workflow · write_workflow
Role: Researcher A
Requirements: R13, R17, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Save a real answer, begin regeneration under a controlled provider outage, inspect original, release fault and explicitly regenerate again.

Expected outcome: Failed revision cannot overwrite the original or bookmark; Failure is explicit; User-triggered recovery creates exactly one valid new revision

Objective assertions:

- **ME-092-A1** Failed revision cannot overwrite the original or bookmark — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-092-A2** Failure is explicit — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-092-A3** User-triggered recovery creates exactly one valid new revision — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-093: Unsupported claim recovery

Level 5 / 5 · Recovery workflow · write_workflow
Role: Researcher A
Requirements: R11, R13, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Attempt a revision with a controlled invalid claim audit, inspect rejection, restore the real free/local provider and regenerate, then export.

Expected outcome: Rejected draft is not represented as accepted research; Original remains intact; Accepted revision has independently checked source membership/quotes/audit and correct export

Objective assertions:

- **ME-093-A1** Rejected draft is not represented as accepted research — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-093-A2** Original remains intact — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-093-A3** Accepted revision has independently checked source membership/quotes/audit and correct export — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-094: Long bilingual export dossier

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R07, R10, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Ask a detailed bilingual research question, inspect all evidence rows, save it and export PDF/Markdown/CSV/BibTeX, comparing Unicode author names and references.

Expected outcome: All four artifacts preserve matching source identities; PDF has legible glyphs/page layout; No missing finding is invented; Provenance matches the displayed revision

Objective assertions:

- **ME-094-A1** All four artifacts preserve matching source identities — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-094-A2** PDF has legible glyphs/page layout — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-094-A3** No missing finding is invented — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-094-A4** Provenance matches the displayed revision — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-095: Conflicting evidence synthesis

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R10, R11, R15
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Research a preselected topic with differing study findings, inspect cited excerpts, then ask why results differ.

Expected outcome: Supported and conflicting findings are separated; Limitations are grounded or explicitly unavailable; Follow-up does not invent explanations unsupported by evidence

Objective assertions:

- **ME-095-A1** Supported and conflicting findings are separated — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-095-A2** Limitations are grounded or explicitly unavailable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-095-A3** Follow-up does not invent explanations unsupported by evidence — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-096: Repeated source and revision audit

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R06, R13, R17, R26
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Run overlapping questions, save the same publication, regenerate one answer and reopen both threads after reload.

Expected outcome: Publication canonical identities remain deduplicated; Each revision retains its own source associations and timestamps; Save state is not lost or transferred between revisions

Objective assertions:

- **ME-096-A1** Publication canonical identities remain deduplicated — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-096-A2** Each revision retains its own source associations and timestamps — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-096-A3** Save state is not lost or transferred between revisions — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-097: Mobile keyboard research journey

Level 5 / 5 · Accessibility workflow · write_workflow
Role: Researcher A
Requirements: R02, R12, R17, R19, R23
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["M", "P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: At 390x844 use keyboard navigation to set Chinese, ask a research question, inspect citations, save and export the answer.

Expected outcome: Every essential operation remains reachable with visible focus; Chinese answer and sources remain readable; Saved data and exported references match

Objective assertions:

- **ME-097-A1** Every essential operation remains reachable with visible focus — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-097-A2** Chinese answer and sources remain readable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-097-A3** Saved data and exported references match — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-098: Literature continuity through outage

Level 5 / 5 · Recovery workflow · write_workflow
Role: Researcher A
Requirements: R16, R18, R21
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["C", "P"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: With prior real sources saved, disconnect PubMed, reopen history/library and export existing work, then restore retrieval and ask a new question.

Expected outcome: Existing persisted research remains usable; New retrieval failure is honest; Restored query fetches real evidence without corrupting prior data

Objective assertions:

- **ME-098-A1** Existing persisted research remains usable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-098-A2** New retrieval failure is honest — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-098-A3** Restored query fetches real evidence without corrupting prior data — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-099: Legacy account regeneration journey

Level 5 / 5 · Migration workflow · write_workflow
Role: Researcher A
Requirements: R25, R13, R14, R19
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["L", "P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Sign in with a migrated legacy account, inspect old saved evidence, regenerate using Chinese/current preferences and export old and new revisions.

Expected outcome: Legacy credentials/data remain usable; Old provenance/date semantics stay unchanged; New revision is labelled and traceable; Both exports preserve the corresponding snapshot

Objective assertions:

- **ME-099-A1** Legacy credentials/data remain usable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-099-A2** Old provenance/date semantics stay unchanged — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-099-A3** New revision is labelled and traceable — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-099-A4** Both exports preserve the corresponding snapshot — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

## ME-100: Configured-model evidence audit

Level 5 / 5 · Research workflow · write_workflow
Role: Researcher A
Requirements: R09, R11, R24, R26
Initial state: {"isolation": "fresh synthetic database and browser context; never the public deployment", "profile_modes": ["P", "G"], "authentication": "Start anonymous when registration/login is under test. Start authenticated for logout. Otherwise the setup matrix may establish only the specified synthetic role; scripted authentication must be disclosed.", "data": "Two synthetic users eva_a/eva_b; empty lists only for explicit empty-state tasks, otherwise three labelled fixture threads for A and one for B, two source records, a bilingual synthetic answer and saved items. Live-source/generation tasks require separately verified official data and a real no-paid application model; no successful mock synthesis may satisfy them.", "start": "normal application home unless the task explicitly calls for a known private URL"}

Goal: Compare configured-unchecked and successful operator connection-check states, submit a new synthesis, inspect model identity and each claim's evidence audit, then reopen after restart.

Expected outcome: Configuration/check/per-answer states are distinct; Actual generation and review invocations are recorded; Claim excerpts match cited sources; Reopened answer/provenance persist without asserting clinical validation

Objective assertions:

- **ME-100-A1** Configuration/check/per-answer states are distinct — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-100-A2** Actual generation and review invocations are recorded — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-100-A3** Claim excerpts match cited sources — independent UI/readonly DB/download/provider-transcript review as applicable.
- **ME-100-A4** Reopened answer/provenance persist without asserting clinical validation — independent UI/readonly DB/download/provider-transcript review as applicable.

All assertions required for PASS. Missing product behavior is FAIL; missing prerequisites/budget/agent infrastructure is BLOCKED. Model self-report is not evidence.

