# ME3-CUA-0351: Unsave previously bookmarked publication

Status: **PASS**
Executed: 2026-11-22T21:39:33.466Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Removed independently saved PMID33551565; matching filter becomes explicit no saved publications, total2. Browser refresh resets filter and shows remaining Minnesota6373426 and Electronic-cigarettes39878158 records; removed ADA record absent. No confirmation shown.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_desktop_saved_list_0.jpg; after.png: 06_other_publication_retained_0.jpg

## Actions

### 2026-11-22T21:38:29.784Z — 01_desktop_saved_list

```javascript
await viewport.set({width:1440,height:900}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:38:37.247Z — 02_desktop_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:38:46.047Z — 03_remove_publication

```javascript
await activeTab.cua.click({x:616,y:703}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:38:58.097Z — 04_remove_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:39:11.699Z — 05_refresh_removed

```javascript
await activeTab.reload(); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:39:20.805Z — 06_other_publication_retained

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_desktop_saved_list_0.jpg](01_desktop_saved_list_0.jpg)
- [02_desktop_settled_0.jpg](02_desktop_settled_0.jpg)
- [03_remove_publication_0.jpg](03_remove_publication_0.jpg)
- [04_remove_settled_0.jpg](04_remove_settled_0.jpg)
- [05_refresh_removed_0.jpg](05_refresh_removed_0.jpg)
- [06_other_publication_retained_0.jpg](06_other_publication_retained_0.jpg)
