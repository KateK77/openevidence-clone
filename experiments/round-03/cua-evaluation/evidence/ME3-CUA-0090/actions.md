# ME3-CUA-0090: Punctuation and hyphen input

Status: **BLOCKED**
Executed at: 2026-11-22T04:24:37.355Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Actual literature query GLP-1 receptor agonists returned16 publications; first visible title Mechanisms of action and therapeutic applications of GLP-1 and dual GIP/GLP-1 receptor agonists. Original hyphenated input retained, but no normalized-query field in lookup.

Full question and normalized-form inspection would require model-enabled research submission; fee authorization unavailable. Relevant lookup is partial evidence only.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:23:54.105Z — desktop_setup

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:24:00.924Z — open_library

```javascript
await tab.cua.click({x:97,y:415}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:24:09.423Z — before

```javascript
await tab.cua.click({x:624,y:486}); await tab.cua.type({text:'GLP-1 receptor agonists'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:24:17.537Z — submit

```javascript
await tab.cua.click({x:1228,y:486}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:24:26.232Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [desktop_setup_0.jpg](desktop_setup_0.jpg)
- [open_library_0.jpg](open_library_0.jpg)
- [submit_0.jpg](submit_0.jpg)
