# ME3-CUA-0211: Source abstracts do not translate

Status: **PASS**
Executed: 2026-11-22T06:32:44.528Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Saved Chinese preference from203/204 remains active. At390x844 opened real PubMed PMID6373426 title and expanded original abstract, read by vertical scrolling through its ending. English source title/abstract and PMID retained; controls and full source body readable without page-wide horizontal overflow. No synthesis invoked.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_source_before_0.jpg; after.png: 06_mobile_original_abstract_tail_0.jpg

## Actions

### 2026-11-22T06:31:49.535Z — 01_mobile_source_setup

```javascript
await viewport.set({width:390,height:844}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T06:32:02.482Z — 02_mobile_source_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:32:11.697Z — 03_mobile_read_source

```javascript
await activeTab.cua.click({x:350,y:365}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:32:24.787Z — 04_mobile_english_title

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:32:32.180Z — 05_mobile_abstract_scroll

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:32:40.231Z — 06_mobile_original_abstract_tail

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_source_before_0.jpg](02_mobile_source_before_0.jpg)
- [04_mobile_english_title_0.jpg](04_mobile_english_title_0.jpg)
- [06_mobile_original_abstract_tail_0.jpg](06_mobile_original_abstract_tail_0.jpg)
