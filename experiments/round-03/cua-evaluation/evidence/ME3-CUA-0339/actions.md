# ME3-CUA-0339: Deletion preserves unrelated publication

Status: **PASS**
Executed: 2026-11-22T21:29:00.833Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Independently searched and bookmarked real PMID33551565, ADA's Standards of Medical Care in Diabetes. Deleted synthetic evaluation thread17 containing answer19 with that sole source (source association additionally captured in333). Saved publications still contains exactly one unchanged PMID/title and Saved state.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 07_saved_list_before_0.jpg; after.png: 11_saved_publication_retained_0.jpg

## Actions

### 2026-11-22T21:27:27.655Z — 01_publication_search

```javascript
await activeTab.cua.click({x:110,y:418}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:27:37.438Z — 02_search_safe_pmid

```javascript
await activeTab.cua.click({x:651,y:480}); await activeTab.cua.type({text:'33551565'}); await activeTab.cua.click({x:1245,y:480}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:27:45.583Z — 03_real_pmid_result

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:27:52.890Z — 04_publication_controls

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:04.825Z — 05_independent_bookmark

```javascript
await activeTab.cua.click({x:500,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:11.701Z — 06_saved_publication_before

```javascript
await activeTab.cua.click({x:110,y:465}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:20.412Z — 07_saved_list_before

```javascript
await activeTab.cua.click({x:520,y:190}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:27.950Z — 08_target_thread

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/17'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:35.689Z — 09_disposable_confirm_prompt

```javascript
await activeTab.cua.click({x:458,y:362}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:42.569Z — 10_confirm_delete

```javascript
await activeTab.cua.click({x:791,y:442}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:28:50.489Z — 11_saved_publication_retained

```javascript
await activeTab.cua.click({x:110,y:460}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_publication_search_0.jpg](01_publication_search_0.jpg)
- [02_search_safe_pmid_0.jpg](02_search_safe_pmid_0.jpg)
- [03_real_pmid_result_0.jpg](03_real_pmid_result_0.jpg)
- [04_publication_controls_0.jpg](04_publication_controls_0.jpg)
- [05_independent_bookmark_0.jpg](05_independent_bookmark_0.jpg)
- [06_saved_publication_before_0.jpg](06_saved_publication_before_0.jpg)
- [07_saved_list_before_0.jpg](07_saved_list_before_0.jpg)
- [08_target_thread_0.jpg](08_target_thread_0.jpg)
- [09_disposable_confirm_prompt_0.jpg](09_disposable_confirm_prompt_0.jpg)
- [10_confirm_delete_0.jpg](10_confirm_delete_0.jpg)
- [11_saved_publication_retained_0.jpg](11_saved_publication_retained_0.jpg)
