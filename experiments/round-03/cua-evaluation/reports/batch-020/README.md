# Batch020: ME3-CUA-0371–0390

4 PASS / 0 FAIL / 16 BLOCKED. Cumulative through390:181 PASS /14 FAIL /195 BLOCKED;83 NOT_RUN.

[Cumulative results](../../results/all_results.csv) · [Action trace](action_trace.jsonl) · [Screenshot provenance](screenshot_manifest.json) · [Fixture preparation](fixture_preparation.md)

371 reload and rerun restored exact saved query/year/type/sort and returned16 real PubMed records.372 duplicate guard left one row.373 changed supported Year2024 to2023, reran and saved as a distinct row.374 removed disposable2023 search; actual reload retained2024 only, all three publication bookmarks and eleven conversations unchanged.

375–378 require unavailable accountB and owner-switch routes;379 controlled latency unavailable;380 generation/revision fixture unavailable.381–386 actually activated desktop/mobile Markdown/PDF and desktop BibTeX/CSV exports; app success messages observed, but actual file/preview access unavailable under prior browser security denial. No toast-only PASS, guessed downloaded content, or restriction bypass.387–390 lack accepted/unconfigured/provider-failure/working-provider fixtures.

## Integrity

Unchanged live SHA c903b65ce3f8f49fe72416ca8948d215a0690a49 checked read-only in Render. No application/frozen-test/config edits or paid generation. Scored interactions use actual Chrome screenshots and pointer/keyboard. JPEG originals retained and canonical PNGs faithfully converted.373 capture02 appended digits accidentally, corrected before submitting; no incorrect query sent.381 initially used an incorrect plural path; recovered through visible Saved answers to observed /answer/18, not scored as application failure.382 capture01 is a viewport transition and excluded from canonical evidence. No PDF/file contents were inspected.

## Cases

| Test | Status | Observation |
|---|---|
| [ME3-CUA-0371](../../evidence/ME3-CUA-0371/actions.md) | PASS | After actual browser reload, opened persisted saved search and clicked its diabetes row. Form restored diabetes/2024/Clinical Trial/Publication date and reran real PubMed, showing16 publications and Saved search loaded. |
| [ME3-CUA-0372](../../evidence/ME3-CUA-0372/actions.md) | PASS | One persisted diabetes/2024/Clinical Trial/pub-date search exists after reload/rerun. Attempted same Search saved control again; it remains inactive and list stays exactly one equivalent row. |
| [ME3-CUA-0373](../../evidence/ME3-CUA-0373/actions.md) | PASS | Changed supported Year field from2024 to2023, reran real search and saved. Saved searches now contains distinct2023 and2024 diabetes/Clinical Trial/pub-date rows; current unchanged parameters show Search saved guard. |
| [ME3-CUA-0374](../../evidence/ME3-CUA-0374/actions.md) | PASS | Removed disposable2023 saved search. Actual reload shows only2024 row; all three saved PMIDs6373426/33551565/39878158 and collection names remain; all eleven conversation titles/order remain unchanged. |
| [ME3-CUA-0375](../../evidence/ME3-CUA-0375/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0376](../../evidence/ME3-CUA-0376/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0377](../../evidence/ME3-CUA-0377/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0378](../../evidence/ME3-CUA-0378/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0379](../../evidence/ME3-CUA-0379/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0380](../../evidence/ME3-CUA-0380/actions.md) | BLOCKED | Precondition review only; current owned synthetic evaluation session captured, required scored workflow not executed. |
| [ME3-CUA-0381](../../evidence/ME3-CUA-0381/actions.md) | BLOCKED | Owned answer18 exposes Export > Markdown. Activated; application shows Markdown export downloaded. Actual downloaded file or safe preview not accessible through permitted browser surface. |
| [ME3-CUA-0382](../../evidence/ME3-CUA-0382/actions.md) | BLOCKED | At390px owned answer18 Export menu and Markdown are readable/actionable; activated after clean reload and app reports Markdown export downloaded. Actual file/preview unavailable. |
| [ME3-CUA-0383](../../evidence/ME3-CUA-0383/actions.md) | BLOCKED | Desktop Export>PDF activated on owned answer18; app reports PDF export downloaded. No PDF preview opened in the permitted Chrome surface. |
| [ME3-CUA-0384](../../evidence/ME3-CUA-0384/actions.md) | BLOCKED | At390px Export>PDF reachable; activation produces readable PDF export downloaded message. Actual PDF rendering/title/status not inspected. |
| [ME3-CUA-0385](../../evidence/ME3-CUA-0385/actions.md) | BLOCKED | Observed populated answer18 source list (PMID32356626), activated BibTeX export; app reports BibTeX export downloaded. |
| [ME3-CUA-0386](../../evidence/ME3-CUA-0386/actions.md) | BLOCKED | Activated CSV export on populated answer18 source fixture (PMID32356626); app reports CSV export downloaded. |
| [ME3-CUA-0387](../../evidence/ME3-CUA-0387/actions.md) | BLOCKED | Required fixture unavailable; captured current source-backed fallback answer only, not scored as accepted/literature-only/provider-failed generation. |
| [ME3-CUA-0388](../../evidence/ME3-CUA-0388/actions.md) | BLOCKED | Required fixture unavailable; captured current source-backed fallback answer only, not scored as accepted/literature-only/provider-failed generation. |
| [ME3-CUA-0389](../../evidence/ME3-CUA-0389/actions.md) | BLOCKED | Required fixture unavailable; captured current source-backed fallback answer only, not scored as accepted/literature-only/provider-failed generation. |
| [ME3-CUA-0390](../../evidence/ME3-CUA-0390/actions.md) | BLOCKED | Required fixture unavailable; captured current source-backed fallback answer only, not scored as accepted/literature-only/provider-failed generation. |

Next automatic batch391–410.
