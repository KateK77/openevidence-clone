# ME3-CUA-0370: Saved search with filters

Status: **PASS**
Executed: 2026-11-22T21:58:10.601Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Searched real PubMed for diabetes, year2024, Clinical Trial, Publication date (16 publications). Saved search list shows one diabetes entry with sort:pub date, year:2024, article_type:Clinical Trial matching selected parameters.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_results_save_search_0.jpg; after.png: 06_inspect_saved_search_0.jpg

## Actions

### 2026-11-22T21:57:11.935Z — 01_search_form

```javascript
await activeTab.cua.click({x:105,y:419}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:23.049Z — 02_set_search_parameters

```javascript
await activeTab.cua.click({x:650,y:479}); await activeTab.cua.type({text:'diabetes'}); await activeTab.cua.click({x:420,y:568}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:980,y:570}); await activeTab.cua.keypress({keys:['HOME']}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.click({x:1240,y:570}); await activeTab.cua.keypress({keys:['END']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:35.148Z — 03_execute_filtered_search

```javascript
await activeTab.cua.click({x:1247,y:480}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:41.822Z — 04_results_save_search

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:49.649Z — 05_save_exact_search

```javascript
await activeTab.cua.click({x:1310,y:697}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:57.961Z — 06_inspect_saved_search

```javascript
await activeTab.cua.click({x:390,y:699}); await activeTab.cua.scroll({x:1050,y:650,scrollY:320,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_search_form_0.jpg](01_search_form_0.jpg)
- [02_set_search_parameters_0.jpg](02_set_search_parameters_0.jpg)
- [03_execute_filtered_search_0.jpg](03_execute_filtered_search_0.jpg)
- [04_results_save_search_0.jpg](04_results_save_search_0.jpg)
- [05_save_exact_search_0.jpg](05_save_exact_search_0.jpg)
- [06_inspect_saved_search_0.jpg](06_inspect_saved_search_0.jpg)
