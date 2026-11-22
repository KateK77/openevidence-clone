# ME3-CUA-0363: Clear saved-publication filter

Status: **PASS**
Executed: 2026-11-22T21:49:28.878Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 applied smoking cessation filter showing only39878158. Clearing restores Minnesota6373426 and ADA33551565 alongside Electronic cigarettes without submit/reload. All cards readable via vertical scroll, no horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_prepare_0.jpg; after.png: 08_mobile_restored_remaining_0.jpg

## Actions

### 2026-11-22T21:48:11.810Z — 01_mobile_prepare

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:48:20.999Z — 02_mobile_unfiltered

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:48:32.190Z — 03_mobile_filter_control

```javascript
await activeTab.cua.scroll({x:200,y:300,scrollY:-1810,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:48:43.756Z — 04_mobile_restrictive_filter

```javascript
await activeTab.cua.click({x:155,y:448}); await activeTab.cua.type({text:'smoking cessation'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:48:51.937Z — 05_mobile_restricted

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:49:00.059Z — 06_mobile_clear

```javascript
await activeTab.cua.click({x:155,y:448}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:49:07.684Z — 07_mobile_restored_first

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:49:15.905Z — 08_mobile_restored_remaining

```javascript
await activeTab.cua.scroll({x:200,y:700,scrollY:1000,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_prepare_0.jpg](01_mobile_prepare_0.jpg)
- [02_mobile_unfiltered_0.jpg](02_mobile_unfiltered_0.jpg)
- [03_mobile_filter_control_0.jpg](03_mobile_filter_control_0.jpg)
- [04_mobile_restrictive_filter_0.jpg](04_mobile_restrictive_filter_0.jpg)
- [05_mobile_restricted_0.jpg](05_mobile_restricted_0.jpg)
- [06_mobile_clear_0.jpg](06_mobile_clear_0.jpg)
- [07_mobile_restored_first_0.jpg](07_mobile_restored_first_0.jpg)
- [08_mobile_restored_remaining_0.jpg](08_mobile_restored_remaining_0.jpg)
