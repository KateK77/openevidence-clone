# ME3-CUA-0150: Question recorded chronologically

Status: **FAIL**
Executed: 2026-11-22T05:43:26.650Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Submitted two distinct safe unmapped questions A150 first question and B150 second question to same conversation/thread/15. Both outcomes persist after reload in correct01/02 order. Each card displays only Nov21,2026, with no distinct time-of-day timestamp.

Submission order works, but required distinct timestamps are not shown; both cards have identical date-only labels. No provider synthesis invoked.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_submit_first_question_0.jpg; after.png: 12_persisted_chronology_0.jpg

## Actions

### 2026-11-22T05:41:34.552Z — 01_chronology_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:41:42.568Z — 02_first_question_form

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:41:51.741Z — 03_type_first_question

```javascript
await activeTab.cua.click({x:750,y:680}); await activeTab.cua.type({text:'脊髓空洞症 A150 first question?'});
```
Tool error: False

### 2026-11-22T05:41:58.568Z — 04_submit_first_question

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1190,y:780});
```
Tool error: False

### 2026-11-22T05:42:06.214Z — 05_first_question_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:42:14.769Z — 06_followup_scroll

```javascript
await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:42:22.628Z — 07_followup_form

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:42:31.608Z — 08_second_question_input

```javascript
await activeTab.cua.click({x:710,y:669}); await activeTab.cua.type({text:'脊髓空洞症 B150 second question?'});
```
Tool error: False

### 2026-11-22T05:42:38.488Z — 09_submit_second_question

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1308,y:758});
```
Tool error: False

### 2026-11-22T05:42:46.509Z — 10_second_question_recorded

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:42:58.830Z — 11_reload_conversation

```javascript
await activeTab.reload();
```
Tool error: False

### 2026-11-22T05:43:07.954Z — 12_persisted_chronology

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/15

## Original captures

- [02_first_question_form_0.jpg](02_first_question_form_0.jpg)
- [04_submit_first_question_0.jpg](04_submit_first_question_0.jpg)
- [05_first_question_result_0.jpg](05_first_question_result_0.jpg)
- [07_followup_form_0.jpg](07_followup_form_0.jpg)
- [09_submit_second_question_0.jpg](09_submit_second_question_0.jpg)
- [10_second_question_recorded_0.jpg](10_second_question_recorded_0.jpg)
- [12_persisted_chronology_0.jpg](12_persisted_chronology_0.jpg)
