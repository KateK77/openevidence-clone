# ME3-CUA-0352: Unsave previously bookmarked publication

Status: **PASS**
Executed: 2026-11-22T21:40:41.588Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 removed PMID6373426 from two-bookmark list. After actual refresh list count1 shows unchanged Electronic cigarettes for smoking cessation PMID39878158; Minnesota removed. Remove/status readable and no horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_before_0.jpg; after.png: 05_mobile_refresh_0.jpg

## Actions

### 2026-11-22T21:39:34.101Z — 01_mobile_before

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:39:48.994Z — 02_mobile_top

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:40:00.766Z — 03_mobile_target_controls

```javascript
await activeTab.cua.scroll({x:215,y:699,scrollY:464,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:40:18.791Z — 04_mobile_remove

```javascript
await activeTab.cua.click({x:190,y:434}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:40:29.604Z — 05_mobile_refresh

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_before_0.jpg](01_mobile_before_0.jpg)
- [02_mobile_top_0.jpg](02_mobile_top_0.jpg)
- [03_mobile_target_controls_0.jpg](03_mobile_target_controls_0.jpg)
- [04_mobile_remove_0.jpg](04_mobile_remove_0.jpg)
- [05_mobile_refresh_0.jpg](05_mobile_refresh_0.jpg)
