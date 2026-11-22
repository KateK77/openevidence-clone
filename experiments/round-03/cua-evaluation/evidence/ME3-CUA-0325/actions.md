# ME3-CUA-0325: History date ascending order

Status: **PASS**
Executed: 2026-11-22T07:40:15.898Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Selected Oldest first; all13 owned rows inspected with Nov20 earliest,Nov21 middle,Nov22 latest. Latest editedCUA323 title is last despite alphabetic C preceding numeric/Chinese titles, matching date chronology.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_oldest_dates_0.jpg; after.png: 06_later_dates_0.jpg

## Actions

### 2026-11-22T07:39:18.373Z — 01_history

```javascript
await activeTab.cua.click({x:110,y:284});
```
Tool error: False

### 2026-11-22T07:39:24.578Z — 02_before_sort

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:39:34.655Z — 03_oldest_selection

```javascript
await activeTab.cua.click({x:1318,y:362}); await activeTab.cua.keypress({keys:['END']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:39:44.157Z — 04_oldest_dates

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:39:54.167Z — 05_later_dates_scroll

```javascript
await activeTab.cua.click({x:1043,y:297}); await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:40:02.420Z — 06_later_dates

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_before_sort_0.jpg](02_before_sort_0.jpg)
- [04_oldest_dates_0.jpg](04_oldest_dates_0.jpg)
- [06_later_dates_0.jpg](06_later_dates_0.jpg)
