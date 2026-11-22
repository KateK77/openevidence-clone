# ME3-CUA-0071: Submission length counter

Status: **PASS**
Executed at: 2026-11-22T04:07:08.711Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Typed diabetes: 8/2,000; appended space-hyphen-space-test, newline and 中文: 18/2,000. Exact counter updates observed. No submission.



## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:06:00.044Z — before

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:06:16.382Z — short_text

```javascript
await tab.cua.click({x:649,y:676}); await tab.cua.type({text:"diabetes"}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:06:33.737Z — after

```javascript
await tab.cua.type({text:" - test\n中文"}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before.jpg](before.jpg)
- [short_text_0.jpg](short_text_0.jpg)
