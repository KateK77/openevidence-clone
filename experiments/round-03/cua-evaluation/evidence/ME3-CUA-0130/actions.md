# ME3-CUA-0130: Publication detail back-navigation

Status: **PASS**
Executed: 2026-11-22T05:23:45.868Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Searched PMID39219390 with Year2024 and Publication date sort. Opened inline Abstract & publication details then collapsed back to result card. Keyword,Year2024,sort Publication date and1 result remained visible throughout. This app uses inline details, so return-to-list uses collapse rather than route back.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_filtered_context_0.jpg; after.png: 07_returned_list_context_0.jpg

## Actions

### 2026-11-22T05:22:45.084Z — 01_back_navigation_setup

```javascript
await frenchIdentity.close(); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:22:54.384Z — 02_filter_and_sort

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:1220,y:579}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:23:03.484Z — 03_submit_filtered_search

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:23:11.665Z — 04_filtered_context

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:23:20.121Z — 05_detail_control

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:23:31.672Z — 06_details_preserve_context

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:23:42.834Z — 07_returned_list_context

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_filter_and_sort_0.jpg](02_filter_and_sort_0.jpg)
- [04_filtered_context_0.jpg](04_filtered_context_0.jpg)
- [05_detail_control_0.jpg](05_detail_control_0.jpg)
- [06_details_preserve_context_0.jpg](06_details_preserve_context_0.jpg)
- [07_returned_list_context_0.jpg](07_returned_list_context_0.jpg)
