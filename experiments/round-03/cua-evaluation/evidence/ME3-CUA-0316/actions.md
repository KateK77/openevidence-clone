# ME3-CUA-0316: Research history lists owned threads

Status: **FAIL**
Executed: 2026-11-22T07:30:30.646Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Actual390px history displays owned titles and row links, but visible rows omit the desktop dates/latest-activity information; hovering first row reveals none. Earlier captures01/02 were desktop during viewport recovery and excluded from mobile scoring.

Required readable dates/latest-activity information absent from mobile history rows.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_mobile_actual_viewport_0.jpg; after.png: 04_mobile_missing_dates_0.jpg

## Actions

### 2026-11-22T07:29:35.493Z — 01_mobile_history

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:29:44.340Z — 02_mobile_list

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:30:06.287Z — 03_mobile_actual_viewport

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:30:16.352Z — 04_mobile_missing_dates

```javascript
await activeTab.cua.move({x:159,y:490}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_history_0.jpg](01_mobile_history_0.jpg)
- [02_mobile_list_0.jpg](02_mobile_list_0.jpg)
- [03_mobile_actual_viewport_0.jpg](03_mobile_actual_viewport_0.jpg)
- [04_mobile_missing_dates_0.jpg](04_mobile_missing_dates_0.jpg)
