# ME3-CUA-0276: Regenerate disabled without provider

Status: **BLOCKED**
Executed: 2026-11-22T07:07:10.571Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public server configured; current detail has regeneration action. Required no-provider instance not supplied.

Independent unconfigured_mode fixture absent; cannot assess disabled-action state by modifying shared configuration.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_configured_not_no_provider_0.jpg; after.png: 02_configured_not_no_provider_0.jpg

## Actions

### 2026-11-22T07:06:27.837Z — 01_no_provider_regeneration_gate

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T07:07:07.468Z — 02_configured_not_no_provider

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_configured_not_no_provider_0.jpg](02_configured_not_no_provider_0.jpg)
