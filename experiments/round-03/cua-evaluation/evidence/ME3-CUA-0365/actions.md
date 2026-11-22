# ME3-CUA-0365: Create publication collection

Status: **PASS**
Executed: 2026-11-22T21:51:37.852Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

In owned Saved publications created name CUA365 desktop collection through article Collection/Update collection control. Readable Saved/Changes saved successfully; collection-name filter returns member PMID6373426 only, and name survives reload. App represents collections inline and through filtering, not a separate directory.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_collection_controls_0.jpg; after.png: 06_reloaded_collection_name_0.jpg

## Actions

### 2026-11-22T21:50:33.355Z — 01_collection_controls

```javascript
await activeTab.cua.scroll({x:1050,y:723,scrollY:340,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:50:48.406Z — 02_create_named_collection

```javascript
await activeTab.cua.click({x:530,y:494}); await activeTab.cua.type({text:'CUA365 desktop collection'}); await activeTab.cua.click({x:379,y:549}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:50:57.699Z — 03_collection_saved

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:51:07.153Z — 04_collection_list

```javascript
await activeTab.cua.click({x:560,y:98}); await activeTab.cua.type({text:'CUA365 desktop collection'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:51:17.165Z — 05_collection_persisted

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:51:26.963Z — 06_reloaded_collection_name

```javascript
await activeTab.cua.scroll({x:1050,y:723,scrollY:340,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_collection_controls_0.jpg](01_collection_controls_0.jpg)
- [02_create_named_collection_0.jpg](02_create_named_collection_0.jpg)
- [03_collection_saved_0.jpg](03_collection_saved_0.jpg)
- [04_collection_list_0.jpg](04_collection_list_0.jpg)
- [05_collection_persisted_0.jpg](05_collection_persisted_0.jpg)
- [06_reloaded_collection_name_0.jpg](06_reloaded_collection_name_0.jpg)
