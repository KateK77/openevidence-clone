# ME3-CUA-0345: Bookmark publication

Status: **PASS**
Executed: 2026-11-22T21:33:24.119Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Live PubMed search39878158 returned one Electronic cigarettes for smoking cessation (Cochrane2025). Saved once; opened Saved publications shows that exact PMID/title once and prior ADA record, total2. Real official identity verified earlier164/165; no mocked publication.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_search_page_0.jpg; after.png: 07_reading_list_0.jpg

## Actions

### 2026-11-22T21:32:25.073Z — 01_search_page

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/library'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:35.175Z — 02_search_real_publication

```javascript
await activeTab.cua.click({x:651,y:487}); await activeTab.cua.type({text:'39878158'}); await activeTab.cua.click({x:1245,y:487}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:43.746Z — 03_pubmed_loaded

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:51.451Z — 04_publication_before_save

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:58.414Z — 05_save_publication

```javascript
await activeTab.cua.click({x:500,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:33:07.653Z — 06_saved_state

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:33:13.922Z — 07_reading_list

```javascript
await activeTab.cua.click({x:520,y:190}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_search_page_0.jpg](01_search_page_0.jpg)
- [02_search_real_publication_0.jpg](02_search_real_publication_0.jpg)
- [03_pubmed_loaded_0.jpg](03_pubmed_loaded_0.jpg)
- [04_publication_before_save_0.jpg](04_publication_before_save_0.jpg)
- [05_save_publication_0.jpg](05_save_publication_0.jpg)
- [06_saved_state_0.jpg](06_saved_state_0.jpg)
- [07_reading_list_0.jpg](07_reading_list_0.jpg)
