# ME3-CUA-0294: Executed query provenance visible

Status: **PASS**
Executed: 2026-11-22T07:15:11.642Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Successfully retrieved real PMID32356626 answer shows actual executed queries32356626(1PMID) and quoted32356626(0PMIDs), separately from Original question and normalized-before-context fields.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_desktop_queries_0.jpg; after.png: 01_desktop_queries_0.jpg

## Actions

### 2026-11-22T07:15:02.500Z — 01_desktop_queries

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_queries_0.jpg](01_desktop_queries_0.jpg)
