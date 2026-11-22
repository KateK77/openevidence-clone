# ME3-CUA-0271: Detail view handles long quotations

Status: **BLOCKED**
Executed: 2026-11-22T07:04:26.668Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile owned outcome18 contains no accepted claims; earlier long raw PubMed abstract is not a controlled multiple-claim answer.

Required controlled answer with multiple long evidence excerpts absent. Raw-source scrolling cannot establish claim association behavior.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_no_long_claim_fixture_0.jpg; after.png: 02_mobile_no_long_claim_fixture_0.jpg

## Actions

### 2026-11-22T07:04:06.908Z — 01_mobile_long_claim_gate

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T07:04:18.677Z — 02_mobile_no_long_claim_fixture

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_no_long_claim_fixture_0.jpg](02_mobile_no_long_claim_fixture_0.jpg)
