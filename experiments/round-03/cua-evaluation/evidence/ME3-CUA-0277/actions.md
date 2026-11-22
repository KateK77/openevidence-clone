# ME3-CUA-0277: Regenerate disabled without provider

Status: **BLOCKED**
Executed: 2026-11-22T07:07:24.110Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile current configured instance available; independent absent-provider state unavailable.

unconfigured_mode fixture missing; no shared-server settings changed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_configured_precondition_0.jpg; after.png: 02_mobile_configured_precondition_0.jpg

## Actions

### 2026-11-22T07:07:10.814Z — 01_mobile_no_provider_gate

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T07:07:21.810Z — 02_mobile_configured_precondition

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_configured_precondition_0.jpg](02_mobile_configured_precondition_0.jpg)
