# ME3-CUA-0459: Public HTTPS landing works externally

Status: **PASS**
Executed: 2026-11-22T22:47:41.844Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390px public HTTPS homepage loaded MedEvidence AI 3.0 title, responsive workspace, readable research-only and synthetic-data disclaimers, menu and composer without horizontal clipping.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_settled_0.jpg; after.png: 02_settled_0.jpg

## Actions

### 2026-11-22T22:47:35.383Z — 01_mobile_public

```javascript
await viewport.set({width:390,height:844});await activeTab.reload();await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:47:39.201Z — 02_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));await nodeRepl.write({url:await activeTab.url(),title:await activeTab.title()});
```
Tool error: False
{"url":"https://medevidence-ai-v3.onrender.com/","title":"MedEvidence AI 3.0"}

## Original captures

- [01_mobile_public_0.jpg](01_mobile_public_0.jpg)
- [02_settled_0.jpg](02_settled_0.jpg)
