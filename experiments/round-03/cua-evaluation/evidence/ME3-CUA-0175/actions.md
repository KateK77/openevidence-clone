# ME3-CUA-0175: Configured but unchecked state

Status: **BLOCKED**
Executed: 2026-11-22T06:09:09.638Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public Settings visibly distinguishes Configured · not checked and warns configuration does not guarantee a successful request. This is partial observed behavior only.

Frozen fixture requires an isolated configured-but-unchecked instance. Only the shared public deployment is available; no independent fixture established. No probe run.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_public_configured_unchecked_0.jpg; after.png: 02_public_configured_unchecked_0.jpg

## Actions

### 2026-11-22T06:08:50.495Z — 01_inspect_connection_section

```javascript
await activeTab.cua.click({x:1380,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:09:06.434Z — 02_public_configured_unchecked

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_public_configured_unchecked_0.jpg](02_public_configured_unchecked_0.jpg)
