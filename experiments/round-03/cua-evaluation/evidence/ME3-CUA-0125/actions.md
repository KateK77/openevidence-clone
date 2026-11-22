# ME3-CUA-0125: Missing abstract represented

Status: **PASS**
Executed: 2026-11-22T05:17:45.336Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Official PubMed had explicitly No abstract available for PMID39219390 before test. App search and expanded Source abstract say 'No abstract is available for this record.' No synthetic summary/full text. Incidental title shown [Not Available] despite official French title; not part of this abstract-only assertion.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_missing_abstract_results_0.jpg; after.png: 08_no_abstract_notice_0.jpg

## Actions

### 2026-11-22T05:16:45.310Z — 01_missing_abstract_start

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:16:53.447Z — 02_missing_abstract_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'39219390'});
```
Tool error: False

### 2026-11-22T05:17:02.894Z — 03_submit_missing_abstract

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:17:09.265Z — 04_missing_abstract_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:17:18.155Z — 05_missing_abstract_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:17:24.179Z — 06_open_missing_abstract

```javascript
await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:17:30.606Z — 07_missing_abstract_expanded

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:17:42.008Z — 08_no_abstract_notice

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_missing_abstract_query_0.jpg](02_missing_abstract_query_0.jpg)
- [04_missing_abstract_results_0.jpg](04_missing_abstract_results_0.jpg)
- [05_missing_abstract_detail_control_0.jpg](05_missing_abstract_detail_control_0.jpg)
- [07_missing_abstract_expanded_0.jpg](07_missing_abstract_expanded_0.jpg)
- [08_no_abstract_notice_0.jpg](08_no_abstract_notice_0.jpg)
