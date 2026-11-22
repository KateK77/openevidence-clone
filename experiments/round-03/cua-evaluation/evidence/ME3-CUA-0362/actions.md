# ME3-CUA-0362: Clear saved-publication filter

Status: **PASS**
Executed: 2026-11-22T21:48:11.560Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Applied Minnesota restrictive filter showing only6373426. Cleared text without submit/reload: previously hidden ADA33551565 and Electronic cigarettes39878158 cards reappear immediately while Minnesota remains.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_desktop_filter_preparation_0.jpg; after.png: 05_clear_filter_0.jpg

## Actions

### 2026-11-22T21:47:24.055Z — 01_desktop_filter_preparation

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:47:31.995Z — 02_desktop_ready

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:47:41.293Z — 03_restrictive_filter

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'Minnesota'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:47:51.909Z — 04_restrictive_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:48:00.097Z — 05_clear_filter

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.scroll({x:1050,y:722,scrollY:600,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_filter_preparation_0.jpg](01_desktop_filter_preparation_0.jpg)
- [02_desktop_ready_0.jpg](02_desktop_ready_0.jpg)
- [03_restrictive_filter_0.jpg](03_restrictive_filter_0.jpg)
- [04_restrictive_result_0.jpg](04_restrictive_result_0.jpg)
- [05_clear_filter_0.jpg](05_clear_filter_0.jpg)
