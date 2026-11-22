# ME3-CUA-0446: Keyboard publication save

Status: **PASS**
Executed: 2026-11-22T22:34:30.942Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard focus visibly reaches Save publication for PMID32356626; Enter saves, feedback/Saved badge appears, keyboard follows View saved publications and exact article exists in list (count4).

Initial Enter occurred after focus passed Save and did not save; reversed to visibly confirmed Save focus before successful activation.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 08_reverse_focus_0.jpg; after.png: 13_list_confirmed_0.jpg

## Actions

### 2026-11-22T22:32:40.224Z — 01_search_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/library'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:43.608Z — 02_search_pmid

```javascript
await activeTab.cua.click({x:700,y:485}); await activeTab.cua.type({text:'32356626'}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:32:47.213Z — 03_results

```javascript
await activeTab.cua.scroll({x:1000,y:700,scrollY:600,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:01.255Z — 04_tab_save_focus

```javascript
for(var k446=0;k446<11;k446++) await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:15.702Z — 05_save_focused

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:18.490Z — 06_save_enter

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:22.442Z — 07_saved_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:32.260Z — 08_reverse_focus

```javascript
await activeTab.cua.keypress({keys:['SHIFT','TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:43.303Z — 09_confirmed_focus_enter

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:33:48.515Z — 10_saved_confirmed

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:03.782Z — 11_keyboard_saved_link

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:13.806Z — 12_open_saved_keyboard

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:34:17.607Z — 13_list_confirmed

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_search_setup_0.jpg](01_search_setup_0.jpg)
- [02_search_pmid_0.jpg](02_search_pmid_0.jpg)
- [03_results_0.jpg](03_results_0.jpg)
- [04_tab_save_focus_0.jpg](04_tab_save_focus_0.jpg)
- [05_save_focused_0.jpg](05_save_focused_0.jpg)
- [06_save_enter_0.jpg](06_save_enter_0.jpg)
- [07_saved_settled_0.jpg](07_saved_settled_0.jpg)
- [08_reverse_focus_0.jpg](08_reverse_focus_0.jpg)
- [09_confirmed_focus_enter_0.jpg](09_confirmed_focus_enter_0.jpg)
- [10_saved_confirmed_0.jpg](10_saved_confirmed_0.jpg)
- [11_keyboard_saved_link_0.jpg](11_keyboard_saved_link_0.jpg)
- [12_open_saved_keyboard_0.jpg](12_open_saved_keyboard_0.jpg)
- [13_list_confirmed_0.jpg](13_list_confirmed_0.jpg)
