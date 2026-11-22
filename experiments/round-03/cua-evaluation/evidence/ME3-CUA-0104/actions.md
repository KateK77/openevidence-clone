# ME3-CUA-0104: Result title and journal

Status: **PASS**
Executed: 2026-11-22T04:41:55.234Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile keyword search diabetes: opened first publication after explicitly collapsing/reopening. Full title wraps readably; journal The Journal of clinical endocrinology and metabolism wraps within card;2022 card year matches2022 Sep28 detail. Authors, DOI and abstract visible without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:40:52.704Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:40:58.446Z — top

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:10.183Z — before

```javascript
await tab.cua.click({x:172,y:506}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'diabetes'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:21.158Z — submit

```javascript
await tab.cua.click({x:180,y:563}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:28.126Z — scroll

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:36.033Z — ready

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:43.384Z — collapsed

```javascript
await tab.cua.click({x:160,y:335}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:41:52.431Z — after

```javascript
await tab.cua.click({x:160,y:335}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [collapsed_0.jpg](collapsed_0.jpg)
- [ready_0.jpg](ready_0.jpg)
- [scroll_0.jpg](scroll_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
- [top_0.jpg](top_0.jpg)
