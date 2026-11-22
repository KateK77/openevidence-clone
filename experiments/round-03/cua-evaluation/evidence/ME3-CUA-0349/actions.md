# ME3-CUA-0349: Saved publications list has search/filter

Status: **PASS**
Executed: 2026-11-22T21:36:25.698Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Populated reading list has3 genuine bookmarked publications. Visible filter supports title/author/PMID/collection. Typing39878158 instantly reduces visible list to exact Electronic cigarettes for smoking cessation PMID39878158; no submit/refresh needed.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_populated_publications_0.jpg; after.png: 02_filter_by_pmid_0.jpg

## Actions

### 2026-11-22T21:36:07.266Z — 01_populated_publications

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/publications'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:36:14.539Z — 02_filter_by_pmid

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.type({text:'39878158'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_populated_publications_0.jpg](01_populated_publications_0.jpg)
- [02_filter_by_pmid_0.jpg](02_filter_by_pmid_0.jpg)
