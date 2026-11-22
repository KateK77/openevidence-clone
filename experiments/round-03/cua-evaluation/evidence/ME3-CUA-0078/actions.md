# ME3-CUA-0078: No duplicate pending submit

Status: **BLOCKED**
Executed at: 2026-11-22T04:14:46.866Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Inspected unchanged public configured service and reviewed documented fixture/setup options. No controlled-delay fixture is available; did not attempt uncontrolled duplicate provider requests.

Required test-safe controllable latency fixture cannot be established on current public instance without changing service environment. Public production configuration remains unchanged.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from setup_0.jpg
- after.png from after_0.jpg

## Action trace

### 2026-11-22T04:14:31.514Z — setup

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:14:43.893Z — after

```javascript
await tab.cua.click({x:124,y:136}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [setup_0.jpg](setup_0.jpg)
