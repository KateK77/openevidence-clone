# ME3-CUA-0162: Canonical metadata update does not rewrite old answer

Status: **BLOCKED**
Executed: 2026-11-22T05:57:51.672Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

A saved source snapshot now exists (/answer/18), but no documented isolated canonical-metadata update fixture exists.

Cannot arrange the required two canonical versions without unsupported mutation of live data. Normal reopen alone cannot prove snapshot immutability after canonical update.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_precondition_no_update_fixture_0.jpg; after.png: 01_precondition_no_update_fixture_0.jpg

## Actions

### 2026-11-22T05:57:49.376Z — 01_precondition_no_update_fixture

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_precondition_no_update_fixture_0.jpg](01_precondition_no_update_fixture_0.jpg)
