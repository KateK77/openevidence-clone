# ME3-CUA-0098: Keyword PubMed search

Status: **PASS**
Executed: 2026-11-22T04:35:39.760Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Searched diabetes in live literature UI:16 publications. Visible records include Diagnosis and Management of Central Diabetes Insipidus in Adults (2022, PMID35771962), Nephrogenic diabetes insipidus: a comprehensive overview (2022, PMID35146976), and Diabetes or endocrinopathy admitted in the COVID-19 ward (2020, PMID32383239), each with source link. Results differ meaningfully from prior GLP-1 query.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:34:56.285Z — open_library

```javascript
await tab.cua.click({x:105,y:415}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:03.269Z — before

```javascript
await tab.cua.click({x:610,y:488}); await tab.cua.type({text:'diabetes'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:13.199Z — submit

```javascript
await tab.cua.click({x:1243,y:486}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:22.206Z — results

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:28.973Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [open_library_0.jpg](open_library_0.jpg)
- [results_0.jpg](results_0.jpg)
- [submit_0.jpg](submit_0.jpg)
