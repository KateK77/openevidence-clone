# ME3-CUA-0145: Cache does not invent new publication content

Status: **PASS**
Executed: 2026-11-22T05:41:02.145Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Performed exact PMID33551565 lookup twice in same session and inspected full expanded card both times. Identity/title2021,Clinical diabetes journal,2021Jan issue,DOI10.2337/cd21-pe01,Authors unavailable and No abstract available stayed identical and matched earlier official-source verification. No unrelated canned content observed.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 07_first_complete_0.jpg; after.png: 10_second_result_metadata_0.jpg

## Actions

### 2026-11-22T05:39:16.119Z — 01_repeat_lookup_setup

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:39:26.516Z — 02_exact_pmid_clear_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'33551565'}); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:680,y:577}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:1220,y:579}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:39:41.690Z — 03_first_lookup

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:39:48.594Z — 04_first_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:39:57.352Z — 05_first_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:40:06.434Z — 06_first_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:40:16.193Z — 07_first_complete

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:40:24.527Z — 08_second_lookup

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:40:32.394Z — 09_second_result_scroll

```javascript
await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:40:48.090Z — 10_second_result_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_exact_pmid_clear_filters_0.jpg](02_exact_pmid_clear_filters_0.jpg)
- [04_first_result_0.jpg](04_first_result_0.jpg)
- [05_first_detail_control_0.jpg](05_first_detail_control_0.jpg)
- [06_first_metadata_0.jpg](06_first_metadata_0.jpg)
- [07_first_complete_0.jpg](07_first_complete_0.jpg)
- [08_second_lookup_0.jpg](08_second_lookup_0.jpg)
- [10_second_result_metadata_0.jpg](10_second_result_metadata_0.jpg)
