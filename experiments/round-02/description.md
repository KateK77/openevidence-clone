# Round 2 scope

The user authorized a version 2 implementation based on the original platform requirements and the completed manual acceptance feedback. The previous instruction to record defects without fixing them applied to Round 1 acceptance; this round explicitly authorizes implementation.

All reports, GitHub descriptions, and repository documentation must be written in English. Chinese strings appear only as functional test inputs, terminology mappings, and captured application data.

## Baseline

- Repository: KateK77/openevidence-clone (private).
- Original source requirements: ../round-01/description.md.
- Version 1: v0.1.0-r1.
- Baseline before Round 2: 56256603ee3b10ef5bea359a73ea1a23fa4ec517.
- Round 2 branch: v2-round-02.
- Planned version tag: v2.0.0-r2.

## Requested improvements

1. Make logout immediately and consistently update the interface.
2. Retain working account isolation, persistence, literature search, history, and exports.
3. Accept short English and Chinese clinical queries.
4. Improve Chinese retrieval and explain unsupported query mapping.
5. Show unambiguous save progress/success/failure and prevent duplicate saves while unchanged.
6. Clarify saved answers versus saved publications.
7. Correct PDF/Markdown character corruption and repeated reference punctuation.
8. Identify electronic and issue publication dates.
9. Make the mobile navigation and evidence views usable at narrow widths.
10. Provide an easier, reliable startup path after the original directory/npm/port difficulties.
11. Preserve independent round comparison, test the changes, document results, and upload the new version to the private repository.

## Implementation approach

Rebuild the React presentation and interaction layer while preserving and extending the tested Django persistence and retrieval foundation. Use an additive database migration and a backup rather than recreating the user's database. Keep model unavailability transparent. Do not claim clinical validation or successful live model testing without evidence.
