# ME3-CUA-0101: Known PMID direct lookup

Status: **PASS**
Executed: 2026-11-22T04:39:09.457Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile entered PMID15137354, submitted search and obtained1 matching publication. Collapsed/reopened its details via pointer. Title and2004 journal metadata matched fixture; long abstract and DOI wrapped legibly, PMID15137354 source link accessible at bottom without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: open_details_0.jpg

## Actions

### 2026-11-22T04:38:04.552Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:14.952Z — top

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:21.615Z — before

```javascript
await tab.cua.click({x:174,y:508}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'15137354'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:28.843Z — submit

```javascript
await tab.cua.click({x:184,y:563}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:36.867Z — details_scroll

```javascript
await tab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:44.036Z — details_ready

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:50.764Z — collapse

```javascript
await tab.cua.click({x:152,y:29}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:38:57.480Z — open_details

```javascript
await tab.cua.click({x:159,y:606}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [before_0.jpg](before_0.jpg)
- [collapse_0.jpg](collapse_0.jpg)
- [details_ready_0.jpg](details_ready_0.jpg)
- [details_scroll_0.jpg](details_scroll_0.jpg)
- [open_details_0.jpg](open_details_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
- [top_0.jpg](top_0.jpg)
