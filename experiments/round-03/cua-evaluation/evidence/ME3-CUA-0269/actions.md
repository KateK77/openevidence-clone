# ME3-CUA-0269: Failed answer still shows sources

Status: **BLOCKED**
Executed: 2026-11-22T07:02:40.655Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Owned outcomes18/19 are source-exclusion insufficiency, not failed provider generation/review.

controlled_provider_failure fixture with successful retrieval and rejected/failed generated outcome absent. No production fault induced.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_no_provider_failure_outcome_0.jpg; after.png: 02_no_provider_failure_outcome_0.jpg

## Actions

### 2026-11-22T07:02:20.895Z — 01_provider_failure_gate

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18');
```
Tool error: False

### 2026-11-22T07:02:37.804Z — 02_no_provider_failure_outcome

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_no_provider_failure_outcome_0.jpg](02_no_provider_failure_outcome_0.jpg)
