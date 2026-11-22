# ME3-CUA-0113: Year range with no matches

Status: **PASS**
Executed: 2026-11-22T05:03:24.326Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Using the available Year control to restrict diabetes to 2030 produced 0 publications with explicit no-match/non-absence-of-evidence wording. Clearing Year and searching again restored 16 publications. This checks single-year empty-state recovery; separate end-year/range UI absence is recorded in 112.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_desktop_before_zero_0.jpg; after.png: 05_restored_results_0.jpg

## Actions

### 2026-11-22T05:02:40.372Z — 01_desktop_before_zero

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'2030'});
```
Tool error: False

### 2026-11-22T05:02:48.914Z — 02_submit_empty_year

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:03:01.750Z — 03_empty_and_clear

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']});
```
Tool error: False

### 2026-11-22T05:03:09.632Z — 04_repeat_without_year

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:03:15.212Z — 05_restored_results

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_before_zero_0.jpg](01_desktop_before_zero_0.jpg)
- [02_submit_empty_year_0.jpg](02_submit_empty_year_0.jpg)
- [03_empty_and_clear_0.jpg](03_empty_and_clear_0.jpg)
- [05_restored_results_0.jpg](05_restored_results_0.jpg)
