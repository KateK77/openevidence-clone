# ME3-CUA-0360: Filter saved publications by text

Status: **PASS**
Executed: 2026-11-22T21:47:00.381Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Fixture genuinely saved distinct papers via UI345/355/357. In current3-paper reading list, unique title substring smoking cessation yields only Electronic cigarettes for smoking cessation PMID39878158; unrelated ADA/Minnesota hidden.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_populated_distinct_titles_0.jpg; after.png: 03_title_filter_0.jpg

## Actions

### 2026-11-22T21:46:34.355Z — 01_populated_distinct_titles

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:46:42.005Z — 02_unfiltered_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:46:48.923Z — 03_title_filter

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.type({text:'smoking cessation'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_populated_distinct_titles_0.jpg](01_populated_distinct_titles_0.jpg)
- [02_unfiltered_baseline_0.jpg](02_unfiltered_baseline_0.jpg)
- [03_title_filter_0.jpg](03_title_filter_0.jpg)
