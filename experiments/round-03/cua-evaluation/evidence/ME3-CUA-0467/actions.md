# ME3-CUA-0467: Public mobile navigation

Status: **PASS**
Executed: 2026-11-22T22:50:32.741Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390px opened hosted mobile drawer, navigated Search PubMed with readable search/filter controls, reopened menu and navigated Profile; identity, editable fields and session controls reachable via vertical scroll without horizontal clipping.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_home_0.jpg; after.png: 07_profile_scroll_0.jpg

## Actions

### 2026-11-22T22:50:01.983Z — 01_home

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:04.990Z — 02_menu

```javascript
await activeTab.cua.click({x:29,y:31});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:09.396Z — 03_pubmed

```javascript
await activeTab.cua.click({x:113,y:405});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:11.822Z — 04_pubmed_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:23.893Z — 05_reopen_menu

```javascript
await activeTab.cua.click({x:29,y:31});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:26.377Z — 06_profile

```javascript
await activeTab.cua.click({x:83,y:568});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:50:29.065Z — 07_profile_scroll

```javascript
await activeTab.cua.scroll({x:346,y:720,scrollY:300,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_home_0.jpg](01_home_0.jpg)
- [02_menu_0.jpg](02_menu_0.jpg)
- [03_pubmed_0.jpg](03_pubmed_0.jpg)
- [04_pubmed_settled_0.jpg](04_pubmed_settled_0.jpg)
- [05_reopen_menu_0.jpg](05_reopen_menu_0.jpg)
- [06_profile_0.jpg](06_profile_0.jpg)
- [07_profile_scroll_0.jpg](07_profile_scroll_0.jpg)
