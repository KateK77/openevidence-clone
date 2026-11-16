# Prerequisite readiness — 26 explicitly blocked cases

Readiness assessment only, dated November 16, 2026. All 100 benchmark results remain **NOT_RUN**. No prerequisite finding is an application FAIL. This addendum leaves the frozen FIXTURES.md and all test definitions unchanged.

**0 of these 26 additional prerequisites have been provisioned; all 26 are explicitly marked below.** Offline review confirmed their profiles are unsupported by the current isolated adapter. A successful public-site Gemini check from development cannot establish readiness of these fresh isolated fixtures.

The other 74 cases comprise 50 offline-profile and 24 live-PubMed-profile tasks. The shared offline browser/database preflight passes; that does not validate every case-specific fixture or establish the 24 live retrieval prerequisites. Native API compatibility and model entitlement remain unverified. The global actual-bill-cap block applies to every case, including these 74.

## Per-case requirements

| ID | Difficulty | Profile | Case | Readiness |
|---|---|---|---|---|
| T068 | Medium | configured | Configured but unchecked | BLOCKED_PREREQUISITE; result NOT_RUN |
| T069 | Medium | live | Chinese connection probe | BLOCKED_PREREQUISITE; result NOT_RUN |
| T070 | Medium | live | English evidence synthesis | BLOCKED_PREREQUISITE; result NOT_RUN |
| T071 | Hard | live | Chinese research synthesis | BLOCKED_PREREQUISITE; result NOT_RUN |
| T072 | Hard | live | Regenerate while preserving original | BLOCKED_PREREQUISITE; result NOT_RUN |
| T076 | Hard | fault_membership | Reject nonexistent citation | BLOCKED_PREREQUISITE; result NOT_RUN |
| T077 | Hard | fault_quote | Reject altered quotation | BLOCKED_PREREQUISITE; result NOT_RUN |
| T078 | Hard | fault_numeric | Reject unsupported numeric claim | BLOCKED_PREREQUISITE; result NOT_RUN |
| T079 | Hard | fault_review | Reject contradicted claim | BLOCKED_PREREQUISITE; result NOT_RUN |
| T080 | Hard | fault_language | Wrong-language retry boundary | BLOCKED_PREREQUISITE; result NOT_RUN |
| T081 | Hard | fault_auth | Provider credential failure | BLOCKED_PREREQUISITE; result NOT_RUN |
| T082 | Hard | fault_quota | Provider quota exhaustion | BLOCKED_PREREQUISITE; result NOT_RUN |
| T083 | Hard | fault_timeout | Model timeout | BLOCKED_PREREQUISITE; result NOT_RUN |
| T084 | Hard | fault_pubmed | Literature service failure and recovery | BLOCKED_PREREQUISITE; result NOT_RUN |
| T085 | Hard | fault_injection | Untrusted article injection | BLOCKED_PREREQUISITE; result NOT_RUN |
| T088 | Hard | live | Audit generated claims | BLOCKED_PREREQUISITE; result NOT_RUN |
| T091 | Expert | live | Complete evidence research lifecycle | BLOCKED_PREREQUISITE; result NOT_RUN |
| T092 | Expert | live | Two-researcher confidentiality lifecycle | BLOCKED_PREREQUISITE; result NOT_RUN |
| T093 | Expert | live_transition | Missing-model to live revision lifecycle | BLOCKED_PREREQUISITE; result NOT_RUN |
| T094 | Expert | live | Conflicting evidence comparison | BLOCKED_PREREQUISITE; result NOT_RUN |
| T095 | Expert | fault_sequence | Verification failure and explicit recovery | BLOCKED_PREREQUISITE; result NOT_RUN |
| T096 | Expert | hosted | Public availability and persistence | BLOCKED_PREREQUISITE; result NOT_RUN |
| T097 | Expert | live | Mobile complete research workflow | BLOCKED_PREREQUISITE; result NOT_RUN |
| T098 | Expert | fault_rate | Rate-limit isolation and recovery | BLOCKED_PREREQUISITE; result NOT_RUN |
| T099 | Expert | live | Cross-format provenance reconciliation | BLOCKED_PREREQUISITE; result NOT_RUN |
| T100 | Expert | live | Long research thread and reproducibility | BLOCKED_PREREQUISITE; result NOT_RUN |

## T068 — Configured but unchecked

Required: Supply protected real provider configuration to an isolated adapter; clear readiness cache without probing; verify configured-but-unchecked state is reproducible.

Cost boundary: Read-only configuration setup requires no inference; any subsequent provider probe is excluded from this approval.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T069 — Chinese connection probe

Required: Provision a real provider with verified zero-cost entitlement or a bounded shared-budget allowance; retain the actual Chinese readiness-probe response and request log.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T070 — English evidence synthesis

Required: Enable genuine English synthesis and live PubMed in isolated state; retain original abstracts, generation and verification responses for independent claim review.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T071 — Chinese research synthesis

Required: Enable genuine Chinese synthesis and live PubMed; establish Chinese preference before submission and preserve original-language source text for audit.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T072 — Regenerate while preserving original

