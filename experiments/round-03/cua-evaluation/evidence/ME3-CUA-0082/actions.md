# ME3-CUA-0082: Short Chinese medical term normalization

Status: **BLOCKED**
Executed at: 2026-11-22T04:18:10.559Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Submitted 糖尿病 on Search PubMed; 16 relevant publications returned, original Chinese input retained. Opened first PMID 15137354 and visually matched title and PMID on official PubMed. The lookup page exposes no separate original/normalized/executed-query provenance fields.

Full normalization audit requires research outcome/provenance flow; configured synthesis may incur unverified provider charges. Literature lookup alone is insufficient for this criterion; no PASS inferred.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from query_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:16:59.081Z — before

```javascript
await tab.cua.click({x:117,y:417}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:07.233Z — query

```javascript
await tab.cua.click({x:633,y:486}); await tab.cua.type({text:'糖尿病'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:16.515Z — searching

```javascript
await tab.cua.click({x:1241,y:488}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:24.020Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:31.789Z — source_card

```javascript
await tab.cua.click({x:1393,y:703}); await tab.cua.keypress({keys:["PAGEDOWN"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:39.471Z — source_card_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:17:48.615Z — source_open

```javascript
await tab.cua.click({x:371,y:186}); await nodeRepl.write(await browser.tabs.list());
```
Tool error: False

[{"id":"432238160","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238160\"]","url":"https://medevidence-ai-v3.onrender.com/library","title":"MedEvidence AI 3.0"},{"id":"432238161","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238161\"]","url":"https://pubmed.ncbi.nlm.nih.gov/15137354/","title":"pubmed.ncbi.nlm.nih.gov"}]
### 2026-11-22T04:17:55.853Z — official_source

```javascript
const sourceTab=await browser.tabs.get('432238161'); await nodeRepl.write(await sourceTab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [official_source_0.jpg](official_source_0.jpg)
- [query_0.jpg](query_0.jpg)
- [searching_0.jpg](searching_0.jpg)
- [source_card_0.jpg](source_card_0.jpg)
- [source_card_settled_0.jpg](source_card_settled_0.jpg)
