# ME3-CUA-0439: Mobile saved collection editing

Status: **PASS**
Executed: 2026-11-22T22:29:11.619Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

390px collection field/update reachable; PMID6373426 changed to CUA439 mobile collection, success message fully visible and exact value persists after reload; no horizontal clipping.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_collection_before_0.jpg; after.png: 06_persisted_scroll_0.jpg

## Actions

### 2026-11-22T22:28:33.572Z — 01_collection_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:36.112Z — 02_edit_collection

```javascript
await activeTab.cua.click({x:150,y:617}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'CUA439 mobile collection'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:46.313Z — 03_save_collection

```javascript
await activeTab.cua.click({x:105,y:672}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:49.877Z — 04_saved_feedback

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:52.238Z — 05_reload

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:55.363Z — 06_persisted_scroll

```javascript
await activeTab.cua.scroll({x:200,y:680,scrollY:550,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_collection_before_0.jpg](01_collection_before_0.jpg)
- [02_edit_collection_0.jpg](02_edit_collection_0.jpg)
- [03_save_collection_0.jpg](03_save_collection_0.jpg)
- [04_saved_feedback_0.jpg](04_saved_feedback_0.jpg)
- [05_reload_0.jpg](05_reload_0.jpg)
- [06_persisted_scroll_0.jpg](06_persisted_scroll_0.jpg)
