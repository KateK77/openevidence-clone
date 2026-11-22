# ME3-CUA-0326: History date descending order

Status: **PASS**
Executed: 2026-11-22T07:40:40.304Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Changed same13-row list from Oldest first to Newest first. CUA323 latest updated title now first followed by32356626,latest脊髓空洞症,A150; Nov22→Nov21→Nov20 dates descend. Previous sort replaced.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_oldest_baseline_0.jpg; after.png: 03_descending_dates_0.jpg

## Actions

### 2026-11-22T07:40:16.160Z — 01_oldest_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:40:19.165Z — 02_choose_newest

```javascript
await activeTab.cua.click({x:1316,y:72}); await activeTab.cua.keypress({keys:['HOME']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:40:29.266Z — 03_descending_dates

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_oldest_baseline_0.jpg](01_oldest_baseline_0.jpg)
- [03_descending_dates_0.jpg](03_descending_dates_0.jpg)
