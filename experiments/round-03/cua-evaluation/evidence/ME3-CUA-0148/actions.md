# ME3-CUA-0148: Retrieval-only mode creates a source-bearing result

Status: **BLOCKED**
Executed: 2026-11-22T05:41:22.681Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Current live homepage explicitly says AI synthesis configured. No independent instance deliberately lacking provider configuration is available. Did not submit heart failure SGLT2 under the wrong environment or change service configuration.

Requires separate unconfigured-model evaluation instance; current configured live instance fails prerequisite.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: precondition_0.jpg; after.png: precondition_0.jpg

## Actions

### 2026-11-22T05:41:08.184Z — 01_ai_configuration_precondition

```javascript
await activeTab.cua.click({x:114,y:136});
```
Tool error: False

### 2026-11-22T05:41:14.194Z — precondition

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [precondition_0.jpg](precondition_0.jpg)
