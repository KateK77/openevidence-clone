# ME3-CUA-0204: Language preference saves

Status: **PASS**
Executed: 2026-11-22T06:21:33.711Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared a saved English baseline through mobile UI, then selected Chinese, saved and reloaded Settings. Chinese remains selected and configured-language notice uses Chinese. Controls/status remain readable at390x844; no toast-only inference.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 05_baseline_saved_choose_chinese_0.jpg; after.png: 08_mobile_chinese_persisted_0.jpg

## Actions

### 2026-11-22T06:20:20.401Z — 01_mobile_prepare_english_baseline

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:20:31.755Z — 02_set_english_for_fresh_mobile_transition

```javascript
await activeTab.cua.click({x:187,y:757}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.click({x:360,y:798}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:20:49.972Z — 03_english_baseline_save_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:20:57.186Z — 04_save_baseline

```javascript
await activeTab.cua.click({x:101,y:261});
```
Tool error: False

### 2026-11-22T06:21:03.932Z — 05_baseline_saved_choose_chinese

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:182,y:20}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T06:21:12.282Z — 06_chinese_mobile_save

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:101,y:261});
```
Tool error: False

### 2026-11-22T06:21:20.757Z — 07_mobile_saved_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:21:31.183Z — 08_mobile_chinese_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_prepare_english_baseline_0.jpg](01_mobile_prepare_english_baseline_0.jpg)
- [03_english_baseline_save_control_0.jpg](03_english_baseline_save_control_0.jpg)
- [05_baseline_saved_choose_chinese_0.jpg](05_baseline_saved_choose_chinese_0.jpg)
- [06_chinese_mobile_save_0.jpg](06_chinese_mobile_save_0.jpg)
- [07_mobile_saved_reload_0.jpg](07_mobile_saved_reload_0.jpg)
- [08_mobile_chinese_persisted_0.jpg](08_mobile_chinese_persisted_0.jpg)
