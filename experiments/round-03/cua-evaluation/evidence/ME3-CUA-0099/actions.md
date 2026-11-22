# ME3-CUA-0099: Keyword PubMed search

Status: **PASS**
Executed: 2026-11-22T04:36:36.530Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Mobile: entered diabetes and submitted Search PubMed;16 publications. First two cards show complete wrapped titles,2022 dates, metadata, PMID35771962 and35146976 links. Results/control widths fit; page scrolling reveals required links without horizontal overflow. Requested390x844; original scaled capture retained.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:35:40.026Z — setup

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:46.081Z — top

```javascript
await tab.cua.keypress({keys:['CTRL','HOME']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:35:54.329Z — before

```javascript
await tab.cua.click({x:170,y:507}); await tab.cua.keypress({keys:['CTRL','a']}); await tab.cua.type({text:'diabetes'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:36:09.126Z — submit

```javascript
await tab.cua.click({x:180,y:563}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:36:17.423Z — list

```javascript
await tab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:36:23.622Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [list_0.jpg](list_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submit_0.jpg](submit_0.jpg)
- [top_0.jpg](top_0.jpg)
