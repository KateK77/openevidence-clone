# ME3-CUA-0460: Public site supports sign-in entry

Status: **BLOCKED**
Executed: 2026-11-22T22:47:46.384Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public homepage is currently authenticated as synthetic account me3cua_20261120_batch004; account control displayed instead of Sign in.

Required signed-out public entry unavailable in existing authenticated context; recoverable credentials and independent signed-out Chrome context not supplied. Did not log out/strand session.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_signed_in_precondition_0.jpg; after.png: 01_signed_in_precondition_0.jpg

## Actions

### 2026-11-22T22:47:42.089Z — 01_signed_in_precondition

```javascript
await viewport.set({width:1440,height:900});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_signed_in_precondition_0.jpg](01_signed_in_precondition_0.jpg)
