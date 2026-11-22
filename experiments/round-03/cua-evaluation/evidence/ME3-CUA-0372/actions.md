# ME3-CUA-0372: Duplicate equivalent saved search

Status: **PASS**
Executed: 2026-11-22T22:00:41.238Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

One persisted diabetes/2024/Clinical Trial/pub-date search exists after reload/rerun. Attempted same Search saved control again; it remains inactive and list stays exactly one equivalent row.

UI duplicate guard observed; no claim that two duplicate save requests were accepted.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_equivalent_saved_search_0.jpg; after.png: 02_duplicate_attempt_0.jpg

## Actions

### 2026-11-22T22:00:15.510Z — 01_equivalent_saved_search

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:00:21.698Z — 02_duplicate_attempt

```javascript
await activeTab.cua.click({x:1310,y:531}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_equivalent_saved_search_0.jpg](01_equivalent_saved_search_0.jpg)
- [02_duplicate_attempt_0.jpg](02_duplicate_attempt_0.jpg)
