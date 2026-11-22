# ME3-CUA-0217: Language setting persists through sign-out

Status: **BLOCKED**
Executed: 2026-11-22T06:37:30.419Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Chinese preference persisted through previous reloads, but active synthetic account reauthentication credentials are unavailable in resumed context.

Cannot complete required sign-out/back-in without losing test account access. Reload alone does not establish reauthentication persistence.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_chinese_saved_no_credentials_0.jpg; after.png: 02_chinese_saved_no_credentials_0.jpg

## Actions

### 2026-11-22T06:37:12.683Z — 01_reauthentication_precondition

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/settings');
```
Tool error: False

### 2026-11-22T06:37:27.213Z — 02_chinese_saved_no_credentials

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_chinese_saved_no_credentials_0.jpg](02_chinese_saved_no_credentials_0.jpg)
