# ME3-CUA-0471: Hosted restart maintains persisted research

Status: **BLOCKED**
Executed: 2026-11-22T22:53:36.801Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Hosted synthetic History remains visible with CUA455/456 renamed threads and existing research data; service is currently live.

No operator-approved service restart/recovery fixture or recoverable sign-in credentials. Ordinary navigation/reload is not a restart; no deployment restart executed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_history_settled_0.jpg; after.png: 02_history_settled_0.jpg

## Actions

### 2026-11-22T22:53:23.086Z — 01_persisted_data_precondition

```javascript
await docs469.close();await activeTab.goto('https://medevidence-ai-v3.onrender.com/history');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:53:32.261Z — 02_history_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_persisted_data_precondition_0.jpg](01_persisted_data_precondition_0.jpg)
- [02_history_settled_0.jpg](02_history_settled_0.jpg)
