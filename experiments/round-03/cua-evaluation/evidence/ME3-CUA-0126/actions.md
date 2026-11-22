# ME3-CUA-0126: Missing abstract represented

Status: **PASS**
Executed: 2026-11-22T05:18:55.551Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 searched official-verified no-abstract PMID39219390, collapsed and reopened details. Source abstract clearly states No abstract is available for this record; notice/PMID/metadata fit readable mobile layout without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_mobile_collapsed_0.jpg; after.png: 09_mobile_no_abstract_notice_0.jpg

## Actions

### 2026-11-22T05:17:45.567Z — 01_mobile_missing_abstract_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:17:54.806Z — 02_mobile_known_record_search

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:18:01.261Z — 03_mobile_result_scroll

```javascript
await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:18:06.926Z — 04_mobile_detail_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:18:12.763Z — 05_mobile_collapse

```javascript
await activeTab.cua.click({x:143,y:393});
```
Tool error: False

### 2026-11-22T05:18:22.508Z — 06_mobile_collapsed

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:18:28.159Z — 07_mobile_open_details

```javascript
await activeTab.cua.click({x:146,y:606});
```
Tool error: False

### 2026-11-22T05:18:42.150Z — 08_mobile_opened

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:351,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:18:53.242Z — 09_mobile_no_abstract_notice

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_known_record_search_0.jpg](02_mobile_known_record_search_0.jpg)
- [04_mobile_detail_before_0.jpg](04_mobile_detail_before_0.jpg)
- [06_mobile_collapsed_0.jpg](06_mobile_collapsed_0.jpg)
- [08_mobile_opened_0.jpg](08_mobile_opened_0.jpg)
- [09_mobile_no_abstract_notice_0.jpg](09_mobile_no_abstract_notice_0.jpg)
