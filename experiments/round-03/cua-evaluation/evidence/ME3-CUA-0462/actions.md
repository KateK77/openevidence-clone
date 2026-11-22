# ME3-CUA-0462: Public research history persists

Status: **BLOCKED**
Executed: 2026-11-22T22:48:14.330Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Hosted History shows actual synthetic research threads including renamed CUA455/456, script-literal415 and PMID thread16.

Full sign-out/sign-in persistence requires recoverable credentials not supplied. Existing-session history is partial evidence only; no reauthentication executed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_settled_0.jpg; after.png: 02_settled_0.jpg

## Actions

### 2026-11-22T22:48:04.113Z — 01_history_precondition

```javascript
await activeTab.cua.click({x:110,y:284});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:07.525Z — 02_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_history_precondition_0.jpg](01_history_precondition_0.jpg)
- [02_settled_0.jpg](02_settled_0.jpg)
