# ME3-CUA-0430: Mobile menu opens and closes visibly

Status: **PASS**
Executed: 2026-11-22T22:22:28.483Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 menu opens showing all primary/Settings/Profile destinations and visible Close; Close dismisses overlay leaving thread22 readable with no page-wide horizontal clipping.

Pointer mobile viewport, not native touch.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_open_menu_0.jpg; after.png: 04_closed_settled_0.jpg

## Actions

### 2026-11-22T22:21:56.738Z — 01_mobile_transition

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:22:05.977Z — 02_open_menu

```javascript
await activeTab.cua.click({x:29,y:31}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:22:22.853Z — 03_close_menu

```javascript
await activeTab.cua.click({x:279,y:28}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:22:25.833Z — 04_closed_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_transition_0.jpg](01_mobile_transition_0.jpg)
- [02_open_menu_0.jpg](02_open_menu_0.jpg)
- [03_close_menu_0.jpg](03_close_menu_0.jpg)
- [04_closed_settled_0.jpg](04_closed_settled_0.jpg)
