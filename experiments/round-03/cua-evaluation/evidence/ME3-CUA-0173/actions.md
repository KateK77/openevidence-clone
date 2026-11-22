# ME3-CUA-0173: Model status reachable from home

Status: **PASS**
Executed: 2026-11-22T06:08:45.765Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 activated the model-status link on Research home; /settings opened with matching configured notice and English preference. Link and readiness explanation remain readable without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_status_link_0.jpg; after.png: 03_mobile_matching_settings_0.jpg

## Actions

### 2026-11-22T06:08:24.052Z — 01_home_for_mobile

```javascript
await activeTab.cua.click({x:110,y:135}); await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T06:08:30.170Z — 02_mobile_status_link

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:171,y:587});
```
Tool error: False

### 2026-11-22T06:08:43.431Z — 03_mobile_matching_settings

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/settings

## Original captures

- [02_mobile_status_link_0.jpg](02_mobile_status_link_0.jpg)
- [03_mobile_matching_settings_0.jpg](03_mobile_matching_settings_0.jpg)
