# ME3-CUA-0350: Saved publications list has search/filter

Status: **PASS**
Executed: 2026-11-22T21:36:59.577Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 populated reading-list filter accepts33551565 and displays only exact ADA's Standards of Medical Care in Diabetes PMID33551565 with Saved state. Field/title/actions wrap within viewport, vertical scroll works. Capture01 transitional desktop scaling excluded; settled02/04 govern.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_settled_baseline_0.jpg; after.png: 04_mobile_filter_result_0.jpg

## Actions

### 2026-11-22T21:36:25.936Z — 01_mobile_populated_list

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:36:34.330Z — 02_mobile_settled_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:36:40.734Z — 03_mobile_filter

```javascript
await activeTab.cua.click({x:155,y:448}); await activeTab.cua.type({text:'33551565'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:36:48.236Z — 04_mobile_filter_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_populated_list_0.jpg](01_mobile_populated_list_0.jpg)
- [02_mobile_settled_baseline_0.jpg](02_mobile_settled_baseline_0.jpg)
- [03_mobile_filter_0.jpg](03_mobile_filter_0.jpg)
- [04_mobile_filter_result_0.jpg](04_mobile_filter_result_0.jpg)
