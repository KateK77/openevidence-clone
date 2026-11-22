# ME3-CUA-0448: Mobile menu Escape dismiss

Status: **PASS**
Executed: 2026-11-22T22:36:18.084Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px Tab focuses menu trigger; Enter opens drawer with Close focused; Escape closes it and visible focus returns to hamburger trigger.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_open_keyboard_0.jpg; after.png: 05_focus_returned_0.jpg

## Actions

### 2026-11-22T22:35:53.897Z — 01_mobile_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:57.125Z — 02_menu_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:00.381Z — 03_open_keyboard

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:12.611Z — 04_escape

```javascript
await activeTab.cua.keypress({keys:['ESC']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:15.441Z — 05_focus_returned

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_setup_0.jpg](01_mobile_setup_0.jpg)
- [02_menu_focus_0.jpg](02_menu_focus_0.jpg)
- [03_open_keyboard_0.jpg](03_open_keyboard_0.jpg)
- [04_escape_0.jpg](04_escape_0.jpg)
- [05_focus_returned_0.jpg](05_focus_returned_0.jpg)
