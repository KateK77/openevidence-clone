# ME3-CUA-0140: Publication types displayed

Status: **PASS**
Executed: 2026-11-22T05:36:29.997Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Opened indexed PMID6373426. Visible type badges include Clinical Trial,Controlled Clinical Trial,Journal Article,Research Support Non-U.S.Govt and U.S.Govt P.H.S.; available clinical-trial type agrees with official PubMed fixture. This record has types, so missing-type branch was not encountered.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 05_types_visible_0.jpg; after.png: 06_opened_types_0.jpg

## Actions

### 2026-11-22T05:35:42.166Z — 01_types_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:35:52.949Z — 02_known_types_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'6373426'});
```
Tool error: False

### 2026-11-22T05:36:00.220Z — 03_submit_types

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:36:06.362Z — 04_type_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:36:14.656Z — 05_types_visible

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:436,y:687});
```
Tool error: False

### 2026-11-22T05:36:27.261Z — 06_opened_types

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_known_types_query_0.jpg](02_known_types_query_0.jpg)
- [04_type_results_0.jpg](04_type_results_0.jpg)
- [05_types_visible_0.jpg](05_types_visible_0.jpg)
- [06_opened_types_0.jpg](06_opened_types_0.jpg)
