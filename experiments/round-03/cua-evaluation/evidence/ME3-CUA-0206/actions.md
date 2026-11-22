# ME3-CUA-0206: Density preference saves

Status: **PASS**
Executed: 2026-11-22T06:24:02.253Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Captured Comfortable saved-answer row, chose Compact and saved. Reloaded Saved answers: same item remains and row height visibly decreased (about56 to44 screenshot pixels at matching1440x900 capture). Reloaded Settings confirms Compact, Chinese and Detailed retained. No data loss or toast-only inference.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_comfortable_list_before_0.jpg; after.png: 09_compact_list_persisted_0.jpg

## Actions

### 2026-11-22T06:22:29.249Z — 01_before_comfortable_answer_list

```javascript
await activeTab.cua.click({x:107,y:326});
```
Tool error: False

### 2026-11-22T06:22:39.404Z — 02_comfortable_list_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:90,y:550});
```
Tool error: False

### 2026-11-22T06:22:46.746Z — 03_settings_density_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:22:59.911Z — 04_choose_compact

```javascript
await activeTab.cua.click({x:650,y:839}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.click({x:1380,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:23:07.718Z — 05_compact_draft

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:23:15.796Z — 06_save_compact

```javascript
await activeTab.cua.click({x:380,y:268});
```
Tool error: False

### 2026-11-22T06:23:22.533Z — 07_saved_open_list

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:110,y:326});
```
Tool error: False

### 2026-11-22T06:23:31.506Z — 08_compact_list_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:23:40.699Z — 09_compact_list_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:91,y:552});
```
Tool error: False

### 2026-11-22T06:23:48.147Z — 10_settings_reload

```javascript
await activeTab.reload();
```
Tool error: False

### 2026-11-22T06:23:58.901Z — 11_compact_settings_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_comfortable_list_before_0.jpg](02_comfortable_list_before_0.jpg)
- [03_settings_density_before_0.jpg](03_settings_density_before_0.jpg)
- [05_compact_draft_0.jpg](05_compact_draft_0.jpg)
- [07_saved_open_list_0.jpg](07_saved_open_list_0.jpg)
- [08_compact_list_reload_0.jpg](08_compact_list_reload_0.jpg)
- [09_compact_list_persisted_0.jpg](09_compact_list_persisted_0.jpg)
- [11_compact_settings_persisted_0.jpg](11_compact_settings_persisted_0.jpg)
