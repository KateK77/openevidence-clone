# ME3-CUA-0110: Publication year start filter

Status: **PASS**
Executed: 2026-11-22T04:50:44.582Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Set year2024 for diabetes and applied search. Inspected all16 returned cards across screenshots:15 display2024 and PMID39845881 displays2025; none earlier than2024. Returned to top and verified filter2024 remains visible. Manually transcribed all PMIDs/years in observed_years.json. Full-page screenshot timed out and returned a downscaled preview later; year verdict uses readable viewport captures only.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: year_verified_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:47:22.009Z — before

```javascript
await tab.cua.click({x:429,y:573}); await tab.cua.type({text:'2024'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:47:32.672Z — year_verified

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:47:44.250Z — apply

```javascript
await tab.cua.click({x:1209,y:484}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:47:51.967Z — result

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:48:08.679Z — all_results

```javascript
await nodeRepl.write(await tab.screenshot({fullPage:true}));
```
Tool error: True
Error: Timed out after 5000ms waiting for CDP command Page.captureScreenshot.

### 2026-11-22T04:48:22.062Z — page1_scroll

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:48:32.955Z — page1

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:48:42.440Z — scroll2

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:48:49.145Z — page2

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:48:57.446Z — scroll3

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:06.756Z — page3

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:14.391Z — scroll4

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:21.506Z — page4

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:32.156Z — scroll5

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:39.691Z — page5

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:48.899Z — scroll6

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:49:58.115Z — page6

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:50:05.863Z — scroll7

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:50:14.805Z — page7

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:50:29.610Z — return_filters

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:50:41.878Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [apply_0.jpg](apply_0.jpg)
- [before_0.jpg](before_0.jpg)
- [page1_0.jpg](page1_0.jpg)
- [page1_scroll_0.jpg](page1_scroll_0.jpg)
- [page2_0.jpg](page2_0.jpg)
- [page3_0.jpg](page3_0.jpg)
- [page4_0.jpg](page4_0.jpg)
- [page5_0.jpg](page5_0.jpg)
- [page6_0.jpg](page6_0.jpg)
- [page7_0.jpg](page7_0.jpg)
- [result_0.jpg](result_0.jpg)
- [return_filters_0.jpg](return_filters_0.jpg)
- [scroll2_0.jpg](scroll2_0.jpg)
- [scroll3_0.jpg](scroll3_0.jpg)
- [scroll4_0.jpg](scroll4_0.jpg)
- [scroll5_0.jpg](scroll5_0.jpg)
- [scroll6_0.jpg](scroll6_0.jpg)
- [scroll7_0.jpg](scroll7_0.jpg)
- [year_verified_0.jpg](year_verified_0.jpg)
