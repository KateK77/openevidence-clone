# ME3-CUA-0357: Publication save progress

Status: **PASS**
Executed: 2026-11-22T21:46:27.655Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Saved previously unsaved real PMID6373426. Actual immediate screenshot shows Saving...; settled state Saved plus completion feedback and count2→3. Clicking unchanged Saved does not restart save; reading list contains correct single record. Pending and final states retained.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_real_search_0.jpg; after.png: 07_persisted_reading_list_0.jpg

## Actions

### 2026-11-22T21:45:16.791Z — 01_real_search

```javascript
await activeTab.cua.click({x:110,y:418}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:45:28.477Z — 02_search

```javascript
await activeTab.cua.click({x:650,y:480}); await activeTab.cua.type({text:'6373426'}); await activeTab.cua.click({x:1245,y:480}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:45:39.737Z — 03_unsaved_before

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:45:48.323Z — 04_save_pending

```javascript
await activeTab.cua.click({x:496,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:45:56.724Z — 05_save_complete

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:46:04.539Z — 06_unchanged_repeat

```javascript
await activeTab.cua.click({x:477,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:46:11.515Z — 07_persisted_reading_list

```javascript
await activeTab.cua.click({x:520,y:165}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_real_search_0.jpg](01_real_search_0.jpg)
- [02_search_0.jpg](02_search_0.jpg)
- [03_unsaved_before_0.jpg](03_unsaved_before_0.jpg)
- [04_save_pending_0.jpg](04_save_pending_0.jpg)
- [05_save_complete_0.jpg](05_save_complete_0.jpg)
- [06_unchanged_repeat_0.jpg](06_unchanged_repeat_0.jpg)
- [07_persisted_reading_list_0.jpg](07_persisted_reading_list_0.jpg)
