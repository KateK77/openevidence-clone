# ME3-CUA-0081: Draft recovery after validation

Status: **PASS**
Executed at: 2026-11-22T04:16:58.805Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Entered 2,002-character multiline draft; submit rejected with explicit length error. Removed only final X and newline using keyboard; clipboard copy verified remaining 2,000 characters exactly equal original draft, so unrelated text unchanged. Second submission succeeded to a saved research conversation. This validates input recovery, not AI synthesis.



## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_settled_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:15:15.381Z — setup

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:15:22.907Z — desktop_ready

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:15:35.521Z — before

```javascript
await tab.cua.click({x:631,y:675}); await tab.cua.keypress({keys:["CTRL","a"]}); await tab.clipboard.writeText(q2000+'\nX'); await tab.cua.keypress({keys:["CTRL","v"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:15:50.925Z — before_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:15:57.268Z — reject_attempt

```javascript
await tab.cua.click({x:1178,y:771}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:16:06.994Z — rejected

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:16:15.172Z — corrected

```javascript
await tab.cua.click({x:721,y:684}); await tab.cua.keypress({keys:["CTRL","END"]}); await tab.cua.keypress({keys:["BACKSPACE"]}); await tab.cua.keypress({keys:["BACKSPACE"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:16:25.639Z — corrected_verified

```javascript
await tab.cua.keypress({keys:["CTRL","a"]}); await tab.cua.keypress({keys:["CTRL","c"]}); const correctedDraft=await tab.clipboard.readText(); await nodeRepl.write({length:correctedDraft.length,equalsOriginal2000:correctedDraft===q2000}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

{"length":2000,"equalsOriginal2000":true}
### 2026-11-22T04:16:33.415Z — resubmitted

```javascript
await tab.cua.click({x:1175,y:771}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:16:43.845Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [before_settled_0.jpg](before_settled_0.jpg)
- [corrected_0.jpg](corrected_0.jpg)
- [corrected_verified_0.jpg](corrected_verified_0.jpg)
- [desktop_ready_0.jpg](desktop_ready_0.jpg)
- [reject_attempt_0.jpg](reject_attempt_0.jpg)
- [rejected_0.jpg](rejected_0.jpg)
- [resubmitted_0.jpg](resubmitted_0.jpg)
- [setup_0.jpg](setup_0.jpg)
