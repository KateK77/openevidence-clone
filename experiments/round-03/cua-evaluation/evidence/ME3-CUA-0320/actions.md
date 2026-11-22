# ME3-CUA-0320: History search control

Status: **PASS**
Executed: 2026-11-22T07:33:17.803Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px entered known title fragment3355 and searched; only33551565 owned thread remains. Search term,button and result readable without overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_search_0.jpg; after.png: 03_mobile_matching_title_0.jpg

## Actions

### 2026-11-22T07:32:52.958Z — 01_mobile_search

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:33:00.816Z — 02_mobile_enter_fragment

```javascript
await activeTab.cua.click({x:139,y:370}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'3355'}); await activeTab.cua.click({x:344,y:369});
```
Tool error: False

### 2026-11-22T07:33:09.082Z — 03_mobile_matching_title

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_search_0.jpg](01_mobile_search_0.jpg)
- [03_mobile_matching_title_0.jpg](03_mobile_matching_title_0.jpg)
