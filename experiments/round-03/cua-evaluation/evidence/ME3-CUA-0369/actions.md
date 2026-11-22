# ME3-CUA-0369: Delete collection and preserve saved items

Status: **FAIL**
Executed: 2026-11-22T21:57:11.670Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared CUA365 desktop collection containing PMID6373426 and39878158. Inspected top, bottom and filtered collection view: only per-article Collection input/Update collection and Remove from library are exposed; no collection Delete or confirmation workflow.

Required collection deletion is unavailable in the visible UI. Removing publications or clearing membership one article at a time would not exercise the required Delete collection workflow; neither was substituted.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_collection_management_top_0.jpg; after.png: 04_filtered_collection_no_delete_0.jpg

## Actions

### 2026-11-22T21:56:39.262Z — 01_prepare_two_member_collection

```javascript
await activeTab.cua.click({x:530,y:720}); await activeTab.cua.type({text:'CUA365 desktop collection'}); await activeTab.cua.click({x:379,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:56:49.235Z — 02_two_member_saved_bottom_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:56:52.371Z — 03_collection_management_top

```javascript
await activeTab.cua.scroll({x:1050,y:450,scrollY:-2400,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:57:01.628Z — 04_filtered_collection_no_delete

```javascript
await activeTab.cua.click({x:550,y:438}); await activeTab.cua.type({text:'CUA365 desktop collection'}); await activeTab.cua.scroll({x:1050,y:650,scrollY:480,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_prepare_two_member_collection_0.jpg](01_prepare_two_member_collection_0.jpg)
- [02_two_member_saved_bottom_controls_0.jpg](02_two_member_saved_bottom_controls_0.jpg)
- [03_collection_management_top_0.jpg](03_collection_management_top_0.jpg)
- [04_filtered_collection_no_delete_0.jpg](04_filtered_collection_no_delete_0.jpg)
