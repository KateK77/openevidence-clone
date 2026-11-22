# ME3-CUA-0414: Unknown conversation ID safe failure

Status: **PASS**
Executed: 2026-11-22T22:17:30.751Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Authenticated /thread/999999999 returns No Conversation matches the given query, no unrelated thread. Visible Research history backlink recovers correctly.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_owned_thread_baseline_0.jpg; after.png: 03_thread_denied_0.jpg

## Actions

### 2026-11-22T22:16:54.490Z — 01_owned_thread_baseline

```javascript
await activeTab.cua.click({x:620,y:432}); await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/16

### 2026-11-22T22:17:07.668Z — 02_nonexistent_thread

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/999999999'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:17:17.730Z — 03_thread_denied

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:17:20.580Z — 04_thread_recovery

```javascript
await activeTab.cua.click({x:356,y:299}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_owned_thread_baseline_0.jpg](01_owned_thread_baseline_0.jpg)
- [02_nonexistent_thread_0.jpg](02_nonexistent_thread_0.jpg)
- [03_thread_denied_0.jpg](03_thread_denied_0.jpg)
- [04_thread_recovery_0.jpg](04_thread_recovery_0.jpg)
