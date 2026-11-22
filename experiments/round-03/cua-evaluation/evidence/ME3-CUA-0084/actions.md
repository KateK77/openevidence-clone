# ME3-CUA-0084: Chinese query with whitespace trimming

Status: **BLOCKED**
Executed at: 2026-11-22T04:21:15.796Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Partial CUA: submitted '   糖尿病   ' through the real literature search; 16 diabetes publications remain visible. Search UI exposes no original/normalized executed-query provenance. Full research submission was not performed.

Normalized-query and original-question assertions require research generation; configured provider fee authorization unavailable. Literature lookup alone does not satisfy full scenario.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from input_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:18:52.235Z — setup

```javascript
await viewport.set({width:1440,height:900}); await tab.cua.keypress({keys:["CTRL","HOME"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:20:42.909Z — before_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:20:55.458Z — input

```javascript
await tab.cua.click({x:525,y:483}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'   糖尿病   '}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:03.904Z — submit

```javascript
await tab.cua.click({x:1203,y:483}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:13.505Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_settled_0.jpg](before_settled_0.jpg)
- [input_0.jpg](input_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
