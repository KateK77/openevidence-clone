# ME3-CUA-0442: Keyboard question input Shift Enter

Status: **PASS**
Executed: 2026-11-22T22:30:00.225Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Tab reaches composer; Shift+Enter produces visible second line; Enter submits safe unmapped-Chinese question and creates actual thread23 with both lines' text.

No provider calls; existing translation-status mislabel tracked separately.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_multiline_before_0.jpg; after.png: 05_submission_settled_0.jpg

## Actions

### 2026-11-22T22:29:23.348Z — 01_home_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:29:26.535Z — 02_keyboard_to_content

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['ENTER']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:29:37.704Z — 03_multiline_before

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.type({text:'脊髓空洞症 CUA442 first'}); await activeTab.cua.keypress({keys:['SHIFT','ENTER']}); await activeTab.cua.type({text:'second line'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:29:42.303Z — 04_enter_submit

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:29:45.225Z — 05_submission_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/23

## Original captures

- [01_home_setup_0.jpg](01_home_setup_0.jpg)
- [02_keyboard_to_content_0.jpg](02_keyboard_to_content_0.jpg)
- [03_multiline_before_0.jpg](03_multiline_before_0.jpg)
- [04_enter_submit_0.jpg](04_enter_submit_0.jpg)
- [05_submission_settled_0.jpg](05_submission_settled_0.jpg)
