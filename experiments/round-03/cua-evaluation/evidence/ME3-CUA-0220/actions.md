# ME3-CUA-0220: Wrong-language draft gets corrective attempt

Status: **BLOCKED**
Executed: 2026-11-22T06:38:07.132Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

No isolated controlled provider returning English first then Chinese correction is supplied.

Cannot observe correction count/final accepted language without wrong_language_fixture.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_missing_required_fixture_0.jpg; after.png: 02_missing_required_fixture_0.jpg

## Actions

### 2026-11-22T06:37:50.545Z — 01_desktop_fault_precondition

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:38:04.076Z — 02_missing_required_fixture

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_missing_required_fixture_0.jpg](02_missing_required_fixture_0.jpg)
