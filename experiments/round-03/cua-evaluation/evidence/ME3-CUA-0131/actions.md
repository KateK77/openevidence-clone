# ME3-CUA-0131: Publication detail back-navigation

Status: **PASS**
Executed: 2026-11-22T05:31:14.771Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 submitted PMID39219390 with Year2024 and Publication date sort. Expanded inline details then collapsed to result. Keyword,year,sort and single result persisted; controls and detail readable without page-wide overflow. Inline collapse is the app's return-to-list workflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_mobile_result_before_details_0.jpg; after.png: 08_mobile_returned_context_0.jpg

## Actions

### 2026-11-22T05:30:15.856Z — 01_mobile_context_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:30:27.600Z — 02_mobile_search_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:30:34.814Z — 03_mobile_result_scroll

```javascript
await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:30:41.111Z — 04_mobile_result_before_details

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:30:48.167Z — 05_mobile_open_details

```javascript
await activeTab.cua.click({x:146,y:606});
```
Tool error: False

### 2026-11-22T05:30:54.324Z — 06_mobile_details

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:31:03.201Z — 07_mobile_close_details

```javascript
await activeTab.cua.click({x:146,y:606});
```
Tool error: False

### 2026-11-22T05:31:12.649Z — 08_mobile_returned_context

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_search_filters_0.jpg](02_mobile_search_filters_0.jpg)
- [04_mobile_result_before_details_0.jpg](04_mobile_result_before_details_0.jpg)
- [06_mobile_details_0.jpg](06_mobile_details_0.jpg)
- [08_mobile_returned_context_0.jpg](08_mobile_returned_context_0.jpg)
