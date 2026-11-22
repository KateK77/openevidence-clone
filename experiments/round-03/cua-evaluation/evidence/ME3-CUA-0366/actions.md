# ME3-CUA-0366: Create publication collection

Status: **PASS**
Executed: 2026-11-22T21:52:23.852Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 created CUA366 mobile collection on independently saved33551565 using Collection/Update collection. Saved/Changes saved successfully readable; filtering by exact collection name returns only ADA member. Inline collection representation, no separate directory. Controls/status fit mobile.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_collection_preparation_0.jpg; after.png: 05_mobile_collection_list_0.jpg

## Actions

### 2026-11-22T21:51:38.109Z — 01_mobile_collection_preparation

```javascript
await activeTab.cua.click({x:560,y:98}); await activeTab.cua.type({text:'33551565'}); await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:51:46.901Z — 02_mobile_collection_controls

```javascript
await activeTab.cua.scroll({x:200,y:700,scrollY:260,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:51:54.868Z — 03_mobile_create_collection

```javascript
await activeTab.cua.click({x:176,y:666}); await activeTab.cua.type({text:'CUA366 mobile collection'}); await activeTab.cua.click({x:101,y:722}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:52:02.184Z — 04_mobile_collection_saved

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:52:14.021Z — 05_mobile_collection_list

```javascript
await activeTab.cua.click({x:170,y:228}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'CUA366 mobile collection'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_collection_preparation_0.jpg](01_mobile_collection_preparation_0.jpg)
- [02_mobile_collection_controls_0.jpg](02_mobile_collection_controls_0.jpg)
- [03_mobile_create_collection_0.jpg](03_mobile_create_collection_0.jpg)
- [04_mobile_collection_saved_0.jpg](04_mobile_collection_saved_0.jpg)
- [05_mobile_collection_list_0.jpg](05_mobile_collection_list_0.jpg)
