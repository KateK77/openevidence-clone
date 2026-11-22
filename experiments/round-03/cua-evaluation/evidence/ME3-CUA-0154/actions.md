# ME3-CUA-0154: Sources remain visible after provider failure

Status: **BLOCKED**
Executed: 2026-11-22T05:52:23.364Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Settings visibly reports AI synthesis configured and AI connection Configured · not checked (server model gemini-3.5-flash-lite). No provider probe or forced failure was run.

Requires a checked provider and authorized isolated forced-generation-error fixture. Neither is available; connection probe itself uses provider quota.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_settings_configured_0.jpg; after.png: 03_settings_configured_0.jpg

## Actions

### 2026-11-22T05:52:02.319Z — 01_desktop_precondition

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T05:52:03.587Z — 02_open_settings

```javascript
await activeTab.cua.click({x:95,y:550});
```
Tool error: False

### 2026-11-22T05:52:09.742Z — 03_settings_configured

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [03_settings_configured_0.jpg](03_settings_configured_0.jpg)
