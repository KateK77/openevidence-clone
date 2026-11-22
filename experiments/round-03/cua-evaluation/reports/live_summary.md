# Real CUA results — no invented outcomes

Results below are computed exclusively from recorded rows in `results/all_results.csv`. An unrun suite has no measured pass rate.

## Overall

| Metric | Value |
|---|---:|
| total | 473 |
| PASS | 126 |
| FAIL | 12 |
| BLOCKED | 172 |
| NOT_RUN | 163 |
| overall_pass_rate_pct | 26.64 |
| executed_pass_rate_pct | 91.3 |
| definitive_coverage_pct | 29.18 |

## Difficulty

| Group | Total | PASS | FAIL | BLOCKED | NOT_RUN | Overall % | Executed % |
|---|---:|---:|---:|---:|---:|---:|---:|
| Easy | 125 | 52 | 6 | 33 | 34 | 41.6 | 89.66 |
| Expert | 13 | 1 | 0 | 9 | 3 | 7.69 | 100.0 |
| Hard | 91 | 11 | 0 | 47 | 33 | 12.09 | 100.0 |
| Medium | 244 | 62 | 6 | 83 | 93 | 25.41 | 91.18 |

## Module

| Group | Total | PASS | FAIL | BLOCKED | NOT_RUN | Overall % | Executed % |
|---|---:|---:|---:|---:|---:|---:|---:|
| Answer details and source presentation | 24 | 11 | 2 | 11 | 0 | 45.83 | 84.62 |
| Authentication and profiles | 36 | 20 | 0 | 16 | 0 | 55.56 | 100.0 |
| Bookmarks, collections and saved searches | 38 | 0 | 0 | 0 | 38 | N/A | N/A |
| Citation and claim-support checks | 24 | 3 | 0 | 21 | 0 | 12.5 | 100.0 |
| Conversations and research history | 28 | 0 | 0 | 0 | 28 | N/A | N/A |
| Hosted operation and resilience | 16 | 0 | 0 | 0 | 16 | N/A | N/A |
| Language and response preferences | 29 | 14 | 0 | 15 | 0 | 48.28 | 100.0 |
| Model configuration and operating modes | 29 | 2 | 0 | 27 | 0 | 6.9 | 100.0 |
| Ownership, input safety and throttling | 20 | 0 | 0 | 0 | 20 | N/A | N/A |
| Product identity and navigation | 23 | 10 | 0 | 13 | 0 | 43.48 | 100.0 |
| Provenance and follow-up context | 23 | 9 | 0 | 10 | 4 | 39.13 | 100.0 |
| PubMed lookup and publication details | 50 | 35 | 6 | 9 | 0 | 70.0 | 85.37 |
| Question composer and terminology | 38 | 16 | 2 | 20 | 0 | 42.11 | 88.89 |
| Regeneration and revision integrity | 18 | 2 | 1 | 15 | 0 | 11.11 | 66.67 |
| Research copy and exports | 29 | 0 | 0 | 0 | 29 | N/A | N/A |
| Research pipeline and evidence persistence | 20 | 4 | 1 | 15 | 0 | 20.0 | 80.0 |
| Responsive and keyboard accessibility | 28 | 0 | 0 | 0 | 28 | N/A | N/A |

## Environment

| Group | Total | PASS | FAIL | BLOCKED | NOT_RUN | Overall % | Executed % |
|---|---:|---:|---:|---:|---:|---:|---:|
| desktop_keyboard_only | 12 | 3 | 0 | 2 | 7 | 25.0 | 100.0 |
| desktop_pointer | 351 | 83 | 9 | 141 | 118 | 23.65 | 90.22 |
| mobile_keyboard_only | 2 | 0 | 0 | 0 | 2 | N/A | N/A |
| mobile_pointer | 108 | 40 | 3 | 29 | 36 | 37.04 | 93.02 |

## Fixture Gate

