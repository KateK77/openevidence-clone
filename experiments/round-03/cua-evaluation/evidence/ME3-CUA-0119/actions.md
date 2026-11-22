# ME3-CUA-0119: Combined year and article type filters

Status: **FAIL**
Executed: 2026-11-22T05:10:46.361Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Single Year=2024 and Clinical Trial remained selected together after search; first3 records PMID38904963,38771888,39326417 showed2024 and trial metadata. However the frozen scenario requires a year interval plus article type; the UI offers no end year or interval control (same gap as112).

Required year interval cannot be entered. Single-year+type combination succeeds but does not fulfill the full frozen interval scenario.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_apply_combined_0.jpg; after.png: 06_combined_metadata_0.jpg

## Actions

### 2026-11-22T05:09:51.966Z — 01_combined_setup

```javascript
await freeThird.close(); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:09:59.313Z — 02_combined_select

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:326,y:627}); await activeTab.cua.click({x:400,y:576}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:960,y:579}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:10:10.266Z — 03_apply_combined

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:10:18.263Z — 04_combined_retained

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:10:25.818Z — 05_combined_scroll

```javascript
await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:10:31.789Z — 06_combined_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_combined_select_0.jpg](02_combined_select_0.jpg)
- [03_apply_combined_0.jpg](03_apply_combined_0.jpg)
- [04_combined_retained_0.jpg](04_combined_retained_0.jpg)
- [06_combined_metadata_0.jpg](06_combined_metadata_0.jpg)
