# ME3-CUA-0449: Mobile menu Escape dismiss

Status: **PASS**
Executed: 2026-11-22T22:36:41.526Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile keyboard-only Space opens focused hamburger; Escape closes drawer and returns clearly visible focus to same trigger.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_space_open_0.jpg; after.png: 04_focus_settled_0.jpg

## Actions

### 2026-11-22T22:36:18.331Z — 01_keyboard_trigger

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:21.831Z — 02_space_open

```javascript
await activeTab.cua.keypress({keys:['SPACE']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:24.235Z — 03_escape_close

```javascript
await activeTab.cua.keypress({keys:['ESC']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:36:27.379Z — 04_focus_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_keyboard_trigger_0.jpg](01_keyboard_trigger_0.jpg)
- [02_space_open_0.jpg](02_space_open_0.jpg)
- [03_escape_close_0.jpg](03_escape_close_0.jpg)
- [04_focus_settled_0.jpg](04_focus_settled_0.jpg)