Required: Prepare a bookmarked literature-only original, then activate a genuine provider through an operator checkpoint; snapshot original and revision evidence/bookmark state.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T076 — Reject nonexistent citation

Required: Build a local deterministic provider proxy returning an otherwise valid draft with a PMID outside the actual evidence set; preserve the injected draft and evidence snapshot.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T077 — Reject altered quotation

Required: Build a local proxy returning a quotation intentionally absent from the referenced authentic abstract; retain exact bytes of draft and source.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T078 — Reject unsupported numeric claim

Required: Build a local proxy returning an unsupported numeric claim tied to known source text; retain both for independent validation.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T079 — Reject contradicted claim

Required: Build a local generation/reviewer proxy with a valid quote and contradicted interpretation plus explicit negative support review; verify draft withholding separately.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T080 — Wrong-language retry boundary

Required: Build a local provider proxy returning English twice under Chinese preference, and a request counter. The required one application corrective retry must hit this free proxy, never a paid provider.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T081 — Provider credential failure

Required: Build a local provider proxy returning controlled 401/403 without forwarding credentials; record failure status and absence of secrets.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T082 — Provider quota exhaustion

Required: Build a local provider proxy returning 429 with bounded response; record all attempts and ensure no forwarding, provider fallback or recharge.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T083 — Model timeout

Required: Build a local stalled provider endpoint with known timeout and request counter; capture timeout timing and persisted evidence.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T084 — Literature service failure and recovery

Required: Provide a switchable PubMed failure proxy and recovery checkpoint to real PubMed; record failure, restoration and single manual resubmission separately.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T085 — Untrusted article injection

Required: Provide a clearly labeled malicious article fixture through an isolated retrieval proxy; genuine model behavior must remain real and separately cost-controlled, with a synthetic canary instead of any secret.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T088 — Audit generated claims

Required: Provide genuine synthesis and preserved actual evidence excerpts, model metadata and verification artifacts; arrange independent review of every claim.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T091 — Complete evidence research lifecycle

Required: Provide genuine Chinese generation across initial/follow-up turns, live PubMed, synthetic registration, downloads and an independent all-criteria lifecycle audit.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T092 — Two-researcher confidentiality lifecycle

Required: Provide two isolated researcher accounts and real generated work, with independently scoped ownership and export checks; no production accounts or data.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T093 — Missing-model to live revision lifecycle

Required: Implement a deterministic operator checkpoint from model-disabled to genuine provider-enabled without altering application code; preserve original and revision snapshots.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T094 — Conflicting evidence comparison

Required: Provide genuine multi-intervention synthesis, live sources and reviewer access to populations/designs; retain comparison/follow-up excerpts and uncertainty evidence.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T095 — Verification failure and explicit recovery

Required: Implement an operator checkpoint from local unsupported-draft proxy to genuine provider; retain rejected and recovered revisions and all provider-call accounting.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T096 — Public availability and persistence

Required: Provide a separately authorized synthetic hosted deployment, persistent database and restart checkpoint. Free plan must be confirmed; no restart/reset of the public-user deployment in offline preparation.

Cost boundary: Hosting/database must stay on confirmed free plans; no new resources or restart actions authorized by this budget-only change.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T097 — Mobile complete research workflow

Required: Provide genuine Chinese synthesis, live PubMed and mobile download handling at frozen 390x844; independently review every narrow-screen workflow step.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T098 — Rate-limit isolation and recovery

Required: Provide isolated rate-limit/cache state, known threshold/reset interval and a counted free local dependency endpoint. Exercise the actual application limiter without generating paid model calls.

Cost boundary: Use local free dependency injection; never call a paid provider for retries or fault preparation.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T099 — Cross-format provenance reconciliation

Required: Provide genuine supported synthesis with multiple references and offline PDF/Markdown/BibTeX/CSV inspectors; retain downloaded originals and per-format metadata comparison.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## T100 — Long research thread and reproducibility

Required: Provide five genuine context-dependent turns with source snapshots per turn, fresh authentication and export evidence; budget for the complete chain without shortening it.

Cost boundary: Real application-provider usage must be independently confirmed free or reserved in the shared $10 actual-cost bound; not verified.

Free check: Frozen task/profile/criteria reviewed against existing adapter allowlist; required adapter is absent. No live or injected execution performed.

Unblock evidence: Reviewed adapter, reproducible synthetic fixture and profile-specific prerequisite proof; unchanged frozen criteria; resolved global billing block and fresh paid approval.

## Retry and evidence rules

T080 deliberately tests an application-level corrective retry. That frozen behavior remains required, but both calls must target a no-cost local fixture. It does not authorize paid CUA retries. T084/T095 require explicit recovery checkpoints, not automatic paid retries. Fault-injection outputs must be labeled synthetic and cannot establish real synthesis quality. Real-generation cases cannot be replaced by canned responses.

After prerequisite resolution, retain native response/call IDs, original difficulty, every frozen criterion, action traces, screenshots, raw usage including cached input, reservation/settlement records, and independent PASS/FAIL review. Missing prerequisites leave cases NOT_RUN with a prerequisite reason; incomplete execution is distinguished from an application FAIL.
