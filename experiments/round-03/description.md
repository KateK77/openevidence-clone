# Round 3 consolidated implementation prompt

## Baseline and authorization

Build MedEvidence AI 3.0 from the original platform requirements in
`../round-01/description.md`, the Round 2 improvements in
`../round-02/description.md`, and the manual acceptance findings below.
This is the consolidated next-round prompt. Earlier instructions to stop after
Round 1 or to record issues without fixes are superseded by the user's explicit
request to implement this new version. Preserve the original prompts and release
tags for comparison. Baseline: `12eb0c0`, tag `v2.0.0-r2`.

All reports, repository documentation and GitHub descriptions must be English.
Chinese application copy and functional inputs are allowed. Preserve existing
accounts, research data, source provenance and successful workflows. Do not
replace live retrieval or generation with fixtures or canned medical answers.

## Manual acceptance evidence

Confirmed passing cases: profile save feedback and reload persistence; immediate
logout; answer bookmark feedback and persistence; follow-up placement and
GLP-1/obesity query context; conversation persistence; rename/history search.
Publication Saved feedback and metadata display have partial evidence only.
Untested or partly observed cases must not be declared passed.

The user selected Chinese but received no Chinese answer. The server was in
literature-only mode with no model configured. This is an unmet acceptance
requirement in the tested environment, not evidence of a model ignoring a prompt.
The language preference notice was insufficiently clear to this user.
A sign-in prompt appeared in another view; session loss was not reproduced or
confirmed and must not be described as a fixed authentication defect.

## Required changes

1. Provide a usable server-side model configuration workflow and an explicit
   connection/Chinese-output check. Support compatible hosted APIs and local
   Ollama. Keep keys out of the browser, logs, source control and reports.
   Do not purchase services or enable billing. Free tiers have provider limits;
   local models have hardware requirements. Never promise unlimited free cloud use.
2. Make the difference between missing configuration, configured-but-unchecked,
   successful connection check, provider failure and per-answer generation clear.
   Show the limitation at the question composer and beside language preferences.
3. Enforce Chinese prose for Chinese answers. Retry a wrong-language response
   once, then expose a clear failure instead of silently accepting English.
   Label source titles, quotations and abstracts as original-language material.
   Distinguish localized application messages from generated research answers.
4. Let the owner generate a new answer from an existing evidence snapshot with
   current preferences after configuring a model. Preserve the prior answer,
   saved state, provenance and evidence snapshot; label the new revision.
5. Validate source membership and exact abstract quotations, add conservative
   numerical consistency checks, and run a separate automated claim-support
   review against cited sources. Reject unsupported output. Do not describe
   another model pass as independent clinical validation or a guarantee.
6. Separate findings, limitations and evidence gaps. Show claim-level source
   excerpts and audit status. Keep unsupported limitations explicitly unavailable.
7. Clarify provenance labels: original question, normalized question before
   context, previous questions used, and actual executed PubMed queries.
   Preserve these distinctions in exports.
8. Preserve and regression-test authentication, ownership, persistence, saves,
   short/Chinese questions, history, exports and responsive interaction.

## Acceptance and delivery

Create a new branch `v3-round-03` and release tag `v3.0.0-r3` only after checks.
Produce consolidated feedback, a traceable change report, test evidence and
manual instructions. Keep automated tests distinct from user acceptance.
If no real model credentials or local model are available, finish the authorized
implementation and explicitly report live Chinese generation as blocked. Never
claim that synthetic model tests prove a live model works. Preserve v1 and v2.

## Provider references

The user selected Gemini Free Tier for this version. Provide a hidden local key
prompt and do not enable billing. The user also requested availability when their
PC is off: prepare persistent hosting configuration, but distinguish a tested
deployment package from an actually provisioned public website. No hosting
subscription or public deployment has been completed as part of local verification.

- Gemini compatible endpoint: https://ai.google.dev/gemini-api/docs/openai
- Gemini free-tier conditions: https://ai.google.dev/gemini-api/docs/billing
- Ollama local compatibility: https://docs.ollama.com/api/openai-compatibility
- Ollama pricing: https://ollama.com/pricing

Consulted November 15, 2026. Provider models, quotas and prices can change.
