# ME3-CUA-0384: PDF answer export discoverable

Status: **BLOCKED**
Executed: 2026-11-22T22:08:43.285Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px Export>PDF reachable; activation produces readable PDF export downloaded message. Actual PDF rendering/title/status not inspected.

Downloaded-file verification inaccessible under existing browser security restriction. No toast-only PASS or alternate-route bypass.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_pdf_baseline_0.jpg; after.png: 04_mobile_pdf_activation_0.jpg

## Actions

### 2026-11-22T22:08:14.890Z — 01_mobile_pdf_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:08:22.533Z — 02_mobile_pdf_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:08:31.312Z — 03_mobile_pdf_menu

```javascript
await activeTab.cua.click({x:318,y:400}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:08:35.351Z — 04_mobile_pdf_activation

```javascript
await activeTab.cua.click({x:260,y:503}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_pdf_setup_0.jpg](01_mobile_pdf_setup_0.jpg)
- [02_mobile_pdf_baseline_0.jpg](02_mobile_pdf_baseline_0.jpg)
- [03_mobile_pdf_menu_0.jpg](03_mobile_pdf_menu_0.jpg)
- [04_mobile_pdf_activation_0.jpg](04_mobile_pdf_activation_0.jpg)
