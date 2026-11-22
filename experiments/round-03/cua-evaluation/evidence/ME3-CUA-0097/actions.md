# ME3-CUA-0097: Query error should retain draft

Status: **BLOCKED**
Executed: 2026-11-22T04:34:56.038Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Returned to research composer; no injected upstream error attempted.

Required documented isolated PubMed-fault fixture unavailable; normal translation-limit outcome is not an upstream retrieval failure.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: precondition_0.jpg; after.png: precondition_0.jpg

## Actions

### 2026-11-22T04:34:52.721Z — precondition

```javascript
await tab.cua.click({x:106,y:134}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [precondition_0.jpg](precondition_0.jpg)
