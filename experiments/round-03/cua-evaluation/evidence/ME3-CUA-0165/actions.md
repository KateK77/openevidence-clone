# ME3-CUA-0165: Bounded long abstract handling

Status: **PASS**
Executed: 2026-11-22T06:02:50.443Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 reran PMID39878158 search, collapsed and expanded details, and scrolled through the structured long abstract to the final review-status sentence and PMID/save controls. Text stayed inside the card with no page-wide horizontal overflow or inaccessible tail. Source abstract label is explicit; no AI-review claim appears.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 07_collapsed_mobile_0.jpg; after.png: 12_mobile_long_text_4_0.jpg

## Actions

### 2026-11-22T06:01:04.936Z — 01_mobile_start

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T06:01:14.027Z — 02_mobile_query_form

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:01:22.218Z — 03_mobile_retrieve

```javascript
await activeTab.cua.click({x:185,y:563});
```
Tool error: False

### 2026-11-22T06:01:30.366Z — 04_mobile_result_scroll

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:360,y:800}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:01:38.431Z — 05_mobile_card

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:01:47.366Z — 06_mobile_collapse

```javascript
await activeTab.cua.click({x:167,y:335});
```
Tool error: False

### 2026-11-22T06:01:53.971Z — 07_collapsed_mobile

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:02:02.102Z — 08_expand_mobile

```javascript
await activeTab.cua.click({x:162,y:606}); await activeTab.cua.click({x:360,y:800}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:02:10.494Z — 09_mobile_long_text_1

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:02:20.890Z — 10_mobile_long_text_2

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:02:27.059Z — 11_mobile_long_text_3

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:02:35.344Z — 12_mobile_long_text_4

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

## Original captures

- [02_mobile_query_form_0.jpg](02_mobile_query_form_0.jpg)
- [04_mobile_result_scroll_0.jpg](04_mobile_result_scroll_0.jpg)
- [05_mobile_card_0.jpg](05_mobile_card_0.jpg)
- [07_collapsed_mobile_0.jpg](07_collapsed_mobile_0.jpg)
- [09_mobile_long_text_1_0.jpg](09_mobile_long_text_1_0.jpg)
- [10_mobile_long_text_2_0.jpg](10_mobile_long_text_2_0.jpg)
- [11_mobile_long_text_3_0.jpg](11_mobile_long_text_3_0.jpg)
- [12_mobile_long_text_4_0.jpg](12_mobile_long_text_4_0.jpg)
