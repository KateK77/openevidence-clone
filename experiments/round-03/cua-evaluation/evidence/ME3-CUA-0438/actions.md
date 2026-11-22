# ME3-CUA-0438: Mobile publication detail readability

Status: **PASS**
Executed: 2026-11-22T22:28:33.328Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px saved PMID6373426 long abstract wraps fully with vertical scrolling; official PMID link opens correct PubMed article; closing source tab returns to intact saved results.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_saved_publications_0.jpg; after.png: 07_return_results_0.jpg

## Actions

### 2026-11-22T22:27:42.179Z — 01_saved_publications

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/publications'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:45.513Z — 02_saved_list

```javascript
await activeTab.cua.scroll({x:200,y:680,scrollY:525,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:54.261Z — 03_expand_long_abstract

```javascript
await activeTab.cua.click({x:166,y:266}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:58.014Z — 04_abstract_scroll

```javascript
await activeTab.cua.scroll({x:209,y:680,scrollY:554,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:06.968Z — 05_open_official_source

```javascript
await activeTab.cua.click({x:85,y:468}); await nodeRepl.write(await browser.tabs.list()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
[{"id":"432238168","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238168\"]","url":"https://medevidence-ai-v3.onrender.com/publications","title":"MedEvidence AI 3.0"},{"id":"432238192","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238192\"]","url":"https://pubmed.ncbi.nlm.nih.gov/6373426/","title":"pubmed.ncbi.nlm.nih.gov"}]

### 2026-11-22T22:28:13.680Z — 06_official_pubmed

```javascript
var source438 = await browser.tabs.get('432238192'); await nodeRepl.write(await source438.screenshot({}));
```
Tool error: False

### 2026-11-22T22:28:30.503Z — 07_return_results

```javascript
await source438.close(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_saved_publications_0.jpg](01_saved_publications_0.jpg)
- [02_saved_list_0.jpg](02_saved_list_0.jpg)
- [03_expand_long_abstract_0.jpg](03_expand_long_abstract_0.jpg)
- [04_abstract_scroll_0.jpg](04_abstract_scroll_0.jpg)
- [05_open_official_source_0.jpg](05_open_official_source_0.jpg)
- [06_official_pubmed_0.jpg](06_official_pubmed_0.jpg)
- [07_return_results_0.jpg](07_return_results_0.jpg)
