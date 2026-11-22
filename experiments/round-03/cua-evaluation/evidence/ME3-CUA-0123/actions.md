# ME3-CUA-0123: Publication date types distinguished

Status: **PASS**
Executed: 2026-11-22T05:13:58.202Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared real fixture PMID33713498 from official PubMed before scored opening: Epub2021Mar13, journal issue2021Jul. App expanded details separately label Electronic publication2021 03 13 and Journal issue2021 Jul; both match official source.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_date_record_result_0.jpg; after.png: 08_dates_readable_0.jpg

## Actions

### 2026-11-22T05:13:00.703Z — 01_date_fixture_search_setup

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:13:07.891Z — 02_known_date_record

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'33713498'});
```
Tool error: False

### 2026-11-22T05:13:20.364Z — 03_submit_known_date_record

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:13:26.499Z — 04_date_record_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:13:35.201Z — 05_date_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:13:41.109Z — 06_expand_date_details

```javascript
await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:13:46.837Z — 07_date_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:13:55.405Z — 08_dates_readable

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_known_date_record_0.jpg](02_known_date_record_0.jpg)
- [04_date_record_result_0.jpg](04_date_record_result_0.jpg)
- [05_date_detail_control_0.jpg](05_date_detail_control_0.jpg)
- [07_date_metadata_0.jpg](07_date_metadata_0.jpg)
- [08_dates_readable_0.jpg](08_dates_readable_0.jpg)
