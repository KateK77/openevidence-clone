# ME3-CUA-0412: Source content rendered inert

Status: **BLOCKED**
Executed: 2026-11-22T22:16:20.968Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Current unchanged app captured; no controlled publication containing HTML-looking abstract text available.

Required untrusted-source fixture not provided. No live PubMed metadata or app/database modified to create it.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_precondition_only_0.jpg; after.png: 02_precondition_only_0.jpg

## Actions

### 2026-11-22T22:16:02.689Z — 01_desktop_precondition_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:16:18.130Z — 02_precondition_only

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_precondition_setup_0.jpg](01_desktop_precondition_setup_0.jpg)
- [02_precondition_only_0.jpg](02_precondition_only_0.jpg)
