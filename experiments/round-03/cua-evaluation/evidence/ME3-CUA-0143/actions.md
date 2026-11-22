# ME3-CUA-0143: Sorting after filters remains coherent

Status: **PASS**
Executed: 2026-11-22T05:39:12.138Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

After broad diabetes search, applied Nature+Year2024 under Relevance, then changed to Publication date and resubmitted. Filters remained; top record changed from CGRP sensory neurons... to Determining structures of RNA conformers using AFM and deep neural networks (PMID39695231). First3 cards are Nature2024. Opened top details matched title/PMID and showed Nature,Electronic publication2024 12 18,Journal issue2025Jan. Sampled top of filtered set; no full16 date audit.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_filtered_relevance_0.jpg; after.png: 11_sorted_record_details_0.jpg

## Actions

### 2026-11-22T05:37:13.065Z — 01_sort_after_filters_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:37:21.847Z — 02_broad_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'diabetes'});
```
Tool error: False

### 2026-11-22T05:37:32.954Z — 03_broad_submit

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:37:42.388Z — 04_set_journal_year

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:680,y:577}); await activeTab.cua.type({text:'Nature'});
```
Tool error: False

### 2026-11-22T05:37:50.660Z — 05_apply_filters_relevance

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:37:58.226Z — 06_filtered_relevance

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1220,y:579}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:38:07.011Z — 07_apply_date_sort

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:38:13.777Z — 08_sorted_filtered_top

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:38:26.222Z — 09_top_record_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:38:34.181Z — 10_open_top_record

```javascript
await activeTab.cua.click({x:436,y:112});
```
Tool error: False

### 2026-11-22T05:38:58.228Z — 11_sorted_record_details

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_broad_query_0.jpg](02_broad_query_0.jpg)
- [04_set_journal_year_0.jpg](04_set_journal_year_0.jpg)
- [06_filtered_relevance_0.jpg](06_filtered_relevance_0.jpg)
- [08_sorted_filtered_top_0.jpg](08_sorted_filtered_top_0.jpg)
- [09_top_record_control_0.jpg](09_top_record_control_0.jpg)
- [11_sorted_record_details_0.jpg](11_sorted_record_details_0.jpg)
