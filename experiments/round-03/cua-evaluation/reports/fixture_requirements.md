# Prerequisites and fixture isolation

All scored actions use genuine Chrome CUA. Fixture setup, when necessary, is **before** scored UI interaction, isolated to test databases/accounts and described in `actions.md`. It must not repair application behavior or silently replace a required live provider with a mock.

| Fixture gate | Core scenarios | Meaning / preparation |
|---|---:|---|
| `baseline` | 76 | Existing app and clean synthetic account/data using documented UI; public service must not be modified for scoring. |
| `live_pubmed` | 55 | Real official PubMed service reachable; use known real publication metadata and abstracts, not mocked responses. |
| `evidence_fixture` | 33 | An isolated already saved answer and associated source snapshots; may be created using existing documented workflow/fixture loader before CUA. |
| `history_fixture` | 25 | At least two synthetic owned conversations with known titles/turns and a second owner where required. |
| `saved_fixture` | 22 | Synthetic bookmarks, collections and saved searches prepared in isolated evaluation account/database. |
| `working_provider` | 22 | Authorized working model provider with bounded approved usage and real generation/review; no spending without separate permission. |
| `unconfigured_mode` | 18 | Independent evaluation instance with deliberately absent AI provider configuration; real PubMed may still require access. |
| `controlled_provider_failure` | 13 | Authorized documented test-only provider failure (timeout/invalid endpoint/failed generation), not production application code modification. |
| `accepted_answer_fixture` | 10 | A real previously accepted model-generated answer with saved evidence/review state; no canned success substituted for live generation test. |
| `hosted_public` | 9 | Use the verified public HTTPS demo with only disposable synthetic accounts and no service mutation outside normal UI. |
| `latency_fixture` | 9 | Documented test-safe controllable delayed retrieval/generation/save flow in disposable environment; no frontend rewriting. |
| `untrusted_source_fixture` | 5 | Synthetic malicious-looking publication data in isolated fixture; never real patient data and no live exploit payload. |
| `upstream_fault` | 5 | Isolated, documented test-safe upstream PubMed failure or throttle fixture; never count it as actual live PubMed success. |
| `claim_reject_fixture` | 4 | Documented controlled provider/reviewer rejection with an intact real/synthetic source snapshot. |
| `overlap_fixture` | 4 | Two controlled retrieved query-result sets sharing a real/synthetic PMID, with traceable provenance. |
| `wrong_language_fixture` | 4 | Controlled model fixture delivering specified wrong-language response twice; never count as actual live-model generation. |
| `long_abstract_fixture` | 3 | Long real/synthetic abstract available in isolated test account; original-source text remains auditable. |
| `missing_metadata_fixture` | 3 | Known PubMed publication or controlled fixture with one truly unavailable metadata field. |
| `multi_query_fixture` | 3 | Stored result with more than one executed query and separate per-query PMID evidence lists. |
| `quota_fixture` | 3 | Explicit approved test-safe simulated 429 / provider allowance exhaustion without incurring charges. |
| `altered_quote_fixture` | 2 | Controlled AI draft containing an altered/misattributed excerpt with a real saved source. |
| `configured_unchecked` | 2 | Isolated instance with server-side provider settings but no successful connection probe yet. |
| `global_quota_fixture` | 2 | Test-safe globally shared provider allowance fixture across two synthetic accounts. |
| `glossary_fixture` | 2 | One known supported and one known unsupported term identified from documented glossary, not guessed from UI behavior. |
| `hosted_docs` | 2 | Current linked repository/deployment documentation visible in Chrome; documentation is external evidence, not proof of hosting internals. |
| `missing_abstract_fixture` | 2 | Known PubMed record or controlled publication fixture genuinely lacking an abstract. |
| `persistence_fault` | 2 | Test-safe isolated save failure/recovery fixture; do not modify product behavior. |
| `snapshot_update_fixture` | 2 | Two versions of publication metadata in an isolated documented fixture to verify immutability of answer-specific snapshots. |
| `unsupported_citation_fixture` | 2 | Controlled AI draft with a citation PMID/DOI not in the persisted evidence snapshot. |
| `unsupported_number_fixture` | 2 | Controlled AI draft claiming an unsupported number despite a valid saved citation. |
| `accepted_chinese_fixture` | 1 | Genuinely accepted Chinese AI answer or clearly designated seeded layout-only fixture; seeded case cannot prove live Chinese synthesis. |
| `csv_fixture` | 1 | Publication metadata containing commas, quotes and line breaks for CSV escape verification. |
| `csv_formula_fixture` | 1 | Controlled synthetic publication title with leading formula-like prefix. |
| `date_fixture` | 1 | PubMed record with separately documented electronic/issue dates. |
| `evidence_gap_fixture` | 1 | Research outcome with explicitly supported evidence-gap statement for inspection. |
| `hosted_optional` | 1 | An explicitly labeled shared synthetic demo account is configured and documented, if such an option is published. |
| `hosted_restart` | 1 | Operator-approved public/service restart while disposable synthetic data exists; no restart on a live service without permission. |
| `hosted_second_browser` | 1 | Two independent authenticated browser profiles/contexts, not merely a private tab on the same session. |
| `hosted_unconfigured` | 1 | Public or isolated verified hosted instance in unconfigured model mode; do not change production configuration without permission. |
| `ime_environment` | 1 | Actual Chrome with Chinese IME available for genuine composition-input testing. |
| `long_answer_fixture` | 1 | Stored long answer/source content sufficient for multi-page PDF verification. |
| `malformed_provider_fixture` | 1 | Controlled malformed provider response, without changing the app source. |
| `no_external_effects` | 1 | Only harmless inert test text; no active script, network exploit or patient data. |
| `no_limitations_fixture` | 1 | Source-backed answer where no limitations are extracted/supported, not a fabricated medical conclusion. |
| `no_source_fixture` | 1 | Persisted failed/empty-evidence answer outcome prepared by documented isolated fixture. |
| `numeric_answer_fixture` | 1 | Accepted outcome with numerical claim and exact supporting original abstract excerpt. |
| `punctuation_fixture` | 1 | Publication metadata with citation punctuation needing BibTeX/Markdown escaping. |
| `unsupported_gap_fixture` | 1 | Controlled draft falsely claiming absence of evidence while snapshot contains relevant studies. |
| `zero_result_fixture` | 1 | Known zero-result PubMed query in isolated environment with explicit source response. |

Where a test refers to a controlled upstream/provider fault, run only if a pre-existing documented test-safe isolated fixture can reproduce that state without changing product functionality. A mock-based fault case cannot serve as evidence for real PubMed or live AI acceptance. For actual paid external CUA or model calls, obtain a separate explicit authorization, approved budget and credential procedure.

Never use live patient data, real medical identities, actual payments, secret API keys in the benchmark, or public test-account manipulation that affects other visitors.
