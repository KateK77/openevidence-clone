# ME3-CUA-0456: Focus retained after modal save

Status: **FAIL**
Executed: 2026-11-22T22:46:11.531Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard-only reproduced on thread23: title saved as CUA456 keyboard focus test; after Save, no visible focus returned to Rename/history and next Tab reached View answer and evidence. Manual reverse navigation returned to History with renamed row present.

Focus restoration requirement failed; save persisted, but editor stayed open and disabled Saved button had no visible return focus.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_open_0.jpg; after.png: 06_after_save_0.jpg

## Actions

### 2026-11-22T22:45:14.398Z — 01_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/23');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:17.298Z — 02_keyboard_rename

```javascript
await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['ENTER']});await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:21.608Z — 03_open

```javascript
await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:40.360Z — 04_edit

```javascript
await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['CTRL','a']});await activeTab.cua.keypress({keys:['BACKSPACE']});await activeTab.cua.type({text:'CUA456 keyboard focus test'});await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:44.973Z — 05_save

```javascript
await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:47.702Z — 06_after_save

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:45:51.053Z — 07_next_tab

```javascript
await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:04.749Z — 08_history_recover

```javascript
for(let i=0;i<4;i++)await activeTab.cua.keypress({keys:['SHIFT','TAB']});await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:08.724Z — 09_history_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_setup_0.jpg](01_setup_0.jpg)
- [02_keyboard_rename_0.jpg](02_keyboard_rename_0.jpg)
- [03_open_0.jpg](03_open_0.jpg)
- [04_edit_0.jpg](04_edit_0.jpg)
- [05_save_0.jpg](05_save_0.jpg)
- [06_after_save_0.jpg](06_after_save_0.jpg)
- [07_next_tab_0.jpg](07_next_tab_0.jpg)
- [08_history_recover_0.jpg](08_history_recover_0.jpg)
- [09_history_settled_0.jpg](09_history_settled_0.jpg)
