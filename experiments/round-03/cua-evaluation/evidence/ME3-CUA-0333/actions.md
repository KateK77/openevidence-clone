# ME3-CUA-0333: Deletion does not remove other threads

Status: **PASS**
Executed: 2026-11-22T21:20:53.506Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Created disposable thread20 CUA333 alongside existing source-backed thread17; confirmed deletion of20. Opened surviving17 fromHistory: sameCUA323 title,33551565 question,Chinese no-abstract response,1record. Exact answer19 still contains PMID33551565 ADA Standards title/card, unchanged from established fixture.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_surviving_thread_before_0.jpg; after.png: 15_same_source_retained_0.jpg

## Actions

### 2026-11-22T21:18:42.516Z — 01_survivor_baseline

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/17');
```
Tool error: False

### 2026-11-22T21:18:50.208Z — 02_surviving_thread_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:18:58.001Z — 03_prepare_second_disposable

```javascript
await activeTab.cua.click({x:117,y:137});
```
Tool error: False

### 2026-11-22T21:19:03.370Z — 04_preparation_input

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:19:11.882Z — 05_disposable_draft

```javascript
await activeTab.cua.click({x:682,y:646}); await activeTab.cua.type({text:'脊髓空洞症 CUA333 disposable isolation'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:19:21.734Z — 06_prepare_create

```javascript
await activeTab.cua.click({x:1190,y:756});
```
Tool error: False

### 2026-11-22T21:19:32.569Z — 07_scored_disposable_before

```javascript
await nodeRepl.write(await activeTab.url()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/20

### 2026-11-22T21:19:44.173Z — 08_confirmation

```javascript
await activeTab.cua.click({x:460,y:361}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:19:55.132Z — 09_confirm_isolated_test_delete

```javascript
await activeTab.cua.click({x:791,y:442});
```
Tool error: False

### 2026-11-22T21:20:03.643Z — 10_survivor_history

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:20:13.019Z — 11_open_surviving_conversation

```javascript
await activeTab.cua.click({x:504,y:430});
```
Tool error: False

### 2026-11-22T21:20:22.150Z — 12_survivor_unchanged

```javascript
await nodeRepl.write(await activeTab.url()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/17

### 2026-11-22T21:20:29.721Z — 13_surviving_evidence_link

```javascript
await activeTab.cua.click({x:393,y:614});
```
Tool error: False

### 2026-11-22T21:20:36.196Z — 14_surviving_evidence_scroll

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/19

### 2026-11-22T21:20:42.618Z — 15_same_source_retained

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_surviving_thread_before_0.jpg](02_surviving_thread_before_0.jpg)
- [04_preparation_input_0.jpg](04_preparation_input_0.jpg)
- [05_disposable_draft_0.jpg](05_disposable_draft_0.jpg)
- [07_scored_disposable_before_0.jpg](07_scored_disposable_before_0.jpg)
- [08_confirmation_0.jpg](08_confirmation_0.jpg)
- [10_survivor_history_0.jpg](10_survivor_history_0.jpg)
- [12_survivor_unchanged_0.jpg](12_survivor_unchanged_0.jpg)
- [15_same_source_retained_0.jpg](15_same_source_retained_0.jpg)
