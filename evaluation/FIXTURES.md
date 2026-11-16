# Evaluation prerequisites and isolation

All tasks start with a fresh database and a fresh browser context. Account A and
account B are synthetic; passwords are random and remain under ignored `.private/`.
The model receives these test credentials only after paid execution is approved.
The original application, existing local database, hosted users and Gemini key are
not modified. Test data must never contain patient information.

Baseline data: A owns three dated, explicitly SYNTHETIC research conversations;
B owns one different private conversation. A has one saved and two unsaved answers;
B has no saved answers/publications. A owns a saved publication in the Obesity
research collection. The historical publication metadata subset for PMID 33567185
comes from the user's prior supplied record; it has no abstract and is explicitly
marked a fixture. It is not a live search or clinical generation result. Live
lookup tests compare to the actual official record, not that incomplete subset.

Tests that save a publication for the first time must start without its saved
association. Tests that change a collection start with Initial research. Tests
of empty states use B. A scratch textarea is evaluator infrastructure, visibly
labeled, for independent clipboard verification; it is not application functionality.

## Profiles

| Profile | Required environment | Current readiness |
|---|---|---|
| offline | AI disabled; external backend/browser networking blocked; real local Django/React/SQLite | Offline preflight available |
| pubmed | AI disabled; live official PubMed access; no replayed literature | Adapter available; network is intentionally not exercised during offline preflight |
| configured / live | A real permitted model and protected server credential; fresh readiness state; genuine generation | Not provisioned in isolated evaluator; BLOCKED until prepared and any cost is separately accounted for |
| fault_* | A controlled external dependency proxy serving specified malicious/malformed/error payload, with authentic source snapshots where required | Not provisioned; never replace fault handling checks with successful canned answers |
| live_transition / fault_sequence | Operator-controlled configuration/dependency transition at the named test checkpoint; unchanged application | Not provisioned |
| hosted | Separate authorized synthetic test deployment and restart checkpoint | Not provisioned; public users must not be reset |

Fault fixtures test handling of deliberately synthetic dependency responses; they
must be labeled as fault injection in results. They cannot prove real Gemini
generation quality. Live profiles cannot be silently converted into offline ones.

The native runner currently executes baseline and PubMed profiles only. Other
profiles fail closed before any paid request and are classified BLOCKED when a run
is approved. Do not start a supposedly complete 100-test evaluation until their
prerequisites are prepared. Keeping them in the frozen suite prevents missing
functionality from being omitted to inflate completion or reduce estimated cost.

Backend-only criteria such as CSRF and password hashing require independent
read-only inspection or explicitly scoped verifier requests alongside the CUA UI
trace. Those verifier actions are never presented as native computer actions.
