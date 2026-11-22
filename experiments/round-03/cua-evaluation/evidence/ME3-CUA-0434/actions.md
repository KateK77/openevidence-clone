# ME3-CUA-0434: Keyboard activate research example

Status: **PASS**
Executed: 2026-11-22T22:26:15.089Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Keyboard-only clearing draft, Tab to examples and Space on SGLT2 example populates correct 57-character question with composer focused; no auto-submit.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_example_focus_settled_0.jpg; after.png: 04_draft_settled_0.jpg

## Actions

### 2026-11-22T22:25:35.744Z — 01_keyboard_draft_clear

```javascript
await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:47.258Z — 02_example_focus_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:55.372Z — 03_space_example

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['SPACE']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:25:58.707Z — 04_draft_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_keyboard_draft_clear_0.jpg](01_keyboard_draft_clear_0.jpg)
- [02_example_focus_settled_0.jpg](02_example_focus_settled_0.jpg)
- [03_space_example_0.jpg](03_space_example_0.jpg)
- [04_draft_settled_0.jpg](04_draft_settled_0.jpg)
