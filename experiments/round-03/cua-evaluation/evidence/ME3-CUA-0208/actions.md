# ME3-CUA-0208: Preferences isolated across accounts

Status: **BLOCKED**
Executed: 2026-11-22T06:27:18.097Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Account A is now saved Chinese/Detailed/Compact. A second independently authenticated synthetic account and A reauthentication credentials are not available in resumed context.

Cannot perform A-to-B account switch and compare B retained preferences while restoring active test account. Single-account persistence is not ownership isolation evidence.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_account_a_preferences_0.jpg; after.png: 02_account_a_preferences_0.jpg

## Actions

### 2026-11-22T06:27:14.204Z — 01_desktop_account_a_settings

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:27:15.554Z — 02_account_a_preferences

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_account_a_preferences_0.jpg](02_account_a_preferences_0.jpg)
