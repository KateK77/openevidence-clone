# ME3-CUA-0368: Remove publication from collection only

Status: **PASS**
Executed: 2026-11-22T21:56:38.996Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Clearing PMID39878158 Collection and updating removed it from CUA365 desktop collection; main Saved publications still shows the same article as Saved with blank Collection. PMID6373426 remains in the collection.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_collection_member_before_0.jpg; after.png: 04_show_standalone_bookmark_0.jpg

## Actions

### 2026-11-22T21:53:28.506Z — 01_collection_member_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:53:31.238Z — 02_remove_membership_only

```javascript
await activeTab.cua.click({x:530,y:721}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:379,y:776}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:56:12.697Z — 03_membership_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:56:26.976Z — 04_show_standalone_bookmark

```javascript
await activeTab.cua.click({x:550,y:326}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.scroll({x:1050,y:650,scrollY:1400,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_collection_member_before_0.jpg](01_collection_member_before_0.jpg)
- [02_remove_membership_only_0.jpg](02_remove_membership_only_0.jpg)
- [03_membership_result_0.jpg](03_membership_result_0.jpg)
- [04_show_standalone_bookmark_0.jpg](04_show_standalone_bookmark_0.jpg)
