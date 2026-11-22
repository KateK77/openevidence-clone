# ME3-CUA-0445: Keyboard dialog dismiss

Status: **FAIL**
Executed: 2026-11-22T22:32:18.604Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Pure keyboard History→thread24→Delete Enter opens confirmation. Escape leaves it visible; focus remains Delete. No deletion occurred.

Required Escape dismissal missing, reproducing444 with keyboard-only workflow.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_keyboard_confirm_open_0.jpg; after.png: 08_after_escape_0.jpg

## Actions

### 2026-11-22T22:31:29.740Z — 01_keyboard_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/history'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:31:32.833Z — 02_history_keyboard

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:31:47.760Z — 03_first_thread_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:31:51.609Z — 04_open_thread

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:31:54.638Z — 05_delete_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:09.576Z — 06_keyboard_confirm_open

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:12.953Z — 07_keyboard_escape

```javascript
await activeTab.cua.keypress({keys:['ESC']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:15.804Z — 08_after_escape

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:18.840Z — 09_cancel_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:26.463Z — 10_safe_cancel

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_keyboard_setup_0.jpg](01_keyboard_setup_0.jpg)
- [02_history_keyboard_0.jpg](02_history_keyboard_0.jpg)
- [03_first_thread_focus_0.jpg](03_first_thread_focus_0.jpg)
- [04_open_thread_0.jpg](04_open_thread_0.jpg)
- [05_delete_focus_0.jpg](05_delete_focus_0.jpg)
- [06_keyboard_confirm_open_0.jpg](06_keyboard_confirm_open_0.jpg)
- [07_keyboard_escape_0.jpg](07_keyboard_escape_0.jpg)
- [08_after_escape_0.jpg](08_after_escape_0.jpg)
- [09_cancel_focus_0.jpg](09_cancel_focus_0.jpg)
- [10_safe_cancel_0.jpg](10_safe_cancel_0.jpg)
