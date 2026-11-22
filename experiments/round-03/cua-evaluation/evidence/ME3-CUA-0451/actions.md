# ME3-CUA-0451: Mobile account switch safety

Status: **BLOCKED**
Executed: 2026-11-22T22:38:04.147Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile authenticated accountA state captured; identity switch not executed.

No accountB credentials and accountA recovery password; sign-out could strand session and cannot establish required B isolation.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_precondition_only_0.jpg; after.png: 01_precondition_only_0.jpg

## Actions

### 2026-11-22T22:37:56.077Z — 01_precondition_only

```javascript
await activeTab.cua.click({x:182,y:290}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_precondition_only_0.jpg](01_precondition_only_0.jpg)
