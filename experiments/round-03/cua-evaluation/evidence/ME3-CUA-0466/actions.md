# ME3-CUA-0466: Public model unavailability honesty

Status: **BLOCKED**
Executed: 2026-11-22T22:50:01.736Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile Settings shows Configured—not checked and gemini-3.5-flash-lite, with provider-quota warning readable.

Required unavailable/unconfigured hosted fixture absent. Did not alter production configuration or invoke quota-consuming health check.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_model_0.jpg; after.png: 02_model_scroll_0.jpg

## Actions

### 2026-11-22T22:49:44.848Z — 01_mobile_model

```javascript
await viewport.set({width:390,height:844});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:49:47.437Z — 02_model_scroll

```javascript
await activeTab.cua.scroll({x:345,y:706,scrollY:470,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_model_0.jpg](01_mobile_model_0.jpg)
- [02_model_scroll_0.jpg](02_model_scroll_0.jpg)
