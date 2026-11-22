# ME3-CUA-0076: Over 2000 characters rejected

Status: **PASS**
Executed at: 2026-11-22T04:12:14.474Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Pasted 2,001 characters, counter 2001/2,000. Submission produced 'question: Ensure this field has no more than 2000 characters.' Reopened history: same four pre-existing conversations, no additional research item.



## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_0.jpg
- after.png from validation_0.jpg

## Action trace

### 2026-11-22T04:11:25.523Z — baseline_history

```javascript
await tab.cua.click({x:99,y:281}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:11:33.225Z — home

```javascript
await tab.cua.click({x:125,y:135}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:11:42.691Z — before

```javascript
await tab.cua.click({x:601,y:678}); await tab.clipboard.writeText(q2000+'X'); await tab.cua.keypress({keys:["CTRL","v"]}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:11:50.673Z — rejected

```javascript
await tab.cua.click({x:1178,y:770}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:11:57.333Z — validation

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:12:05.458Z — after

```javascript
await tab.cua.click({x:103,y:283}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [baseline_history_0.jpg](baseline_history_0.jpg)
- [before_0.jpg](before_0.jpg)
- [home_0.jpg](home_0.jpg)
- [rejected_0.jpg](rejected_0.jpg)
- [validation_0.jpg](validation_0.jpg)
