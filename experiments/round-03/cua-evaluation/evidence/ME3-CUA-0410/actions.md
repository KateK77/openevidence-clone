# ME3-CUA-0410: Error messages contain no raw secrets

Status: **PASS**
Executed: 2026-11-22T22:14:32.060Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Submitted actual2001-character synthetic input; visible error says question: Ensure this field has no more than2000 characters. No provider key, session cookie, backend trace or SQL exception is visible.

Scope limited to ordinary overlength validation error; no general security guarantee or backend secret inspection claimed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_actual_count_before_submit_0.jpg; after.png: 04_invalid_error_inspection_0.jpg

## Actions

### 2026-11-22T22:13:52.668Z — 01_invalid_input_form

```javascript
await activeTab.cua.click({x:120,y:135}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:14:02.975Z — 02_overlimit_input

```javascript
await activeTab.cua.click({x:800,y:650}); await activeTab.cua.type({text:'x'.repeat(2001)}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:14:11.248Z — 03_actual_count_before_submit

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:14:18.697Z — 04_invalid_error_inspection

```javascript
await activeTab.cua.click({x:1190,y:755}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_invalid_input_form_0.jpg](01_invalid_input_form_0.jpg)
- [02_overlimit_input_0.jpg](02_overlimit_input_0.jpg)
- [03_actual_count_before_submit_0.jpg](03_actual_count_before_submit_0.jpg)
- [04_invalid_error_inspection_0.jpg](04_invalid_error_inspection_0.jpg)
