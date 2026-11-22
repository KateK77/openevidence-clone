# ME3-CUA-0114: Year range with no matches

Status: **PASS**
Executed: 2026-11-22T05:04:12.296Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile Year 2030 yielded explicit 0-publication empty state; clearing the Year field and resubmitting restored 16 diabetes publications. Controls, notice and result cards remained readable without page-wide overflow. Single-year empty recovery tested; end-year absence separately recorded.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_set_year_0.jpg; after.png: 07_mobile_recovered_0.jpg

## Actions

### 2026-11-22T05:03:24.579Z — 01_mobile_before

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T05:03:29.869Z — 02_mobile_set_year

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:100,y:644}); await activeTab.cua.type({text:'2030'});
```
Tool error: False

### 2026-11-22T05:03:38.655Z — 03_mobile_submit

```javascript
await activeTab.cua.click({x:180,y:563}); await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:03:44.829Z — 04_mobile_empty_clear

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:03:50.247Z — 05_mobile_clear

```javascript
await activeTab.cua.click({x:95,y:434}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']});
```
Tool error: False

### 2026-11-22T05:03:55.240Z — 06_mobile_recovery_submit

```javascript
await activeTab.cua.click({x:180,y:353});
```
Tool error: False

### 2026-11-22T05:04:00.610Z — 07_mobile_recovered

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_set_year_0.jpg](02_mobile_set_year_0.jpg)
- [04_mobile_empty_clear_0.jpg](04_mobile_empty_clear_0.jpg)
- [07_mobile_recovered_0.jpg](07_mobile_recovered_0.jpg)
