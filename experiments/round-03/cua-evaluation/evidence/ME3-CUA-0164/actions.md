# ME3-CUA-0164: Bounded long abstract handling

Status: **PASS**
Executed: 2026-11-22T06:01:04.694Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Retrieved real PMID39878158 in Search PubMed, expanded its structured long source abstract and navigated to all sections through Authors conclusions and final review-status sentence. Desktop text wraps within card; footer PMID/save controls remain reachable. Labels say Source abstract, with no assertion that AI reviewed it. Official PubMed identity and abstract were separately inspected; this is source-text UI coverage, not AI truncation/generation validation.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 11_collapsed_card_0.jpg; after.png: 14_long_abstract_tail_0.jpg

## Actions

### 2026-11-22T05:58:04.415Z — 01_prepare_official_long_abstract

```javascript
let longSource = await browser.tabs.new(); await longSource.goto('https://pubmed.ncbi.nlm.nih.gov/39878158/');
```
Tool error: False

### 2026-11-22T05:58:18.625Z — 02_official_source_before

```javascript
await nodeRepl.write(await longSource.screenshot({}));
```
Tool error: False

### 2026-11-22T05:58:26.286Z — 03_official_source_scroll

```javascript
await viewport.set({width:1440,height:900}); await longSource.cua.click({x:1200,y:450}); await longSource.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:58:32.126Z — 04_official_identity

```javascript
await nodeRepl.write(await longSource.screenshot({}));
```
Tool error: False

### 2026-11-22T05:58:41.674Z — 05_official_long_abstract_part2

```javascript
await longSource.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:58:48.603Z — 06_official_abstract_tail

```javascript
await nodeRepl.write(await longSource.screenshot({})); await longSource.close();
```
Tool error: False

### 2026-11-22T05:59:03.900Z — 07_open_library

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.click({x:104,y:416});
```
Tool error: False

### 2026-11-22T05:59:19.328Z — 08_library_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:59:26.629Z — 09_retrieve_long_abstract

```javascript
await activeTab.cua.click({x:640,y:487}); await activeTab.cua.type({text:'39878158'}); await activeTab.cua.click({x:1220,y:487});
```
Tool error: False

### 2026-11-22T05:59:35.389Z — 10_result_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1390,y:770}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:59:44.854Z — 11_collapsed_card

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:430,y:685});
```
Tool error: False

### 2026-11-22T05:59:54.985Z — 12_opened_and_scroll

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1390,y:770}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:00:03.708Z — 13_long_abstract_upper

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:00:14.742Z — 14_long_abstract_tail

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:00:30.432Z — 15_open_official_tail_check

```javascript
await activeTab.cua.click({x:370,y:754}); await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238168","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238168\"]","url":"https://medevidence-ai-v3.onrender.com/library","title":"MedEvidence AI 3.0"},{"id":"432238185","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238185\"]","url":"","title":""}]

### 2026-11-22T06:00:41.137Z — 16_source_find_tail

```javascript
longSource = await browser.tabs.get('432238185'); await longSource.cua.keypress({keys:['CTRL','f']}); await longSource.cua.type({text:'Please refer to the Cochrane'}); await longSource.cua.keypress({keys:['ESC']});
```
Tool error: False

### 2026-11-22T06:00:47.368Z — 17_official_tail_matches

```javascript
await nodeRepl.write(await longSource.screenshot({})); await nodeRepl.write(await longSource.url()); await longSource.close();
```
Tool error: False
https://pubmed.ncbi.nlm.nih.gov/39878158/

### 2026-11-22T06:01:00.426Z — 18_returned_app_long_tail

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_official_source_before_0.jpg](02_official_source_before_0.jpg)
- [04_official_identity_0.jpg](04_official_identity_0.jpg)
- [06_official_abstract_tail_0.jpg](06_official_abstract_tail_0.jpg)
- [08_library_before_0.jpg](08_library_before_0.jpg)
- [10_result_before_0.jpg](10_result_before_0.jpg)
- [11_collapsed_card_0.jpg](11_collapsed_card_0.jpg)
- [12_opened_and_scroll_0.jpg](12_opened_and_scroll_0.jpg)
- [13_long_abstract_upper_0.jpg](13_long_abstract_upper_0.jpg)
- [14_long_abstract_tail_0.jpg](14_long_abstract_tail_0.jpg)
- [17_official_tail_matches_0.jpg](17_official_tail_matches_0.jpg)
- [18_returned_app_long_tail_0.jpg](18_returned_app_long_tail_0.jpg)
