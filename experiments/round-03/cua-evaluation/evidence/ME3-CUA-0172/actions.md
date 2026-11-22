# ME3-CUA-0172: Model status reachable from home

Status: **PASS**
Executed: 2026-11-22T06:08:23.816Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Activated Model status & language settings from desktop Research home. It opened /settings with the matching AI synthesis configured notice and saved English preference; readiness wording states configuration does not guarantee a successful request.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_model_status_link_0.jpg; after.png: 03_matching_settings_0.jpg

## Actions

### 2026-11-22T06:08:03.048Z — 01_desktop_home

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:08:09.172Z — 02_model_status_link

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:575,y:573});
```
Tool error: False

### 2026-11-22T06:08:20.500Z — 03_matching_settings

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/settings

## Original captures

- [02_model_status_link_0.jpg](02_model_status_link_0.jpg)
- [03_matching_settings_0.jpg](03_matching_settings_0.jpg)
