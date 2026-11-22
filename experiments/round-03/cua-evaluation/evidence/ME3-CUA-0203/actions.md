# ME3-CUA-0203: Language preference saves

Status: **PASS**
Executed: 2026-11-22T06:20:20.160Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Changed language from English to Chinese and saved; after full Settings reload, Chinese remained selected for the same account. Standard detail and Comfortable density retained. Persistence confirmed beyond the save toast.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_choose_chinese_0.jpg; after.png: 05_chinese_persisted_reload_0.jpg

## Actions

### 2026-11-22T06:19:37.371Z — 01_desktop_before_save

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T06:19:46.789Z — 02_choose_chinese

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:634,y:28}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T06:19:57.665Z — 03_chinese_draft_save

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:382,y:267});
```
Tool error: False

### 2026-11-22T06:20:05.040Z — 04_saved_then_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:20:14.155Z — 05_chinese_persisted_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_choose_chinese_0.jpg](02_choose_chinese_0.jpg)
- [03_chinese_draft_save_0.jpg](03_chinese_draft_save_0.jpg)
- [04_saved_then_reload_0.jpg](04_saved_then_reload_0.jpg)
- [05_chinese_persisted_reload_0.jpg](05_chinese_persisted_reload_0.jpg)
