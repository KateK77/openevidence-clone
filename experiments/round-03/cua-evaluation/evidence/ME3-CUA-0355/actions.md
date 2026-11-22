# ME3-CUA-0355: Duplicate publication save prevented

Status: **PASS**
Executed: 2026-11-22T21:44:18.082Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Saved unsaved PMID33551565 once. Save control becomes Saved; clicked same Saved control without unsave, no new-save feedback or count increment. Reading list total2 contains exact ADA PMID33551565 once plus prior39878158. UI prevents second save.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_search_unsaved_publication_0.jpg; after.png: 06_no_duplicate_list_0.jpg

## Actions

### 2026-11-22T21:43:26.157Z — 01_search_unsaved_publication

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/library'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:43:35.556Z — 02_search_pmid

```javascript
await activeTab.cua.click({x:650,y:487}); await activeTab.cua.type({text:'33551565'}); await activeTab.cua.click({x:1245,y:487}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:43:45.229Z — 03_unsaved_record

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:43:52.801Z — 04_save_once

```javascript
await activeTab.cua.click({x:500,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:44:01.629Z — 05_attempt_repeat_saved

```javascript
await activeTab.cua.click({x:482,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:44:09.210Z — 06_no_duplicate_list

```javascript
await activeTab.cua.click({x:520,y:190}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_search_unsaved_publication_0.jpg](01_search_unsaved_publication_0.jpg)
- [02_search_pmid_0.jpg](02_search_pmid_0.jpg)
- [03_unsaved_record_0.jpg](03_unsaved_record_0.jpg)
- [04_save_once_0.jpg](04_save_once_0.jpg)
- [05_attempt_repeat_saved_0.jpg](05_attempt_repeat_saved_0.jpg)
- [06_no_duplicate_list_0.jpg](06_no_duplicate_list_0.jpg)
