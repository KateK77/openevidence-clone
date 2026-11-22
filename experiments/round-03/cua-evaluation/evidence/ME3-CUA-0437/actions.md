# ME3-CUA-0437: Mobile evidence table contained scroll

Status: **BLOCKED**
Executed: 2026-11-22T22:27:41.941Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Known saved answer18 has one retrieved retracted source; required evidence-heavy saved-answer fixture unavailable.

Single-source fixture cannot establish required evidence-heavy table behavior; no paid synthesis or seeded production data.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_fixture_settled_0.jpg; after.png: 02_fixture_settled_0.jpg

## Actions

### 2026-11-22T22:27:36.834Z — 01_fixture_precondition

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:39.668Z — 02_fixture_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_fixture_precondition_0.jpg](01_fixture_precondition_0.jpg)
- [02_fixture_settled_0.jpg](02_fixture_settled_0.jpg)
