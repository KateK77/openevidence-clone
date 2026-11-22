# ME3-CUA-0212: Chinese settings without model explanation

Status: **BLOCKED**
Executed: 2026-11-22T06:32:59.302Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Only shared public configured instance available; Chinese preference saved. Deliberately absent-provider instance required by frozen gate is not supplied.

Cannot disable provider on shared deployment for scoring. Independent unconfigured_mode fixture required.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_configured_not_unconfigured_0.jpg; after.png: 02_configured_not_unconfigured_0.jpg

## Actions

### 2026-11-22T06:32:44.779Z — 01_configured_instance_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/settings');
```
Tool error: False

### 2026-11-22T06:32:54.624Z — 02_configured_not_unconfigured

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_configured_not_unconfigured_0.jpg](02_configured_not_unconfigured_0.jpg)
