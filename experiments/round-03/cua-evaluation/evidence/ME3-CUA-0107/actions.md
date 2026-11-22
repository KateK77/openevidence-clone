# ME3-CUA-0107: Results date-sorting control

Status: **FAIL**
Executed: 2026-11-22T04:45:15.028Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Selected Publication date for diabetes, clicked Search and observed loading then16 results. Displayed order begins2028 (PMID43062408),2028 (43062407),2026 (43018112),then2027 (43044620 and43008771). Actual order_scroll2 screenshot shows adjacent2026/2027 reversal; no date-field limitation explained.

Publication-date ordering is not monotonic by displayed year and interface supplies no transparent explanation for discrepancy.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: order_scroll2_0.jpg

## Actions

### 2026-11-22T04:43:10.675Z — setup

```javascript
await linkTab.close(); await tab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:43:20.413Z — before

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:43:28.459Z — sort_options

```javascript
await tab.cua.click({x:1204,y:573}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:43:36.465Z — options_visible

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:43:47.427Z — date_selected

```javascript
await tab.cua.keypress({keys:['ARROWDOWN']}); await tab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:43:58.529Z — apply

```javascript
await tab.cua.click({x:1204,y:483}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:06.408Z — result

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:18.138Z — order_scroll

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:26.060Z — order_1

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:34.895Z — order_scroll2

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:42.231Z — order_2

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:44:59.034Z — after

```javascript
await tab.cua.keypress({keys:['ARROWUP']}); await tab.cua.keypress({keys:['ARROWUP']}); await tab.cua.keypress({keys:['ARROWUP']}); await tab.cua.keypress({keys:['ARROWUP']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [apply_0.jpg](apply_0.jpg)
- [before_0.jpg](before_0.jpg)
- [date_selected_0.jpg](date_selected_0.jpg)
- [options_visible_0.jpg](options_visible_0.jpg)
- [order_1_0.jpg](order_1_0.jpg)
- [order_2_0.jpg](order_2_0.jpg)
- [order_scroll2_0.jpg](order_scroll2_0.jpg)
- [order_scroll_0.jpg](order_scroll_0.jpg)
- [result_0.jpg](result_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [sort_options_0.jpg](sort_options_0.jpg)
