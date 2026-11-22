# ME3-CUA-0364: Saved-publication no-match state

Status: **PASS**
Executed: 2026-11-22T21:50:33.102Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Nonexistent CUA364 zephyrquartz nonexistent filter yields explicit No saved publications found and instruction to clear filter. Editable filter remains; clearing restores list. No dedicated reset button, working text-clear recovery path.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_desktop_empty_filter_preparation_0.jpg; after.png: 06_recovered_0.jpg

## Actions

### 2026-11-22T21:49:29.143Z — 01_desktop_empty_filter_preparation

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.scroll({x:220,y:300,scrollY:-2000,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:49:41.331Z — 02_filter_baseline

```javascript
await activeTab.cua.scroll({x:1050,y:300,scrollY:-2000,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:49:50.641Z — 03_nonexistent_filter

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.type({text:'CUA364 zephyrquartz nonexistent'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:50:02.645Z — 04_no_match_state

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:50:10.353Z — 05_clear_recovery

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:50:19.267Z — 06_recovered

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_empty_filter_preparation_0.jpg](01_desktop_empty_filter_preparation_0.jpg)
- [02_filter_baseline_0.jpg](02_filter_baseline_0.jpg)
- [03_nonexistent_filter_0.jpg](03_nonexistent_filter_0.jpg)
- [04_no_match_state_0.jpg](04_no_match_state_0.jpg)
- [05_clear_recovery_0.jpg](05_clear_recovery_0.jpg)
- [06_recovered_0.jpg](06_recovered_0.jpg)
