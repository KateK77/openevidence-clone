# ME3-CUA-0109: Relevance sorting control

Status: **PASS**
Executed: 2026-11-22T04:47:21.776Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Switched diabetes from Publication date to Relevance and applied search. Loading observed, then16 results. Relevance visibly retained; first publication changed from Skeletal phenotype... (PMID43062408) to Diagnosis and Management of Central Diabetes Insipidus in Adults (PMID35771962), matching original relevance result.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:46:36.943Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:52.085Z — before

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:46:59.791Z — relevance_selected

```javascript
await tab.cua.click({x:1208,y:573}); await tab.cua.keypress({keys:['ARROWUP']}); await tab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:47:09.583Z — apply

```javascript
await tab.cua.click({x:1206,y:484}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:47:19.054Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [apply_0.jpg](apply_0.jpg)
- [before_0.jpg](before_0.jpg)
- [relevance_selected_0.jpg](relevance_selected_0.jpg)
- [setup_0.jpg](setup_0.jpg)
