# ME3-CUA-0077: Over 2000 characters rejected

Status: **PASS**
Executed at: 2026-11-22T04:14:31.266Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 390x844

At requested 390x844 viewport pasted 2,001 characters and submitted; readable length error shown. Opened Research history and observed same four baseline conversations, no new item. Initial screenshot downscaling/scroll timeout recovered; final history capture is 390x844. No horizontal overflow in settled mobile UI.



## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_recovered_0.jpg
- after.png from viewport_recovery_0.jpg

## Action trace

### 2026-11-22T04:12:14.719Z — setup

```javascript
await tab.cua.click({x:126,y:135}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:12:24.684Z — before

```javascript
await tab.cua.click({x:157,y:662}); await tab.clipboard.writeText(q2000+'X'); await tab.cua.keypress({keys:["CTRL","v"]}); await tab.cua.scroll({x:353,y:686,scrollY:310,scrollX:0}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: True

Error: Timed out after 10000ms waiting for CDP command Input.synthesizeScrollGesture.
### 2026-11-22T04:12:42.956Z — before_recovered

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:12:53.358Z — submitted

```javascript
await tab.cua.click({x:277,y:768}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:01.529Z — validation

```javascript
await tab.cua.click({x:170,y:299}); await tab.cua.keypress({keys:["PAGEDOWN"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:13.623Z — submit_visible

```javascript
await tab.cua.click({x:277,y:56}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:21.331Z — after_error

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:33.009Z — viewport_recovery

```javascript
await viewport.reset(); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:41.241Z — history

```javascript
await tab.cua.click({x:306,y:627}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:13:47.402Z — history_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:14:11.003Z — history_open

```javascript
await tab.cua.click({x:320,y:653}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_error_0.jpg](after_error_0.jpg)
- [before_recovered_0.jpg](before_recovered_0.jpg)
- [history_0.jpg](history_0.jpg)
- [history_open_0.jpg](history_open_0.jpg)
- [history_settled_0.jpg](history_settled_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_visible_0.jpg](submit_visible_0.jpg)
- [submitted_0.jpg](submitted_0.jpg)
- [validation_0.jpg](validation_0.jpg)
- [viewport_recovery_0.jpg](viewport_recovery_0.jpg)
