# ME3-CUA-0116: Article-type filter

Status: **PASS**
Executed: 2026-11-22T05:06:56.350Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Clinical Trial filter on diabetes returned 16 records; all 16 visually inspected with Clinical Trial, Controlled Clinical Trial or Randomized Controlled Trial metadata badges. Several titles lack 'trial', e.g. Gastroesophageal reflux in diabetes mellitus (PMID10201457), showing metadata-based inclusion rather than title-only matching.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_choose_type_0.jpg; after.png: 11_trial_metadata_page6_0.jpg

## Actions

### 2026-11-22T05:05:32.754Z — 01_return_filters

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:05:40.596Z — 02_choose_type

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:680,y:577}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:960,y:579}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:05:50.322Z — 03_type_selected

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:05:57.057Z — 04_apply_type

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:06:02.018Z — 05_trial_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:10.744Z — 06_trial_metadata_page1

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:18.741Z — 07_trial_metadata_page2

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:27.165Z — 08_trial_metadata_page3

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:34.811Z — 09_trial_metadata_page4

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:42.177Z — 10_trial_metadata_page5

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:06:48.489Z — 11_trial_metadata_page6

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

## Original captures

- [02_choose_type_0.jpg](02_choose_type_0.jpg)
- [03_type_selected_0.jpg](03_type_selected_0.jpg)
- [05_trial_results_0.jpg](05_trial_results_0.jpg)
- [06_trial_metadata_page1_0.jpg](06_trial_metadata_page1_0.jpg)
- [07_trial_metadata_page2_0.jpg](07_trial_metadata_page2_0.jpg)
- [08_trial_metadata_page3_0.jpg](08_trial_metadata_page3_0.jpg)
- [09_trial_metadata_page4_0.jpg](09_trial_metadata_page4_0.jpg)
- [10_trial_metadata_page5_0.jpg](10_trial_metadata_page5_0.jpg)
- [11_trial_metadata_page6_0.jpg](11_trial_metadata_page6_0.jpg)
