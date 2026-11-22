# ME3-CUA-0118: Free-full-text filter

Status: **PASS**
Executed: 2026-11-22T05:09:51.729Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Enabled Free full text on diabetes; result set changed to16 records. Opened official links for first3: PMID35771962 has FREE Full text PMC,33713498 has Wiley Free Full Text plus Free article,39845881 has FREE Full text PMC/Open access. All3 sampled source records support filter; not a full16 external-link audit.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_apply_full_text_0.jpg; after.png: 11_official_third_free_article_0.jpg

## Actions

### 2026-11-22T05:08:04.058Z — 01_desktop_full_text_setup

```javascript
await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T05:08:12.615Z — 02_full_text_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:960,y:579}); await activeTab.cua.keypress({keys:['ARROWUP']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.click({x:326,y:627});
```
Tool error: False

### 2026-11-22T05:08:30.883Z — 03_apply_full_text

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:08:37.701Z — 04_full_text_results

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:710}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:08:45.790Z — 05_full_text_cards

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:08:54.140Z — 06_open_official_source

```javascript
await activeTab.cua.click({x:372,y:189});
```
Tool error: False

### 2026-11-22T05:09:00.544Z — 07_official_free_article

```javascript
const fullTextTab = await browser.tabs.get('432238169'); await nodeRepl.write(await fullTextTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:09:15.446Z — 08_return_and_second_source

```javascript
await fullTextTab.close(); await activeTab.cua.click({x:370,y:480});
```
Tool error: False

### 2026-11-22T05:09:21.403Z — 09_official_second_free_article

```javascript
const freeSecond = await browser.tabs.get('432238171'); await nodeRepl.write(await freeSecond.screenshot({}));
```
Tool error: False

### 2026-11-22T05:09:32.509Z — 10_return_and_third_source

```javascript
await freeSecond.close(); await activeTab.cua.click({x:370,y:770});
```
Tool error: False

### 2026-11-22T05:09:39.199Z — 11_official_third_free_article

```javascript
const freeThird=await browser.tabs.get('432238173'); await nodeRepl.write(await freeThird.screenshot({}));
```
Tool error: False

## Original captures

- [02_full_text_controls_0.jpg](02_full_text_controls_0.jpg)
- [03_apply_full_text_0.jpg](03_apply_full_text_0.jpg)
- [04_full_text_results_0.jpg](04_full_text_results_0.jpg)
- [05_full_text_cards_0.jpg](05_full_text_cards_0.jpg)
- [07_official_free_article_0.jpg](07_official_free_article_0.jpg)
- [09_official_second_free_article_0.jpg](09_official_second_free_article_0.jpg)
- [11_official_third_free_article_0.jpg](11_official_third_free_article_0.jpg)
