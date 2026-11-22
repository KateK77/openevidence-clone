# ME3-CUA-0321: History sort control

Status: **PASS**
Executed: 2026-11-22T07:34:31.972Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

History offers Oldest first and Newest first. Selected oldest displayed Nov20 thenNov21; selected newest displayed latest known updated thread16 first, thenNov22 andNov21 rows. Actual ordering and selected value changed.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_sort_before_0.jpg; after.png: 07_newest_order_0.jpg

## Actions

### 2026-11-22T07:33:18.045Z — 01_reset_search_desktop

```javascript
await viewport.set({width:1440,height:900}); await activeTab.reload();
```
Tool error: False

### 2026-11-22T07:33:27.215Z — 02_sort_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:33:36.426Z — 03_sort_options

```javascript
await activeTab.cua.click({x:1319,y:362}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:33:50.164Z — 04_alternate_sort

```javascript
await activeTab.cua.keypress({keys:['END']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:33:59.044Z — 05_oldest_choice

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:34:09.943Z — 06_choose_newest

```javascript
await activeTab.cua.click({x:1318,y:363}); await activeTab.cua.keypress({keys:['HOME']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:34:18.422Z — 07_newest_order

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_sort_before_0.jpg](02_sort_before_0.jpg)
- [03_sort_options_0.jpg](03_sort_options_0.jpg)
- [05_oldest_choice_0.jpg](05_oldest_choice_0.jpg)
- [07_newest_order_0.jpg](07_newest_order_0.jpg)
