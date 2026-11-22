# ME3-CUA-0207: Density preference saves

Status: **PASS**
Executed: 2026-11-22T06:27:13.960Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared a saved Comfortable baseline at390x844 and captured Saved answers. Selected Compact and saved, then loaded/reloaded the answer list: same row remained and height decreased about48 to42 pixels in matching390x844 captures. Reloaded Settings confirms Compact with Chinese/Detailed retained. Controls/status readable.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 09_comfortable_mobile_list_0.jpg; after.png: 17_compact_list_persisted_0.jpg

## Actions

### 2026-11-22T06:24:02.504Z — 01_mobile_prepare_baseline

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.click({x:360,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:24:24.655Z — 02_mobile_density_baseline_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:24:32.233Z — 03_select_comfortable_baseline

```javascript
await activeTab.cua.click({x:190,y:196}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T06:24:40.717Z — 04_save_comfortable_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:105,y:260});
```
Tool error: False

### 2026-11-22T06:24:52.439Z — 05_baseline_saved_top

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:360,y:790}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T06:25:02.873Z — 06_mobile_nav_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:29,y:31});
```
Tool error: False

### 2026-11-22T06:25:13.046Z — 07_mobile_menu

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:25:20.613Z — 08_open_mobile_saved_answers

```javascript
await activeTab.cua.click({x:109,y:325});
```
Tool error: False

### 2026-11-22T06:25:27.902Z — 09_comfortable_mobile_list

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url()); await activeTab.cua.click({x:29,y:31});
```
Tool error: False
https://medevidence-ai-v3.onrender.com/saved

### 2026-11-22T06:25:36.089Z — 10_menu_back_settings

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:95,y:527});
```
Tool error: False

### 2026-11-22T06:25:43.205Z — 11_mobile_settings_scroll

```javascript
await activeTab.cua.click({x:360,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:25:53.336Z — 12_comfortable_to_compact

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:26:03.811Z — 13_choose_compact_mobile

```javascript
await activeTab.cua.click({x:185,y:199}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T06:26:12.315Z — 14_compact_mobile_save

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:105,y:264});
```
Tool error: False

### 2026-11-22T06:26:20.278Z — 15_saved_navigate_to_list

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.goto('https://medevidence-ai-v3.onrender.com/saved');
```
Tool error: False

### 2026-11-22T06:26:29.621Z — 16_compact_mobile_list_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:26:36.873Z — 17_compact_list_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.goto('https://medevidence-ai-v3.onrender.com/settings');
```
Tool error: False

### 2026-11-22T06:26:43.918Z — 18_settings_reload

```javascript
await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:26:52.011Z — 19_settings_top_after_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:360,y:789}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:27:11.249Z — 20_compact_mobile_settings_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_density_baseline_controls_0.jpg](02_mobile_density_baseline_controls_0.jpg)
- [04_save_comfortable_baseline_0.jpg](04_save_comfortable_baseline_0.jpg)
- [05_baseline_saved_top_0.jpg](05_baseline_saved_top_0.jpg)
- [06_mobile_nav_before_0.jpg](06_mobile_nav_before_0.jpg)
- [07_mobile_menu_0.jpg](07_mobile_menu_0.jpg)
- [09_comfortable_mobile_list_0.jpg](09_comfortable_mobile_list_0.jpg)
- [10_menu_back_settings_0.jpg](10_menu_back_settings_0.jpg)
- [12_comfortable_to_compact_0.jpg](12_comfortable_to_compact_0.jpg)
- [14_compact_mobile_save_0.jpg](14_compact_mobile_save_0.jpg)
- [15_saved_navigate_to_list_0.jpg](15_saved_navigate_to_list_0.jpg)
- [16_compact_mobile_list_reload_0.jpg](16_compact_mobile_list_reload_0.jpg)
- [17_compact_list_persisted_0.jpg](17_compact_list_persisted_0.jpg)
- [19_settings_top_after_reload_0.jpg](19_settings_top_after_reload_0.jpg)
- [20_compact_mobile_settings_persisted_0.jpg](20_compact_mobile_settings_persisted_0.jpg)
