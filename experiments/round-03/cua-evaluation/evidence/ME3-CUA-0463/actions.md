# ME3-CUA-0463: Public PubMed source retrieval

Status: **PASS**
Executed: 2026-11-22T22:49:24.783Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public app search for PMID33551565 returned one live publication, ADA's Standards of Medical Care in Diabetes, with metadata and honest no-abstract notice. Expanded details and opened official PubMed; matching title, PMID33551565 and DOI10.2337/cd21-pe01 visibly verified.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_search_ready_0.jpg; after.png: 08_official_verified_0.jpg

## Actions

### 2026-11-22T22:48:14.582Z — 01_pubmed

```javascript
await activeTab.cua.click({x:105,y:418});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:17.690Z — 02_search_ready

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:28.215Z — 03_query

```javascript
await activeTab.cua.click({x:692,y:481});await activeTab.cua.type({text:'33551565'});await activeTab.cua.click({x:1238,y:481});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:32.231Z — 04_result

```javascript
await activeTab.cua.scroll({x:1320,y:758,scrollY:486,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:45.847Z — 05_publication_details

```javascript
await activeTab.cua.click({x:451,y:700});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:48.979Z — 06_detail_scroll

```javascript
await activeTab.cua.scroll({x:1310,y:745,scrollY:390,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:48:59.603Z — 07_official_link

```javascript
await activeTab.cua.click({x:365,y:775});await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238168","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238168\"]","url":"https://medevidence-ai-v3.onrender.com/library","title":"MedEvidence AI 3.0"},{"id":"432238194","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238194\"]","url":"https://pubmed.ncbi.nlm.nih.gov/33551565/","title":"pubmed.ncbi.nlm.nih.gov"}]

### 2026-11-22T22:49:08.190Z — 08_official_verified

```javascript
let source463=await browser.tabs.get('432238194');await nodeRepl.write(await source463.screenshot({}));await nodeRepl.write(await source463.url());
```
Tool error: False
https://pubmed.ncbi.nlm.nih.gov/33551565/

## Original captures

- [01_pubmed_0.jpg](01_pubmed_0.jpg)
- [02_search_ready_0.jpg](02_search_ready_0.jpg)
- [03_query_0.jpg](03_query_0.jpg)
- [04_result_0.jpg](04_result_0.jpg)
- [05_publication_details_0.jpg](05_publication_details_0.jpg)
- [06_detail_scroll_0.jpg](06_detail_scroll_0.jpg)
- [08_official_verified_0.jpg](08_official_verified_0.jpg)
