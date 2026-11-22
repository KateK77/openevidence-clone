# ME3-CUA-0411: Error messages contain no raw secrets

Status: **PASS**
Executed: 2026-11-22T22:16:02.287Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px actual2001-character submission returns fully readable question length validation. No key, cookie, backend trace or SQL exception visible; message fits viewport.

Scope: this ordinary validation error only.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_overlimit_input_0.jpg; after.png: 03_mobile_error_no_secrets_0.jpg

## Actions

### 2026-11-22T22:15:27.043Z — 01_mobile_invalid_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:15:38.454Z — 02_mobile_overlimit_input

```javascript
await activeTab.cua.click({x:170,y:668}); await activeTab.cua.type({text:'x'.repeat(2001)}); await activeTab.cua.scroll({x:200,y:600,scrollY:400,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:15:50.479Z — 03_mobile_error_no_secrets

```javascript
await activeTab.cua.click({x:290,y:373}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_invalid_setup_0.jpg](01_mobile_invalid_setup_0.jpg)
- [02_mobile_overlimit_input_0.jpg](02_mobile_overlimit_input_0.jpg)
- [03_mobile_error_no_secrets_0.jpg](03_mobile_error_no_secrets_0.jpg)