| Group | Total | PASS | FAIL | BLOCKED | NOT_RUN | Overall % | Executed % |
|---|---:|---:|---:|---:|---:|---:|---:|
| accepted_answer_fixture | 11 | 0 | 0 | 10 | 1 | N/A | N/A |
| accepted_chinese_fixture | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| altered_quote_fixture | 2 | 0 | 0 | 2 | 0 | N/A | N/A |
| baseline | 116 | 57 | 0 | 37 | 22 | 49.14 | 100.0 |
| claim_reject_fixture | 4 | 0 | 0 | 3 | 1 | N/A | N/A |
| configured_unchecked | 3 | 0 | 0 | 3 | 0 | N/A | N/A |
| controlled_provider_failure | 14 | 0 | 0 | 11 | 3 | N/A | N/A |
| csv_fixture | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| csv_formula_fixture | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| date_fixture | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 |
| evidence_fixture | 43 | 16 | 3 | 3 | 21 | 37.21 | 84.21 |
| evidence_gap_fixture | 2 | 2 | 0 | 0 | 0 | 100.0 | 100.0 |
| global_quota_fixture | 2 | 0 | 0 | 1 | 1 | N/A | N/A |
| glossary_fixture | 3 | 1 | 2 | 0 | 0 | 33.33 | 33.33 |
| history_fixture | 35 | 0 | 0 | 0 | 35 | N/A | N/A |
| hosted_docs | 2 | 0 | 0 | 0 | 2 | N/A | N/A |
| hosted_optional | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 |
| hosted_public | 10 | 0 | 0 | 0 | 10 | N/A | N/A |
| hosted_restart | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| hosted_second_browser | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| hosted_unconfigured | 2 | 0 | 0 | 0 | 2 | N/A | N/A |
| ime_environment | 2 | 0 | 0 | 2 | 0 | N/A | N/A |
| latency_fixture | 9 | 0 | 0 | 7 | 2 | N/A | N/A |
| live_pubmed | 76 | 39 | 6 | 19 | 12 | 51.32 | 86.67 |
| long_abstract_fixture | 5 | 2 | 0 | 2 | 1 | 40.0 | 100.0 |
| long_answer_fixture | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| malformed_provider_fixture | 1 | 0 | 0 | 1 | 0 | N/A | N/A |
| missing_abstract_fixture | 3 | 3 | 0 | 0 | 0 | 100.0 | 100.0 |
| missing_metadata_fixture | 3 | 2 | 1 | 0 | 0 | 66.67 | 66.67 |
| multi_query_fixture | 3 | 0 | 0 | 2 | 1 | N/A | N/A |
| no_external_effects | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| no_limitations_fixture | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 |
| no_source_fixture | 1 | 1 | 0 | 0 | 0 | 100.0 | 100.0 |
| numeric_answer_fixture | 1 | 0 | 0 | 1 | 0 | N/A | N/A |
| overlap_fixture | 4 | 0 | 0 | 4 | 0 | N/A | N/A |
| persistence_fault | 2 | 0 | 0 | 0 | 2 | N/A | N/A |
| punctuation_fixture | 1 | 0 | 0 | 0 | 1 | N/A | N/A |
| quota_fixture | 3 | 0 | 0 | 2 | 1 | N/A | N/A |
| saved_fixture | 28 | 0 | 0 | 0 | 28 | N/A | N/A |
| snapshot_update_fixture | 2 | 0 | 0 | 1 | 1 | N/A | N/A |
| unconfigured_mode | 25 | 0 | 0 | 23 | 2 | N/A | N/A |
| unsupported_citation_fixture | 2 | 0 | 0 | 2 | 0 | N/A | N/A |
| unsupported_gap_fixture | 1 | 0 | 0 | 1 | 0 | N/A | N/A |
| unsupported_number_fixture | 2 | 0 | 0 | 2 | 0 | N/A | N/A |
| untrusted_source_fixture | 5 | 0 | 0 | 3 | 2 | N/A | N/A |
| upstream_fault | 7 | 0 | 0 | 7 | 0 | N/A | N/A |
| working_provider | 23 | 0 | 0 | 18 | 5 | N/A | N/A |
| wrong_language_fixture | 4 | 0 | 0 | 4 | 0 | N/A | N/A |
| zero_result_fixture | 1 | 0 | 0 | 1 | 0 | N/A | N/A |

## Core scenarios

- Unique core scenarios: 365
- At least one definitive variant: 93
- All variants PASS: 84
