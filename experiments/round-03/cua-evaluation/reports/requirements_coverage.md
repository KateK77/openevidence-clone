# MedEvidence 3.0 — CUA requirements coverage

Source uploaded SHA-256: `91df4cd29312aad57d12e052c5f07cc1727d9f7d83b5a33ce8e5213a38cbc8e9`. The Description is the authoritative product contract, not a status report.

The suite contains **365 distinct core scenarios** and **473 execution IDs**; variant executions are not additional independent features. **No evaluation has been performed.**

| Acceptance ID | Unique core scenarios | CUA execution variants | Boundary |
|---|---:|---:|---|
| V3-A01 | 32 | 44 | UI candidate |
| V3-A02 | 48 | 60 | UI-only/partial |
| V3-A03 | 25 | 38 | UI candidate |
| V3-A04 | 39 | 53 | UI-only/partial |
| V3-A05 | 46 | 61 | UI candidate |
| V3-A06 | 23 | 29 | UI candidate |
| V3-A07 | 16 | 17 | UI-only/partial |
| V3-A08 | 14 | 21 | UI candidate |
| V3-A09 | 19 | 27 | UI candidate |
| V3-A10 | 7 | 8 | UI candidate |
| V3-A11 | 46 | 56 | UI-only/partial |
| V3-A12 | 35 | 43 | UI candidate |
| V3-A13 | 28 | 33 | UI candidate |
| V3-A14 | 17 | 18 | UI candidate |
| V3-A15 | 23 | 30 | UI candidate |
| V3-A16 | 19 | 23 | UI candidate |
| V3-A17 | 29 | 38 | UI candidate |
| V3-A18 | 49 | 66 | UI candidate |
| V3-A19 | 26 | 29 | UI candidate |
| V3-A20 | 35 | 51 | UI candidate |
| V3-A21 | 41 | 45 | UI-only/partial |
| V3-A22 | 0 | 0 | non-CUA only |
| V3-A23 | 14 | 16 | UI-only/partial |
| V3-A24 | 14 | 16 | UI-only/partial |

## Modules

| Module | Core scenarios | Execution IDs |
|---|---:|---:|
| Answer details and source presentation | 17 | 24 |
| Authentication and profiles | 25 | 36 |
| Bookmarks, collections and saved searches | 29 | 38 |
| Citation and claim-support checks | 22 | 24 |
| Conversations and research history | 20 | 28 |
| Hosted operation and resilience | 14 | 16 |
| Language and response preferences | 21 | 29 |
| Model configuration and operating modes | 23 | 29 |
| Ownership, input safety and throttling | 19 | 20 |
| Product identity and navigation | 16 | 23 |
| Provenance and follow-up context | 19 | 23 |
| PubMed lookup and publication details | 37 | 50 |
| Question composer and terminology | 25 | 38 |
| Regeneration and revision integrity | 17 | 18 |
| Research copy and exports | 26 | 29 |
| Research pipeline and evidence persistence | 16 | 20 |
| Responsive and keyboard accessibility | 19 | 28 |

## Duplicate-prevention protocol

Each core has a unique user goal, scored action path and expected observable result. Additional IDs for the same core are limited to materially distinct viewport and/or keyboard interaction; the variant changes an independently observable acceptance dimension.
Identical titles are never scored as two distinct core scenarios. Running the same workflow in different variants must not be described as separate independent features.
Do not introduce additional variants or loosen expected results after freezing.

## Deliberately excluded from CUA scoring

V3-A22 (database migration preservation) requires migration and database integrity inspection, not browser-only action. Backend cryptography, CSRF, infrastructure, provider billing and clinical/source-truth guarantees have additional engineering verification boundaries described separately.
