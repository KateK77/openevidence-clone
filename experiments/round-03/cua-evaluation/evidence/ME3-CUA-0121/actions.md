# ME3-CUA-0121: Clear filters restores relevant results

Status: **PASS**
Executed: 2026-11-22T05:12:19.367Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

On390x844 applied Year2024+Clinical Trial; filtered cards showed2024 trial metadata. Cleared both visible controls and repeated diabetes search;16 broad results restored, first PMID35771962 and second34238458. Controls and cards remained readable without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_two_filters_0.jpg; after.png: 09_mobile_restored_results_0.jpg

## Actions

### 2026-11-22T05:11:18.598Z — 01_mobile_filters_setup

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T05:11:25.051Z — 02_mobile_two_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:100,y:644}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:105,y:724}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:11:32.358Z — 03_mobile_apply_two

```javascript
await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:11:37.626Z — 04_mobile_active_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:11:43.972Z — 05_mobile_filtered_card

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:11:51.510Z — 06_mobile_clear_filters

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:100,y:644}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:105,y:724}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:12:00.870Z — 07_mobile_cleared_search

```javascript
await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:12:08.731Z — 08_mobile_cleared_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:12:17.282Z — 09_mobile_restored_results

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_two_filters_0.jpg](02_mobile_two_filters_0.jpg)
- [04_mobile_active_filters_0.jpg](04_mobile_active_filters_0.jpg)
- [05_mobile_filtered_card_0.jpg](05_mobile_filtered_card_0.jpg)
- [06_mobile_clear_filters_0.jpg](06_mobile_clear_filters_0.jpg)
- [08_mobile_cleared_controls_0.jpg](08_mobile_cleared_controls_0.jpg)
- [09_mobile_restored_results_0.jpg](09_mobile_restored_results_0.jpg)
