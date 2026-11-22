# ME3-CUA-0461: Public account persists across reload

Status: **BLOCKED**
Executed: 2026-11-22T22:48:03.869Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Profile shows existing synthetic account and saved first name; no fresh account created.

Fresh-account registration and recoverable new credentials/independent browser context unavailable; existing session persistence cannot substitute fresh-account scenario.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_profile_settled_0.jpg; after.png: 02_profile_settled_0.jpg

## Actions

### 2026-11-22T22:47:46.626Z — 01_existing_account_precondition

```javascript
await activeTab.cua.click({x:95,y:602});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:47:49.481Z — 02_profile_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_existing_account_precondition_0.jpg](01_existing_account_precondition_0.jpg)
- [02_profile_settled_0.jpg](02_profile_settled_0.jpg)
