# ME3-CUA-0149: Retrieval-only mode creates a source-bearing result

Status: **BLOCKED**
Executed: 2026-11-22T05:41:34.304Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 homepage explicitly says AI synthesis configured. No independent absent-provider instance supplied; source-bearing retrieval-only submission was not executed.

Required independent unconfigured-mode instance unavailable.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: precondition_0.jpg; after.png: precondition_0.jpg

## Actions

### 2026-11-22T05:41:22.936Z — 01_mobile_configuration_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:41:31.654Z — precondition

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [precondition_0.jpg](precondition_0.jpg)
