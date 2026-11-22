# ME3-CUA-0128: Missing authors or journal represented

Status: **PASS**
Executed: 2026-11-22T05:21:12.629Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared known real PMID33551565 whose official PubMed explicitly No authors listed. Searched and opened app details; explicit Authors unavailable, valid Clinical diabetes journal/2021Jan/DOI10.2337/cd21-pe01 and PMID retained; no invented author. Tested missing-authors branch of authors-or-journal scenario.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_author_result_0.jpg; after.png: 08_authors_unavailable_0.jpg

## Actions

### 2026-11-22T05:20:18.446Z — 01_missing_author_start

```javascript
await authorFixture.close(); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:20:25.306Z — 02_missing_author_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'33551565'});
```
Tool error: False

### 2026-11-22T05:20:32.816Z — 03_submit_author_fixture

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:20:39.103Z — 04_author_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:20:47.224Z — 05_author_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:20:53.744Z — 06_open_author_details

```javascript
await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:21:00.556Z — 07_author_expanded

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:21:10.005Z — 08_authors_unavailable

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_missing_author_query_0.jpg](02_missing_author_query_0.jpg)
- [04_author_result_0.jpg](04_author_result_0.jpg)
- [05_author_detail_control_0.jpg](05_author_detail_control_0.jpg)
- [07_author_expanded_0.jpg](07_author_expanded_0.jpg)
- [08_authors_unavailable_0.jpg](08_authors_unavailable_0.jpg)
