# ME3-CUA-0127: Missing DOI represented

Status: **PASS**
Executed: 2026-11-22T05:19:52.392Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Searched previously official-verified PMID6373426 lacking DOI and opened details. DOI explicitly Unavailable; valid authors, journal,1984Jan journal issue, source abstract and clickable PMID6373426 retained. No fabricated DOI/link.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_missing_doi_result_0.jpg; after.png: 08_doi_unavailable_and_pmid_0.jpg

## Actions

### 2026-11-22T05:18:55.791Z — 01_missing_doi_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:19:02.498Z — 02_missing_doi_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'6373426'});
```
Tool error: False

### 2026-11-22T05:19:10.037Z — 03_submit_missing_doi

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:19:18.996Z — 04_missing_doi_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:19:26.299Z — 05_doi_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:19:32.769Z — 06_open_doi_details

```javascript
await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:19:39.978Z — 07_doi_expanded

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:19:49.510Z — 08_doi_unavailable_and_pmid

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_missing_doi_query_0.jpg](02_missing_doi_query_0.jpg)
- [04_missing_doi_result_0.jpg](04_missing_doi_result_0.jpg)
- [05_doi_control_0.jpg](05_doi_control_0.jpg)
- [07_doi_expanded_0.jpg](07_doi_expanded_0.jpg)
- [08_doi_unavailable_and_pmid_0.jpg](08_doi_unavailable_and_pmid_0.jpg)
