# ME3-CUA-0447: Keyboard publication save

Status: **PASS**
Executed: 2026-11-22T22:35:53.630Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard-only after setup: reaches query, retrieves live PMID33713498, tabs to visibly focused Save, Enter saves, keyboard follows reading-list link and exact PMID/title persists in list(count5).



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 07_focus_settled_0.jpg; after.png: 11_list_settled_0.jpg

## Actions

### 2026-11-22T22:34:31.188Z — 01_keyboard_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/library'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:34.804Z — 02_keyboard_query_focus

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:46.608Z — 03_focus_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:56.454Z — 04_search

```javascript
await activeTab.cua.type({text:'33713498'}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:00.426Z — 05_results_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:09.452Z — 06_keyboard_save_navigation

```javascript
for(var k447=0;k447<11;k447++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:14.847Z — 07_focus_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:30.386Z — 08_enter_save

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:33.714Z — 09_saved_feedback

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:37.162Z — 10_saved_list_keyboard

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:35:40.904Z — 11_list_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_keyboard_setup_0.jpg](01_keyboard_setup_0.jpg)
- [02_keyboard_query_focus_0.jpg](02_keyboard_query_focus_0.jpg)
- [03_focus_settled_0.jpg](03_focus_settled_0.jpg)
- [04_search_0.jpg](04_search_0.jpg)
- [05_results_settled_0.jpg](05_results_settled_0.jpg)
- [06_keyboard_save_navigation_0.jpg](06_keyboard_save_navigation_0.jpg)
- [07_focus_settled_0.jpg](07_focus_settled_0.jpg)
- [08_enter_save_0.jpg](08_enter_save_0.jpg)
- [09_saved_feedback_0.jpg](09_saved_feedback_0.jpg)
- [10_saved_list_keyboard_0.jpg](10_saved_list_keyboard_0.jpg)
- [11_list_settled_0.jpg](11_list_settled_0.jpg)
