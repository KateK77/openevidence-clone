# ME3-CUA-0374: Remove saved search

Status: **PASS**
Executed: 2026-11-22T22:05:19.650Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Removed disposable2023 saved search. Actual reload shows only2024 row; all three saved PMIDs6373426/33551565/39878158 and collection names remain; all eleven conversation titles/order remain unchanged.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_expand_two_saved_searches_0.jpg; after.png: 08_only_2024_search_0.jpg

## Actions

### 2026-11-22T22:02:44.356Z — 01_history_baseline

```javascript
await activeTab.cua.click({x:112,y:284}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:03:00.210Z — 02_history_baseline_bottom

```javascript
await activeTab.cua.scroll({x:1050,y:670,scrollY:750,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:03:04.893Z — 03_return_saved_search

```javascript
await activeTab.cua.click({x:109,y:418}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:03:22.769Z — 04_expand_two_saved_searches

```javascript
await activeTab.cua.click({x:395,y:680}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:03:38.871Z — 05_remove_disposable_2023_search

```javascript
await activeTab.cua.click({x:1335,y:737}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:03:52.166Z — 06_reload_after_removal

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:04:20.039Z — 07_remaining_after_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:04:37.412Z — 08_only_2024_search

```javascript
await activeTab.cua.click({x:390,y:699}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:04:40.752Z — 09_publications_unaffected

```javascript
await activeTab.cua.click({x:110,y:465}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:04:54.848Z — 10_remaining_publication_identity

```javascript
await activeTab.cua.scroll({x:1050,y:650,scrollY:1300,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:04:59.388Z — 11_history_unchanged

```javascript
await activeTab.cua.click({x:110,y:284}); await activeTab.cua.scroll({x:1050,y:650,scrollY:700,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_history_baseline_0.jpg](01_history_baseline_0.jpg)
- [02_history_baseline_bottom_0.jpg](02_history_baseline_bottom_0.jpg)
- [03_return_saved_search_0.jpg](03_return_saved_search_0.jpg)
- [04_expand_two_saved_searches_0.jpg](04_expand_two_saved_searches_0.jpg)
- [05_remove_disposable_2023_search_0.jpg](05_remove_disposable_2023_search_0.jpg)
- [06_reload_after_removal_0.jpg](06_reload_after_removal_0.jpg)
- [07_remaining_after_reload_0.jpg](07_remaining_after_reload_0.jpg)
- [08_only_2024_search_0.jpg](08_only_2024_search_0.jpg)
- [09_publications_unaffected_0.jpg](09_publications_unaffected_0.jpg)
- [10_remaining_publication_identity_0.jpg](10_remaining_publication_identity_0.jpg)
- [11_history_unchanged_0.jpg](11_history_unchanged_0.jpg)
