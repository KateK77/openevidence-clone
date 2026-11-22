# ME3-CUA-0108: Results date-sorting control

Status: **FAIL**
Executed: 2026-11-22T04:46:36.697Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile selected Publication date and submitted diabetes search; observed Searching then16 results. Adjacent readable cards show PMID43018112 year2026 above PMID43044620 year2027, reproducing desktop order discrepancy. No date metadata limitation explanation visible.

Date-sorted results are not ordered by displayed year; same defect as107. Controls and cards otherwise fit mobile width.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:45:15.280Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:45:23.165Z — top

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:45:32.432Z — before

```javascript
await tab.cua.click({x:263,y:723}); await tab.cua.keypress({keys:['ARROWUP']}); await tab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:45:42.747Z — date_selected

```javascript
await tab.cua.click({x:263,y:723}); await tab.cua.keypress({keys:['ARROWDOWN']}); await tab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:45:55.042Z — submit

```javascript
await tab.cua.click({x:180,y:563}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:01.771Z — results_scroll

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:09.699Z — order1

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:22.133Z — scroll2

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:28.497Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [date_selected_0.jpg](date_selected_0.jpg)
- [order1_0.jpg](order1_0.jpg)
- [results_scroll_0.jpg](results_scroll_0.jpg)
- [scroll2_0.jpg](scroll2_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
- [top_0.jpg](top_0.jpg)
