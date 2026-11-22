# ME3-CUA-0458: Public HTTPS landing works externally

Status: **PASS**
Executed: 2026-11-22T22:47:35.138Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Actual desktop Chrome loaded documented public HTTPS host; title MedEvidence AI 3.0, branded workspace and Research demonstration—not for clinical use plus synthetic-information notice visibly present. Real authenticated navigation/composer rendered.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_landing_settled_0.jpg; after.png: 02_landing_settled_0.jpg

## Actions

### 2026-11-22T22:47:16.221Z — 01_public_home

```javascript
await viewport.set({width:1440,height:900});await activeTab.goto('https://medevidence-ai-v3.onrender.com/');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:47:20.929Z — 02_landing_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));await nodeRepl.write({url:await activeTab.url(),title:await activeTab.title()});
```
Tool error: False
{"url":"https://medevidence-ai-v3.onrender.com/","title":"MedEvidence AI 3.0"}

## Original captures

- [01_public_home_0.jpg](01_public_home_0.jpg)
- [02_landing_settled_0.jpg](02_landing_settled_0.jpg)
