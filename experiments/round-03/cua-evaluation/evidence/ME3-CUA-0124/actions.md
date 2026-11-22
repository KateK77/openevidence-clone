# ME3-CUA-0124: Missing electronic date represented

Status: **FAIL**
Executed: 2026-11-22T05:16:41.037Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared PMID6373426 from official PubMed (1984Jan issue, no electronic date). App expanded metadata shows authors,Journal,Journal issue1984Jan,DOIUnavailable, but entirely omits Electronic publication row rather than explicitly reporting unavailable.

Frozen requirement asks explicit unavailable electronic date; field is silently omitted. No fabricated date observed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_missing_date_results_0.jpg; after.png: 08_missing_date_omitted_0.jpg

## Actions

### 2026-11-22T05:15:29.083Z — 01_missing_epub_search_setup

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:15:35.183Z — 02_missing_epub_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'6373426'});
```
Tool error: False

### 2026-11-22T05:15:44.270Z — 03_submit_missing_date

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:15:51.247Z — 04_missing_date_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:15:58.407Z — 05_missing_date_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:16:23.103Z — 06_open_missing_date

```javascript
await activeTab.cua.click({x:436,y:686});
```
Tool error: False

### 2026-11-22T05:16:29.783Z — 07_missing_date_fields

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:16:38.358Z — 08_missing_date_omitted

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_missing_epub_query_0.jpg](02_missing_epub_query_0.jpg)
- [04_missing_date_results_0.jpg](04_missing_date_results_0.jpg)
- [05_missing_date_detail_control_0.jpg](05_missing_date_detail_control_0.jpg)
- [07_missing_date_fields_0.jpg](07_missing_date_fields_0.jpg)
- [08_missing_date_omitted_0.jpg](08_missing_date_omitted_0.jpg)
