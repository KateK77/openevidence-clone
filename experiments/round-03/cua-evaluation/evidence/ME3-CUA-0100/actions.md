# ME3-CUA-0100: Known PMID direct lookup

Status: **PASS**
Executed: 2026-11-22T04:38:04.303Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Entered known PMID15137354 and searched: exactly1 publication, matching Pathophysiology of diabetes mellitus, Critical care nursing quarterly,2004. Expanded actual details show Richard A Guthrie/Diana W Guthrie, DOI10.1097/00002727-200404000-00003, abstract and matching PMID source link.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: input_verified_0.jpg; after.png: after_settled_0.jpg

## Actions

### 2026-11-22T04:36:36.783Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:36:45.721Z — top

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:36:56.319Z — before

```javascript
await tab.cua.click({x:613,y:483}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'15137354'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:06.346Z — input_verified

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:12.407Z — submit

```javascript
await tab.cua.click({x:1206,y:483}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:19.938Z — result

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:27.922Z — scroll_detail

```javascript
await tab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:35.126Z — bottom_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:41.788Z — open_details

```javascript
await tab.cua.click({x:421,y:679}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:49.032Z — after

```javascript
await tab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:37:55.388Z — after_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [after_settled_0.jpg](after_settled_0.jpg)
- [before_0.jpg](before_0.jpg)
- [bottom_settled_0.jpg](bottom_settled_0.jpg)
- [input_verified_0.jpg](input_verified_0.jpg)
- [open_details_0.jpg](open_details_0.jpg)
- [result_0.jpg](result_0.jpg)
- [scroll_detail_0.jpg](scroll_detail_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
- [top_0.jpg](top_0.jpg)
