# ME3-CUA-0146: PMID and DOI mismatch is not silent

Status: **BLOCKED**
Executed: 2026-11-22T05:41:04.824Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

No isolated DOI-to-wrong/unavailable-PMID upstream fixture supplied. Normal exact-identifier results are present, but no scored mismatch response was triggered.

Required controlled identifier-mismatch upstream fixture unavailable.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: precondition_0.jpg; after.png: precondition_0.jpg

## Actions

### 2026-11-22T05:41:02.386Z — precondition

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [precondition_0.jpg](precondition_0.jpg)
