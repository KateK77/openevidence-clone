# ME3-CUA-0122: Query changes reset stale publications

Status: **PASS**
Executed: 2026-11-22T05:13:00.465Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Replaced diabetes with asthma and submitted. Captured searching transition explicitly clearing old cards and showing 'Searching literature... / Loading publications...'; completed list showed16 asthma records, starting Asthma: definitions and pathophysiology. Old diabetes cards were not retained under an in-flight submitted query.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_replace_query_0.jpg; after.png: 05_asthma_titles_0.jpg

## Actions

### 2026-11-22T05:12:19.619Z — 01_query_switch_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:12:30.633Z — 02_replace_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'asthma'});
```
Tool error: False

### 2026-11-22T05:12:38.419Z — 03_new_query_submit_transition

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1210,y:488}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:12:48.786Z — 04_new_query_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:12:57.764Z — 05_asthma_titles

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_replace_query_0.jpg](02_replace_query_0.jpg)
- [03_new_query_submit_transition_0.jpg](03_new_query_submit_transition_0.jpg)
- [03_new_query_submit_transition_1.jpg](03_new_query_submit_transition_1.jpg)
- [04_new_query_results_0.jpg](04_new_query_results_0.jpg)
- [05_asthma_titles_0.jpg](05_asthma_titles_0.jpg)
