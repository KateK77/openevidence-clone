# ME3-CUA-0139: Search that returns no publications

Status: **PASS**
Executed: 2026-11-22T05:35:41.929Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 unique query zephyrquartz20261122 returned0 with explicit non-absence-of-evidence wording. Edited to asthma and resubmitted;16 results restored with first Asthma: definitions and pathophysiology. Notice/actions readable and no page-wide horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_unlikely_query_0.jpg; after.png: 08_mobile_recovered_0.jpg

## Actions

### 2026-11-22T05:34:40.150Z — 01_mobile_zero_setup

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T05:34:51.108Z — 02_mobile_unlikely_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:172,y:505}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'zephyrquartz20261122'});
```
Tool error: False

### 2026-11-22T05:34:58.044Z — 03_mobile_submit_empty

```javascript
await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:35:04.705Z — 04_mobile_scroll_empty

```javascript
await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:35:12.242Z — 05_mobile_empty_notice

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:35:19.007Z — 06_mobile_edit_query

```javascript
await activeTab.cua.click({x:172,y:297}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'asthma'});
```
Tool error: False

### 2026-11-22T05:35:25.605Z — 07_mobile_resubmit

```javascript
await activeTab.cua.click({x:180,y:353});
```
Tool error: False

### 2026-11-22T05:35:39.558Z — 08_mobile_recovered

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_unlikely_query_0.jpg](02_mobile_unlikely_query_0.jpg)
- [05_mobile_empty_notice_0.jpg](05_mobile_empty_notice_0.jpg)
- [08_mobile_recovered_0.jpg](08_mobile_recovered_0.jpg)
