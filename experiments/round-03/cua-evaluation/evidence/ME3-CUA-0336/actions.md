# ME3-CUA-0336: Search clearing restores history

Status: **PASS**
Executed: 2026-11-22T21:25:25.281Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390x844, CUA323 filtered to one exact title. Clearing input and submitting Search restored all 12 known conversations without refresh; vertical scrolling exposes all rows with no horizontal clipping. Capture02 was before the corrected input interaction, not a filtered result.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_mobile_filter_corrected_0.jpg; after.png: 05_mobile_remaining_restored_0.jpg

## Actions

### 2026-11-22T21:24:36.216Z — 01_mobile_before

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:24:48.876Z — 02_mobile_filter

```javascript
await activeTab.cua.click({x:150,y:132}); await activeTab.cua.type({text:'CUA323'}); await activeTab.cua.click({x:327,y:132}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:24:58.873Z — 03_mobile_filter_corrected

```javascript
await activeTab.cua.click({x:150,y:371}); await activeTab.cua.type({text:'CUA323'}); await activeTab.cua.click({x:327,y:371}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:25:07.299Z — 04_mobile_clear

```javascript
await activeTab.cua.click({x:150,y:371}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:342,y:371}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:25:16.089Z — 05_mobile_remaining_restored

```javascript
await activeTab.cua.scroll({x:202,y:700,scrollY:596,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_before_0.jpg](01_mobile_before_0.jpg)
- [02_mobile_filter_0.jpg](02_mobile_filter_0.jpg)
- [03_mobile_filter_corrected_0.jpg](03_mobile_filter_corrected_0.jpg)
- [04_mobile_clear_0.jpg](04_mobile_clear_0.jpg)
- [05_mobile_remaining_restored_0.jpg](05_mobile_remaining_restored_0.jpg)
