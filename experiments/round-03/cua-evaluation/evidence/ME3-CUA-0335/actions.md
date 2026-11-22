# ME3-CUA-0335: Search clearing restores history

Status: **PASS**
Executed: 2026-11-22T21:24:35.970Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

CUA323 filtered the 12 owned conversations to the exact CUA323 mobile 33551565 row. Clearing the input and submitting Search restored all 12 baseline rows, including both Nov 20 entries, without browser refresh.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_filter_0.jpg; after.png: 06_full_list_restored_0.jpg

## Actions

### 2026-11-22T21:20:56.610Z — 01_history

```javascript
await activeTab.cua.click({x:109,y:284});
```
Tool error: False

### 2026-11-22T21:21:13.119Z — 02_full_history_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:23:55.327Z — 03_resumed_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:24:05.149Z — 04_filter

```javascript
await activeTab.cua.click({x:620,y:123}); await activeTab.cua.type({text:'CUA323'}); await activeTab.cua.click({x:1210,y:123}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:24:17.120Z — 05_clear_search

```javascript
await activeTab.cua.click({x:620,y:363}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.click({x:1227,y:362}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:24:26.541Z — 06_full_list_restored

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_full_history_baseline_0.jpg](02_full_history_baseline_0.jpg)
- [03_resumed_baseline_0.jpg](03_resumed_baseline_0.jpg)
- [04_filter_0.jpg](04_filter_0.jpg)
- [05_clear_search_0.jpg](05_clear_search_0.jpg)
- [06_full_list_restored_0.jpg](06_full_list_restored_0.jpg)
