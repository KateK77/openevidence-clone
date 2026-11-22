# ME3-CUA-0436: Mobile search filters scroll safely

Status: **PASS**
Executed: 2026-11-22T22:27:36.580Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

390px inline filters remain within viewport; year2024,typeClinical Trial and sortPublication date adjusted; native selectors close correctly and Search remains visible. Vertical scrolling does not shift page horizontally.

This build exposes inline filters, not a separate filter modal.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_search_navigation_0.jpg; after.png: 05_adjust_sort_0.jpg

## Actions

### 2026-11-22T22:26:58.286Z — 01_search_navigation

```javascript
await activeTab.cua.click({x:29,y:31}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:01.106Z — 02_search_open

```javascript
await activeTab.cua.click({x:105,y:405}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:03.860Z — 03_filters

```javascript
await activeTab.cua.scroll({x:200,y:680,scrollY:370,scrollX:0}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:14.296Z — 04_adjust_year_type

```javascript
await activeTab.cua.click({x:107,y:424}); await activeTab.cua.type({text:'2024'}); await activeTab.cua.click({x:108,y:505}); await activeTab.cua.keypress({keys:['HOME']}); await activeTab.cua.keypress({keys:['ARROWDOWN']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:27:23.528Z — 05_adjust_sort

```javascript
await activeTab.cua.click({x:263,y:505}); await activeTab.cua.keypress({keys:['END']}); await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_search_navigation_0.jpg](01_search_navigation_0.jpg)
- [02_search_open_0.jpg](02_search_open_0.jpg)
- [03_filters_0.jpg](03_filters_0.jpg)
- [04_adjust_year_type_0.jpg](04_adjust_year_type_0.jpg)
- [05_adjust_sort_0.jpg](05_adjust_sort_0.jpg)
