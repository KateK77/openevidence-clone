# ME3-CUA-0286: Failed regeneration does not replace original

Status: **BLOCKED**
Executed: 2026-11-22T07:12:17.721Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Controlled failed-regeneration fixture absent; cannot force failed child then compare original.

Required frozen prerequisite unavailable; no server configuration, authentication or paid model operations changed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_missing_required_fixture_0.jpg; after.png: 01_missing_required_fixture_0.jpg

## Actions

### 2026-11-22T07:12:09.785Z — 01_missing_required_fixture

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_missing_required_fixture_0.jpg](01_missing_required_fixture_0.jpg)
