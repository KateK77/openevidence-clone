# ME3-CUA-0083: Short Chinese medical term normalization

Status: **BLOCKED**
Executed at: 2026-11-22T04:18:51.999Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 390x844

At mobile viewport entered 糖尿病 and activated Search PubMed. Chinese draft and 16-publication result list retained; full original/normalized/executed-query provenance not exposed by lookup workflow.

Research provenance workflow requires configured generation or separate verified no-charge/unconfigured instance; lookup results alone do not satisfy normalization audit. No generation initiated.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_0.jpg
- after.png from after_settled_0.jpg

## Action trace

### 2026-11-22T04:18:10.799Z — setup

```javascript
await sourceTab.close(); await tab.cua.keypress({keys:["CTRL","HOME"]}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:18:18.051Z — before

```javascript
await tab.cua.click({x:354,y:300}); await tab.cua.keypress({keys:["CTRL","HOME"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:18:27.805Z — submitted

```javascript
await tab.cua.click({x:155,y:487}); await tab.cua.keypress({keys:["CTRL","a"]}); await tab.cua.type({text:'糖尿病'}); await tab.cua.click({x:183,y:542}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:18:37.898Z — after

```javascript
await tab.cua.click({x:352,y:300}); await tab.cua.keypress({keys:["PAGEDOWN"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:18:49.937Z — after_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [after_settled_0.jpg](after_settled_0.jpg)
- [before_0.jpg](before_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submitted_0.jpg](submitted_0.jpg)
