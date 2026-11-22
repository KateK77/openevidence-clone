# ME3-CUA-0464: Public saved publication persistence

Status: **BLOCKED**
Executed: 2026-11-22T22:49:30.038Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Public saved-publication list renders five account-bound synthetic bookmarks; current-session saved state visible.

Required refresh plus reauthentication cannot be completed without recoverable account credentials. Existing-session bookmark persistence is insufficient.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_saved_precondition_0.jpg; after.png: 02_saved_settled_0.jpg

## Actions

### 2026-11-22T22:49:25.030Z — 01_saved_precondition

```javascript
await source463.close();await activeTab.cua.click({x:105,y:465});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:49:27.582Z — 02_saved_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_saved_precondition_0.jpg](01_saved_precondition_0.jpg)
- [02_saved_settled_0.jpg](02_saved_settled_0.jpg)
