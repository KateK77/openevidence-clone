# ME3-CUA-0433: Keyboard activate research example

Status: **PASS**
Executed: 2026-11-22T22:25:35.505Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Tab focuses GLP-1 example with visible outline; Enter populates research draft and moves focus to accessible composer without submission.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_composer_then_example_tab_0.jpg; after.png: 04_draft_settled_0.jpg

## Actions

### 2026-11-22T22:25:04.040Z — 01_focus_composer

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:12.558Z — 02_composer_then_example_tab

```javascript
await activeTab.cua.click({x:700,y:650}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:28.772Z — 03_enter_example

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:32.610Z — 04_draft_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_focus_composer_0.jpg](01_focus_composer_0.jpg)
- [02_composer_then_example_tab_0.jpg](02_composer_then_example_tab_0.jpg)
- [03_enter_example_0.jpg](03_enter_example_0.jpg)
- [04_draft_settled_0.jpg](04_draft_settled_0.jpg)
