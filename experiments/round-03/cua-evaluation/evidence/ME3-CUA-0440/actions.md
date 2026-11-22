# ME3-CUA-0440: Keyboard registration

Status: **BLOCKED**
Executed: 2026-11-22T22:29:19.270Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Authenticated synthetic session retained; fresh registration workflow not executed.

Current account password unknown; no independently available signed-out Chrome context/synthetic registration fixture. Cannot safely sign out and recover; prior account does not substitute fresh keyboard registration.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_settled_precondition_0.jpg; after.png: 02_settled_precondition_0.jpg

## Actions

### 2026-11-22T22:29:11.875Z — 01_precondition

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:29:16.045Z — 02_settled_precondition

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_precondition_0.jpg](01_precondition_0.jpg)
- [02_settled_precondition_0.jpg](02_settled_precondition_0.jpg)
