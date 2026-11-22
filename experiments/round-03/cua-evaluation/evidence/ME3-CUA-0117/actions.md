# ME3-CUA-0117: Article-type filter

Status: **PASS**
Executed: 2026-11-22T05:08:03.808Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390x844 selected Clinical Trial by visible native select and resubmitted diabetes. 16 records returned; first three inspected PMID40294614,6373426,38653618 carry randomized/controlled/clinical-trial metadata, including titles without 'trial'. Filter remains selected and cards/badges readable without horizontal overflow. Mobile inspection sampled first three; desktop116 inspected entire16.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_mobile_choose_trial_0.jpg; after.png: 10_mobile_active_filter_0.jpg

## Actions

### 2026-11-22T05:06:56.587Z — 01_mobile_type_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:07:04.553Z — 02_mobile_reset_type

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:105,y:724}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:07:10.614Z — 03_mobile_broad_baseline

```javascript
await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:07:17.408Z — 04_mobile_choose_trial

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:105,y:724}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T05:07:24.546Z — 05_mobile_apply_trial

```javascript
await activeTab.cua.click({x:180,y:563}); await activeTab.cua.click({x:351,y:787}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:07:32.178Z — 06_mobile_trial_first

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:07:39.092Z — 07_mobile_scroll

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:07:44.109Z — 08_mobile_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:07:50.196Z — 09_mobile_filter_retained

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:07:57.334Z — 10_mobile_active_filter

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_reset_type_0.jpg](02_mobile_reset_type_0.jpg)
- [04_mobile_choose_trial_0.jpg](04_mobile_choose_trial_0.jpg)
- [06_mobile_trial_first_0.jpg](06_mobile_trial_first_0.jpg)
- [08_mobile_metadata_0.jpg](08_mobile_metadata_0.jpg)
- [10_mobile_active_filter_0.jpg](10_mobile_active_filter_0.jpg)
