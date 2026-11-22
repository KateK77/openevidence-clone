# ME3-CUA-0093: IME composition does not submit prematurely

Status: **BLOCKED**
Executed: 2026-11-22T04:32:23.096Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Chrome composer visible, but genuine Chinese IME composition session cannot be established through available browser controls. No paste/direct type was counted as IME.

Required genuine Chinese IME environment unavailable. Browser CUA direct type does not expose compositionstart/compositionend; no synthetic event injection used.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: precondition_0.jpg; after.png: precondition_0.jpg

## Actions

### 2026-11-22T04:32:20.370Z — precondition

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [precondition_0.jpg](precondition_0.jpg)
