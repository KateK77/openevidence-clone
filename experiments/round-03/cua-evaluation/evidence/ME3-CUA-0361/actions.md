# ME3-CUA-0361: Filter saved publications by text

Status: **PASS**
Executed: 2026-11-22T21:47:23.795Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 using genuinely UI-saved three-paper fixture, unique title substring Standards of Medical Care reduces list to exact ADA PMID33551565, other owned titles hidden. Readable filter/card/status and no horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_prepare_mobile_list_0.jpg; after.png: 03_mobile_matching_result_0.jpg

## Actions

### 2026-11-22T21:47:00.635Z — 01_prepare_mobile_list

```javascript
await activeTab.cua.click({x:570,y:439}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:47:08.225Z — 02_mobile_title_filter

```javascript
await activeTab.cua.click({x:155,y:448}); await activeTab.cua.type({text:'Standards of Medical Care'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:47:15.730Z — 03_mobile_matching_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_prepare_mobile_list_0.jpg](01_prepare_mobile_list_0.jpg)
- [02_mobile_title_filter_0.jpg](02_mobile_title_filter_0.jpg)
- [03_mobile_matching_result_0.jpg](03_mobile_matching_result_0.jpg)
