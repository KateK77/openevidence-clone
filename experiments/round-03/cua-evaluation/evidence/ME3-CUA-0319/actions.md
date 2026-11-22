# ME3-CUA-0319: History search control

Status: **PASS**
Executed: 2026-11-22T07:32:52.708Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Desktop history search A150 leaves exactly the known matching owned thread title; entered term remains visible.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_search_before_0.jpg; after.png: 04_matching_title_0.jpg

## Actions

### 2026-11-22T07:32:10.418Z — 01_history_search

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/history');
```
Tool error: False

### 2026-11-22T07:32:20.914Z — 02_search_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:32:35.350Z — 03_search_fragment

```javascript
await activeTab.cua.click({x:603,y:364}); await activeTab.cua.type({text:'A150'}); await activeTab.cua.click({x:1212,y:361});
```
Tool error: False

### 2026-11-22T07:32:43.078Z — 04_matching_title

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_search_before_0.jpg](02_search_before_0.jpg)
- [04_matching_title_0.jpg](04_matching_title_0.jpg)
