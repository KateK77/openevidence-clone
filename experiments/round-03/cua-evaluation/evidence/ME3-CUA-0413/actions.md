# ME3-CUA-0413: Private URL unknown ID safe failure

Status: **PASS**
Executed: 2026-11-22T22:16:54.222Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Authenticated nonexistent /answer/999999999 displays No Turn matches the given query, no trace/unrelated answer. Sidebar Research history successfully recovers to owned list.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_owned_baseline_settled_0.jpg; after.png: 03_nonexistent_id_0.jpg

## Actions

### 2026-11-22T22:16:21.225Z — 01_owned_answer_baseline

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:16:31.379Z — 02_owned_baseline_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:16:36.860Z — 03_nonexistent_id

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/999999999'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:16:45.060Z — 04_navigation_recovery

```javascript
await activeTab.cua.click({x:112,y:284}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_owned_answer_baseline_0.jpg](01_owned_answer_baseline_0.jpg)
- [02_owned_baseline_settled_0.jpg](02_owned_baseline_settled_0.jpg)
- [03_nonexistent_id_0.jpg](03_nonexistent_id_0.jpg)
- [04_navigation_recovery_0.jpg](04_navigation_recovery_0.jpg)
