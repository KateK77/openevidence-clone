# ME3-CUA-0454: Mobile narrow keyboard focus order

Status: **PASS**
Executed: 2026-11-22T22:43:47.767Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard-only at 390px: menu opened with Enter; reverse Shift+Tab reached Profile, Settings and Saved publications with visible outlines. Escape restored trigger, Tab traversed composer and recent items to visible footer; reverse focus remained visible without clipping/trap.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_keyboard_menu_0.jpg; after.png: 07_last_action_footer_0.jpg

## Actions

### 2026-11-22T22:42:42.900Z — 01_setup

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:46.164Z — 02_keyboard_menu

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:01.335Z — 03_reverse_profile

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['SHIFT','TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:10.954Z — 04_reverse_settings

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['SHIFT','TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:21.400Z — 05_reverse_publications

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['SHIFT','TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:25.625Z — 06_exit_to_composer

```javascript
await activeTab.cua.keypress({keys:['ESC']});for(let i=0;i<4;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:29.280Z — 07_last_action_footer

```javascript
for(let i=0;i<8;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:43:33.886Z — 08_reverse

```javascript
await activeTab.cua.keypress({keys:['SHIFT','TAB']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_setup_0.jpg](01_setup_0.jpg)
- [02_keyboard_menu_0.jpg](02_keyboard_menu_0.jpg)
- [03_reverse_profile_0.jpg](03_reverse_profile_0.jpg)
- [04_reverse_settings_0.jpg](04_reverse_settings_0.jpg)
- [05_reverse_publications_0.jpg](05_reverse_publications_0.jpg)
- [06_exit_to_composer_0.jpg](06_exit_to_composer_0.jpg)
- [07_last_action_footer_0.jpg](07_last_action_footer_0.jpg)
- [08_reverse_0.jpg](08_reverse_0.jpg)
