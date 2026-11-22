# ME3-CUA-0455: Focus retained after modal save

Status: **FAIL**
Executed: 2026-11-22T22:45:14.142Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard opened inline Rename, edited thread24 to CUA455 focus return test and saved. Title and History row updated. Immediately after save no visible focus returned to Rename/history; next Tab went directly to View answer and evidence. Four reverse Tabs manually recovered History; edited row remained accessible.

Expected focus return to meaningful history control was absent after Save; disabled Saved button and open inline editor remained, no visible return focus.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_edit_title_0.jpg; after.png: 08_after_save_0.jpg

## Actions

### 2026-11-22T22:43:49.249Z — 01_setup

```javascript
await viewport.set({width:1440,height:900});await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/24');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:51.947Z — 02_skip

```javascript
await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:03.164Z — 03_rename_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:06.705Z — 04_open

```javascript
await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:10.153Z — 05_open_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:21.653Z — 06_edit_title

```javascript
await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['TAB']});await activeTab.cua.keypress({keys:['CTRL','a']});await activeTab.cua.keypress({keys:['BACKSPACE']});await activeTab.cua.type({text:'CUA455 focus return test'});await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:26.986Z — 07_save

```javascript
await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:30.159Z — 08_after_save

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:40.964Z — 09_next_tab

```javascript
await activeTab.cua.keypress({keys:['TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:44.718Z — 10_reverse_history

```javascript
for(let i=0;i<4;i++)await activeTab.cua.keypress({keys:['SHIFT','TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:48.353Z — 11_history_open

```javascript
await activeTab.cua.keypress({keys:['ENTER']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:44:51.209Z — 12_history_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_setup_0.jpg](01_setup_0.jpg)
- [02_skip_0.jpg](02_skip_0.jpg)
- [03_rename_focus_0.jpg](03_rename_focus_0.jpg)
- [04_open_0.jpg](04_open_0.jpg)
- [05_open_settled_0.jpg](05_open_settled_0.jpg)
- [06_edit_title_0.jpg](06_edit_title_0.jpg)
- [07_save_0.jpg](07_save_0.jpg)
- [08_after_save_0.jpg](08_after_save_0.jpg)
- [09_next_tab_0.jpg](09_next_tab_0.jpg)
- [10_reverse_history_0.jpg](10_reverse_history_0.jpg)
- [11_history_open_0.jpg](11_history_open_0.jpg)
- [12_history_settled_0.jpg](12_history_settled_0.jpg)
