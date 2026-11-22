# ME3-CUA-0142: Unavailable full text not implied

Status: **PASS**
Executed: 2026-11-22T05:37:12.829Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 inspected expanded PMID6373426 and scrolled through its source abstract to bottom controls. Source abstract heading explicitly limits scope; only official PMID link/Save publication shown, no full-text Download or read-full-text claim. Long abstract wraps within mobile page without horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_mobile_open_card_0.jpg; after.png: 04_mobile_abstract_and_controls_0.jpg

## Actions

### 2026-11-22T05:36:45.099Z — 01_mobile_abstract_scope_setup

```javascript
await viewport.set({width:390,height:844});
```
Tool error: False

### 2026-11-22T05:36:51.796Z — 02_mobile_open_card

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:37:00.399Z — 03_mobile_scope_scroll

```javascript
await activeTab.cua.click({x:350,y:780}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:37:09.180Z — 04_mobile_abstract_and_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_mobile_open_card_0.jpg](02_mobile_open_card_0.jpg)
- [04_mobile_abstract_and_controls_0.jpg](04_mobile_abstract_and_controls_0.jpg)
