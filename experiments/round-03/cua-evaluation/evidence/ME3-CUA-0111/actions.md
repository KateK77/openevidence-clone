# ME3-CUA-0111: Publication year start filter

Status: **PASS**
Executed: 2026-11-22T05:01:33.372Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At mobile 390x844, diabetes broad search returned 16 publications; Year 2030 returned 0 with explicit 'No publications matched this search' and 'This does not establish an absence of evidence.' Filter stayed visible with no page-wide overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_library_form_0.jpg; after.png: 10_empty_state_0.jpg

## Actions

### 2026-11-22T04:57:15.943Z — setup

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: True
Error: No tab with id: 432238160.

### 2026-11-22T04:58:00.509Z — reconnected

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:00:10.433Z — 01_reconnected_state

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:00:19.200Z — 02_mobile_navigation

```javascript
await activeTab.cua.click({x:28,y:30}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:00:26.558Z — 03_open_pubmed

```javascript
await activeTab.cua.click({x:106,y:405}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:00:36.830Z — 04_search_form

```javascript
await activeTab.cua.click({x:279,y:28}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:00:48.142Z — 05_library_recovery

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/library');
```
Tool error: False

### 2026-11-22T05:00:54.147Z — 06_library_form

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:01:00.513Z — 07_broad_search

```javascript
await activeTab.cua.click({x:172,y:505}); await activeTab.cua.type({text:'diabetes'}); await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:01:09.079Z — 08_baseline_and_year

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:98,y:644}); await activeTab.cua.type({text:'2030'}); await activeTab.cua.click({x:180,y:563});
```
Tool error: False

### 2026-11-22T05:01:18.576Z — 09_year_applied

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:350,y:790}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:01:25.319Z — 10_empty_state

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_reconnected_state_0.jpg](01_reconnected_state_0.jpg)
- [02_mobile_navigation_0.jpg](02_mobile_navigation_0.jpg)
- [03_open_pubmed_0.jpg](03_open_pubmed_0.jpg)
- [04_search_form_0.jpg](04_search_form_0.jpg)
- [06_library_form_0.jpg](06_library_form_0.jpg)
- [08_baseline_and_year_0.jpg](08_baseline_and_year_0.jpg)
- [09_year_applied_0.jpg](09_year_applied_0.jpg)
- [10_empty_state_0.jpg](10_empty_state_0.jpg)
- [reconnected_0.jpg](reconnected_0.jpg)
