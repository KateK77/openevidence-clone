# ME3-CUA-0327: History date descending order

Status: **PASS**
Executed: 2026-11-22T07:41:42.361Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

390px toggled Oldest first→Newest first; newest known dated threadCUA323 returns first, followed by32356626/latest脊髓空洞症/A150, matching desktop326 seeded chronology. Selected value and order replace oldest list. Date labels hidden mobile remains separate316FAIL; ordering verified against known dated identities.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_newest_baseline_0.jpg; after.png: 06_mobile_newest_order_0.jpg

## Actions

### 2026-11-22T07:40:40.560Z — 01_mobile_sort

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T07:40:48.907Z — 02_mobile_newest_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:41:00.334Z — 03_mobile_oldest

```javascript
await activeTab.cua.click({x:191,y:423}); await activeTab.cua.keypress({keys:['END']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:41:08.860Z — 04_mobile_oldest_order

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:41:20.047Z — 05_mobile_select_newest

```javascript
await activeTab.cua.click({x:191,y:423}); await activeTab.cua.keypress({keys:['HOME']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:41:30.059Z — 06_mobile_newest_order

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_newest_baseline_0.jpg](02_mobile_newest_baseline_0.jpg)
- [04_mobile_oldest_order_0.jpg](04_mobile_oldest_order_0.jpg)
- [06_mobile_newest_order_0.jpg](06_mobile_newest_order_0.jpg)
