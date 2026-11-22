# ME3-CUA-0170: Composer label reflects no-model mode

Status: **BLOCKED**
Executed: 2026-11-22T06:03:45.016Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Homepage says AI synthesis configured and uses Ask AI. This is expected configured mode, not the required no-model composer.

Absent-provider fixture unavailable. Current label is not scored as failure because the prerequisite mode is not present.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_configured_composer_label_0.jpg; after.png: 03_configured_composer_label_0.jpg

## Actions

### 2026-11-22T06:03:21.163Z — 01_restore_desktop

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:03:22.517Z — 02_open_home_precondition

```javascript
await activeTab.cua.click({x:110,y:135}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T06:03:41.517Z — 03_configured_composer_label

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.markHandoff();
```
Tool error: False

## Original captures

- [03_configured_composer_label_0.jpg](03_configured_composer_label_0.jpg)
