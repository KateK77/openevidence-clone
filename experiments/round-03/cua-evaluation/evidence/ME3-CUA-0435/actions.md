# ME3-CUA-0435: Mobile account destinations

Status: **PASS**
Executed: 2026-11-22T22:26:58.034Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

390px drawer opens Settings and Profile; preference controls/save and profile fields/save accessible through vertical scroll; no horizontal clipping. No settings changed.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_setup_0.jpg; after.png: 08_profile_settled_0.jpg

## Actions

### 2026-11-22T22:26:15.354Z — 01_mobile_setup

```javascript
await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:18.567Z — 02_open_drawer

```javascript
await activeTab.cua.click({x:29,y:31}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:21.359Z — 03_settings

```javascript
await activeTab.cua.click({x:80,y:528}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:24.142Z — 04_settings_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:36.313Z — 05_settings_scroll

```javascript
await activeTab.cua.scroll({x:210,y:700,scrollY:559,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:40.471Z — 06_menu_again

```javascript
await activeTab.cua.scroll({x:210,y:400,scrollY:-1000,scrollX:0}); await activeTab.cua.click({x:29,y:31}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:45.152Z — 07_profile

```javascript
await activeTab.cua.click({x:80,y:568}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:26:47.641Z — 08_profile_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_setup_0.jpg](01_mobile_setup_0.jpg)
- [02_open_drawer_0.jpg](02_open_drawer_0.jpg)
- [03_settings_0.jpg](03_settings_0.jpg)
- [04_settings_settled_0.jpg](04_settings_settled_0.jpg)
- [05_settings_scroll_0.jpg](05_settings_scroll_0.jpg)
- [06_menu_again_0.jpg](06_menu_again_0.jpg)
- [07_profile_0.jpg](07_profile_0.jpg)
- [08_profile_settled_0.jpg](08_profile_settled_0.jpg)
