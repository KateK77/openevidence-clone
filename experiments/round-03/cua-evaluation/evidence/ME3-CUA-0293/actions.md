# ME3-CUA-0293: Original-question provenance visible

Status: **PASS**
Executed: 2026-11-22T07:15:02.245Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390px, collapsed/reopened provenance retains exact original32356626 under Original question; fields wrap within page, with no essential content clipped.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_collapse_0.jpg; after.png: 03_expand_0.jpg

## Actions

### 2026-11-22T07:14:38.334Z — 01_mobile_provenance

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:14:45.532Z — 02_collapse

```javascript
await activeTab.cua.click({x:152,y:603}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:14:55.027Z — 03_expand

```javascript
await activeTab.cua.click({x:134,y:723}); await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_provenance_0.jpg](01_mobile_provenance_0.jpg)
- [02_collapse_0.jpg](02_collapse_0.jpg)
- [03_expand_0.jpg](03_expand_0.jpg)
