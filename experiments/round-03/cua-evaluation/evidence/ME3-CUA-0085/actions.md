# ME3-CUA-0085: English input is not mistranslated

Status: **BLOCKED**
Executed at: 2026-11-22T04:21:46.779Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Actual literature lookup for SGLT2 heart failure returned 16 publications; first visible title Heart Failure With Reduced Ejection Fraction: A Review. Input retained. No normalized/executed-query provenance visible in lookup UI.

Full research provenance requires model-enabled submission; provider fees unapproved. Relevant search results alone cannot verify executed query.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from input_verified_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:21:16.031Z — before

```javascript
await tab.cua.click({x:516,y:481}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'SGLT2 heart failure'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:24.821Z — input_verified

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:31.065Z — submit

```javascript
await tab.cua.click({x:1204,y:483}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:37.367Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [input_verified_0.jpg](input_verified_0.jpg)
- [submit_0.jpg](submit_0.jpg)
