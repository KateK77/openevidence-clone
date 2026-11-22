# ME3-CUA-0324: Empty rename rejected

Status: **PASS**
Executed: 2026-11-22T07:39:18.126Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Cleared required conversation title and submitted Enter. Native readable Please fill out this field validation appeared; original title remained. Reload confirmed CUA323 mobile33551565 and original message retained, no empty title saved.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 06_validation_state_0.jpg; after.png: 08_original_retained_0.jpg

## Actions

### 2026-11-22T07:37:57.849Z — 01_empty_rename_target

```javascript
await activeTab.cua.click({x:162,y:491}); await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T07:38:05.690Z — 02_title_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:38:14.497Z — 03_open_rename

```javascript
await activeTab.cua.click({x:333,y:360});
```
Tool error: False

### 2026-11-22T07:38:21.425Z — 04_rename_input

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:38:30.953Z — 05_empty_submit

```javascript
await activeTab.cua.click({x:610,y:466}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.keypress({keys:['ENTER']});
```
Tool error: False

### 2026-11-22T07:38:45.037Z — 06_validation_state

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:38:57.728Z — 07_reload_original

```javascript
await activeTab.reload();
```
Tool error: False

### 2026-11-22T07:39:07.372Z — 08_original_retained

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_title_before_0.jpg](02_title_before_0.jpg)
- [04_rename_input_0.jpg](04_rename_input_0.jpg)
- [06_validation_state_0.jpg](06_validation_state_0.jpg)
- [08_original_retained_0.jpg](08_original_retained_0.jpg)
