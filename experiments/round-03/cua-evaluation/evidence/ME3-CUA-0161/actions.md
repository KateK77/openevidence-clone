# ME3-CUA-0161: No-model operation includes saved research

Status: **BLOCKED**
Executed: 2026-11-22T05:57:49.138Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Settings confirms AI synthesis configured; normal publication saving would not exercise no-model operation.

Requires independent absent-provider instance. No such instance is supplied, and production provider configuration is not modified.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_configured_not_unconfigured_0.jpg; after.png: 02_configured_not_unconfigured_0.jpg

## Actions

### 2026-11-22T05:57:35.073Z — 01_open_settings_precondition

```javascript
await activeTab.cua.click({x:93,y:549});
```
Tool error: False

### 2026-11-22T05:57:46.744Z — 02_configured_not_unconfigured

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_configured_not_unconfigured_0.jpg](02_configured_not_unconfigured_0.jpg)
