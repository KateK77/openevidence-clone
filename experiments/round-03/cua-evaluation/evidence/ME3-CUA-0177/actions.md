# ME3-CUA-0177: Connection probe explicit control

Status: **BLOCKED**
Executed: 2026-11-22T06:09:43.689Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public settings has an explicit Check AI connection button and description: one short nonmedical prompt, provider quota usage, JSON/Chinese checks, no medical-quality validation. Repeated views remained not checked; button not activated.

Required isolated configured-unchecked fixture absent. Visible control is partial evidence, not a successful probe or proof of all backend activity.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_probe_description_0.jpg; after.png: 02_probe_description_0.jpg

## Actions

### 2026-11-22T06:09:37.524Z — 01_desktop_probe_control

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:09:40.089Z — 02_probe_description

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_probe_description_0.jpg](02_probe_description_0.jpg)
