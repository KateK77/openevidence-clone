# ME3-CUA-0295: Executed query provenance visible

Status: **PASS**
Executed: 2026-11-22T07:15:55.041Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

390px provenance distinguishes original/normalized/prior-question fields from actual executed32356626 and quoted32356626 queries with1/0PMID counts; wrapped explanation and counts readable, no page-wide overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_queries_0.jpg; after.png: 02_executed_queries_0.jpg

## Actions

### 2026-11-22T07:15:11.884Z — 01_mobile_queries

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:15:17.699Z — 02_executed_queries

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_queries_0.jpg](01_mobile_queries_0.jpg)
- [02_executed_queries_0.jpg](02_executed_queries_0.jpg)
