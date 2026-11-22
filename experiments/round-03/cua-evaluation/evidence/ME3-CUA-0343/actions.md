# ME3-CUA-0343: Saved answers and publications separate

Status: **PASS**
Executed: 2026-11-22T21:31:46.297Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Sidebar destinations have distinct Saved answers versus Saved publications headings and response rows versus publication cards. After independently saving PMID33551565 in339, Saved answers remains exact baseline three answers20/18/16, with no automatic answer bookmark; publication page shows one PMID33551565.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_answers_page_0.jpg; after.png: 02_publications_separate_0.jpg

## Actions

### 2026-11-22T21:31:28.510Z — 01_answers_page

```javascript
await historyOther.close(); await activeTab.cua.click({x:100,y:330}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:31:36.712Z — 02_publications_separate

```javascript
await activeTab.cua.click({x:110,y:465}); await nodeRepl.write(await activeTab.url()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
https://medevidence-ai-v3.onrender.com/publications

## Original captures

- [01_answers_page_0.jpg](01_answers_page_0.jpg)
- [02_publications_separate_0.jpg](02_publications_separate_0.jpg)
