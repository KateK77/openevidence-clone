# ME3-CUA-0292: Original-question provenance visible

Status: **PASS**
Executed: 2026-11-22T07:14:38.085Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Answer18 expanded Retrieval provenance labels Original question and exactly retains submitted 32356626, separately from normalized text and executed searches.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_details_0.jpg; after.png: 06_exact_original_0.jpg

## Actions

### 2026-11-22T07:13:33.572Z — 01_answer_open

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:13:44.647Z — 02_details

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:13:55.257Z — 03_provenance_control

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:14:07.126Z — 04_page_end

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:14:15.808Z — 05_expand_provenance

```javascript
await activeTab.cua.click({x:414,y:778}); await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:14:27.587Z — 06_exact_original

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_answer_open_0.jpg](01_answer_open_0.jpg)
- [02_details_0.jpg](02_details_0.jpg)
- [03_provenance_control_0.jpg](03_provenance_control_0.jpg)
- [04_page_end_0.jpg](04_page_end_0.jpg)
- [05_expand_provenance_0.jpg](05_expand_provenance_0.jpg)
- [06_exact_original_0.jpg](06_exact_original_0.jpg)
