# ME3-CUA-0129: Official-source citation consistency

Status: **FAIL**
Executed: 2026-11-22T05:22:44.844Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Compared two app records via their actual official PMID links. PMID33551565 title/year2021 matched. PMID39219390 year2024 and PMID matched, but app title [Not Available]. Official PubMed displays the French title Diabète de type 2 : combler l’écart entre les évidences cliniques et la pratique.

Available official French title is replaced by [Not Available] in app; identity-field consistency fails for PMID39219390.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 08_french_identity_0.jpg; after.png: 10_french_title_official_0.jpg

## Actions

### 2026-11-22T05:21:12.862Z — 01_identity_fields_before_source

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:21:31.038Z — 02_identity_source

```javascript
await activeTab.cua.click({x:368,y:761});
```
Tool error: False

### 2026-11-22T05:21:38.527Z — 03_identity_official

```javascript
const identityTab=await browser.tabs.get('432238179'); await nodeRepl.write(await identityTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:21:45.987Z — 04_check_french_record

```javascript
await identityTab.close(); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:21:53.919Z — 05_french_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:600,y:488}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'39219390'});
```
Tool error: False

### 2026-11-22T05:22:02.605Z — 06_submit_french

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:22:10.494Z — 07_french_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:22:18.520Z — 08_french_identity

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:22:26.557Z — 09_open_french_source

```javascript
await activeTab.cua.click({x:368,y:761});
```
Tool error: False

### 2026-11-22T05:22:35.396Z — 10_french_title_official

```javascript
const frenchIdentity=await browser.tabs.get('432238181'); await nodeRepl.write(await frenchIdentity.screenshot({}));
```
Tool error: False

## Original captures

- [01_identity_fields_before_source_0.jpg](01_identity_fields_before_source_0.jpg)
- [03_identity_official_0.jpg](03_identity_official_0.jpg)
- [05_french_query_0.jpg](05_french_query_0.jpg)
- [07_french_result_0.jpg](07_french_result_0.jpg)
- [08_french_identity_0.jpg](08_french_identity_0.jpg)
- [10_french_title_official_0.jpg](10_french_title_official_0.jpg)
