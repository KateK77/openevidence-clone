# ME3-CUA-0371: Rerun saved search

Status: **PASS**
Executed: 2026-11-22T22:00:15.264Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

After actual browser reload, opened persisted saved search and clicked its diabetes row. Form restored diabetes/2024/Clinical Trial/Publication date and reran real PubMed, showing16 publications and Saved search loaded.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_open_saved_search_list_0.jpg; after.png: 05_rerun_results_0.jpg

## Actions

### 2026-11-22T21:59:11.455Z — 01_saved_search_baseline

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:59:22.367Z — 02_persisted_saved_search

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:59:34.874Z — 03_open_saved_search_list

```javascript
await activeTab.cua.click({x:390,y:697}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:59:44.924Z — 04_rerun_saved_search

```javascript
await activeTab.cua.click({x:630,y:754}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:00:03.584Z — 05_rerun_results

```javascript
await activeTab.cua.scroll({x:1050,y:640,scrollY:320,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_saved_search_baseline_0.jpg](01_saved_search_baseline_0.jpg)
- [02_persisted_saved_search_0.jpg](02_persisted_saved_search_0.jpg)
- [03_open_saved_search_list_0.jpg](03_open_saved_search_list_0.jpg)
- [04_rerun_saved_search_0.jpg](04_rerun_saved_search_0.jpg)
- [05_rerun_results_0.jpg](05_rerun_results_0.jpg)
