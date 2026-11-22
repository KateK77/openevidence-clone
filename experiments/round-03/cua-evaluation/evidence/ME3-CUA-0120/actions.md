# ME3-CUA-0120: Clear filters restores relevant results

Status: **PASS**
Executed: 2026-11-22T05:11:18.358Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Starting from applied Year2024+Clinical Trial, cleared Year and selected Any type, then searched the unchanged diabetes keyword. Any year/Any journal/Any type and unchecked Free full text were visible;16 broad results restored with original first title Diagnosis and Management of Central Diabetes Insipidus in Adults.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_clear_two_filters_0.jpg; after.png: 04_desktop_filters_restored_0.jpg

## Actions

### 2026-11-22T05:10:46.609Z — 01_two_filters_before

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:10:57.834Z — 02_clear_two_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:960,y:579}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:11:08.189Z — 03_submit_cleared_filters

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:11:15.372Z — 04_desktop_filters_restored

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_clear_two_filters_0.jpg](02_clear_two_filters_0.jpg)
- [04_desktop_filters_restored_0.jpg](04_desktop_filters_restored_0.jpg)
