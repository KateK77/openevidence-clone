# ME3-CUA-0346: Bookmark publication

Status: **PASS**
Executed: 2026-11-22T21:34:32.804Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 real PMID6373426 search returned Minnesota Diabetes Complications Clinical Trial cognitive-functions publication1984. Saved, navigated to Saved publications: count3 (previous2), exact PMID/title appears once with Saved state. Card wraps and actions readable, no horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_search_page_0.jpg; after.png: 07_mobile_reading_list_top_0.jpg

## Actions

### 2026-11-22T21:33:24.371Z — 01_mobile_search_page

```javascript
await activeTab.cua.click({x:100,y:418}); await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:33:32.340Z — 02_mobile_search

```javascript
await activeTab.cua.click({x:170,y:505}); await activeTab.cua.type({text:'6373426'}); await activeTab.cua.click({x:184,y:561}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:33:42.249Z — 03_mobile_result

```javascript
await activeTab.cua.scroll({x:200,y:700,scrollY:625,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:33:54.748Z — 04_mobile_save

```javascript
await activeTab.cua.click({x:89,y:721}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:34:04.519Z — 05_mobile_saved_list

```javascript
await activeTab.cua.click({x:275,y:754}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:34:12.907Z — 06_open_reading_list

```javascript
await activeTab.cua.click({x:81,y:775}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:34:23.303Z — 07_mobile_reading_list_top

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_search_page_0.jpg](01_mobile_search_page_0.jpg)
- [02_mobile_search_0.jpg](02_mobile_search_0.jpg)
- [03_mobile_result_0.jpg](03_mobile_result_0.jpg)
- [04_mobile_save_0.jpg](04_mobile_save_0.jpg)
- [05_mobile_saved_list_0.jpg](05_mobile_saved_list_0.jpg)
- [06_open_reading_list_0.jpg](06_open_reading_list_0.jpg)
- [07_mobile_reading_list_top_0.jpg](07_mobile_reading_list_top_0.jpg)
