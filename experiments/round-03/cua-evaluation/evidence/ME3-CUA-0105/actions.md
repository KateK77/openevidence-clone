# ME3-CUA-0105: Authors exposed

Status: **PASS**
Executed: 2026-11-22T04:42:40.279Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Opened publication details for PMID35771962. Five authors displayed: Maria Tomkins, Sarah Lawless, Julie Martin-Grace, Mark Sherlock, Chris J Thompson. Opened official PubMed source and visually matched all five author names and PMID.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: official_authors_0.jpg

## Actions

### 2026-11-22T04:41:55.471Z — setup

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:42:05.512Z — before

```javascript
await tab.cua.click({x:432,y:160}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:42:12.906Z — after

```javascript
await tab.cua.click({x:430,y:160}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:42:20.354Z — verify_source

```javascript
await tab.cua.click({x:365,y:563}); await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238160","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238160\"]","url":"https://medevidence-ai-v3.onrender.com/library","title":"MedEvidence AI 3.0"},{"id":"432238163","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238163\"]","url":"https://pubmed.ncbi.nlm.nih.gov/35771962/","title":"pubmed.ncbi.nlm.nih.gov"}]

### 2026-11-22T04:42:26.641Z — official_authors

```javascript
const authorTab = await browser.tabs.get('432238163'); await nodeRepl.write(await authorTab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [official_authors_0.jpg](official_authors_0.jpg)
- [setup_0.jpg](setup_0.jpg)
