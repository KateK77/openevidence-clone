# ME3-CUA-0112: Publication year end filter

Status: **FAIL**
Executed: 2026-11-22T05:02:40.111Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Desktop search exposes one numeric 'Year' field, Journal, Article type, Sort and Free full text only. No end-year/upper-bound control or range UI is offered. Setting the single Year field to 2000 returns 16 publications but cannot express the required upper bound.

Required end-year filter is absent from visible search controls; single-year field is not an explicit upper-bound filter.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_filter_inspection_0.jpg; after.png: 08_result_after_year_0.jpg

## Actions

### 2026-11-22T05:01:33.612Z — 01_desktop_filter_controls

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:01:38.363Z — 02_filter_inspection

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:01:45.393Z — 03_single_year_field

```javascript
await activeTab.cua.click({x:420,y:578}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'2000'}); await activeTab.cua.click({x:1200,y:488});
```
Tool error: False

### 2026-11-22T05:01:52.519Z — 04_upper_bound_unavailable

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:02:02.307Z — 05_correct_numeric_input

```javascript
await activeTab.cua.click({x:396,y:576}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'2000'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:02:14.483Z — 06_settled_numeric_field

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:02:21.011Z — 07_submit_year

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:02:28.122Z — 08_result_after_year

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_filter_inspection_0.jpg](02_filter_inspection_0.jpg)
- [04_upper_bound_unavailable_0.jpg](04_upper_bound_unavailable_0.jpg)
- [05_correct_numeric_input_0.jpg](05_correct_numeric_input_0.jpg)
- [06_settled_numeric_field_0.jpg](06_settled_numeric_field_0.jpg)
- [08_result_after_year_0.jpg](08_result_after_year_0.jpg)
