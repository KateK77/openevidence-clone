# ME3-CUA-0106: PMID links open source

Status: **PASS**
Executed: 2026-11-22T04:43:10.441Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Activated source link PMID35771962 from expanded publication. Opened tab URL https://pubmed.ncbi.nlm.nih.gov/35771962/; visible official PubMed title and PMID match application card.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:42:40.518Z — before

```javascript
await authorTab.close(); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:42:56.498Z — activate_link

```javascript
await tab.cua.click({x:366,y:565}); await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238160","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238160\"]","url":"https://medevidence-ai-v3.onrender.com/library","title":"MedEvidence AI 3.0"},{"id":"432238165","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238165\"]","url":"https://pubmed.ncbi.nlm.nih.gov/35771962/","title":"Diagnosis and Management of Central Diabetes Insipidus in Adults - PubMed"}]

### 2026-11-22T04:43:07.022Z — after

```javascript
const linkTab = await browser.tabs.get('432238165'); await nodeRepl.write(await linkTab.url()); await nodeRepl.write(await linkTab.screenshot({}));
```
Tool error: False
https://pubmed.ncbi.nlm.nih.gov/35771962/

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
