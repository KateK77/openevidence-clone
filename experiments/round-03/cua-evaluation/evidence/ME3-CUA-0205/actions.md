# ME3-CUA-0205: Detail preference saves

Status: **PASS**
Executed: 2026-11-22T06:22:29.005Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Selected Detailed, saved, navigated to Research Home and back to Settings. Detailed remains selected and Chinese language unchanged, with no unsaved changes. Persistence verified after route navigation.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_standard_to_detailed_0.jpg; after.png: 07_detailed_and_chinese_persist_0.jpg

## Actions

### 2026-11-22T06:21:33.952Z — 01_desktop_detail_save

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:21:41.713Z — 02_standard_to_detailed

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:650,y:749}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.click({x:1380,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:21:52.861Z — 03_detailed_draft

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:22:00.777Z — 04_save_detailed

```javascript
await activeTab.cua.click({x:382,y:268});
```
Tool error: False

### 2026-11-22T06:22:08.374Z — 05_saved_to_home

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:110,y:135});
```
Tool error: False

### 2026-11-22T06:22:15.714Z — 06_home_then_settings

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:90,y:550});
```
Tool error: False

### 2026-11-22T06:22:26.473Z — 07_detailed_and_chinese_persist

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_standard_to_detailed_0.jpg](02_standard_to_detailed_0.jpg)
- [03_detailed_draft_0.jpg](03_detailed_draft_0.jpg)
- [05_saved_to_home_0.jpg](05_saved_to_home_0.jpg)
- [06_home_then_settings_0.jpg](06_home_then_settings_0.jpg)
- [07_detailed_and_chinese_persist_0.jpg](07_detailed_and_chinese_persist_0.jpg)
