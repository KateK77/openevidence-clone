# ME3-CUA-0314: Historical queries stable after new follow-ups

Status: **PASS**
Executed: 2026-11-22T07:29:14.228Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Recorded source-backed answer18 queries32356626(1PMID),quoted32356626(0PMIDs),Retrieved at11/21/2026 11:55:20PM. Added changed-topic unsupported-Chinese follow-up C314 in thread16, then reopened original via its link. Same URL/source/query counts/time and original empty previous-context retained. Follow-up used safe unmapped branch; no model call.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 05_query_baseline_0.jpg; after.png: 16_unchanged_query_snapshot_0.jpg

## Actions

### 2026-11-22T07:26:02.374Z — 01_first_answer

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18');
```
Tool error: False

### 2026-11-22T07:26:15.558Z — 02_first_answer_bottom

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:26:29.849Z — 03_first_provenance_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:26:39.837Z — 04_expand_baseline

```javascript
await activeTab.cua.click({x:414,y:779}); await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:26:51.612Z — 05_query_baseline

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:27:03.080Z — 06_owning_thread

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/16');
```
Tool error: False

### 2026-11-22T07:27:14.874Z — 07_followup_scroll

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:27:25.345Z — 08_followup_composer

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:27:37.922Z — 09_modified_topic_draft

```javascript
await activeTab.cua.click({x:614,y:642}); await activeTab.cua.type({text:'脊髓空洞症 C314 changed topic?'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:27:53.250Z — 10_submit_followup

```javascript
await activeTab.cua.click({x:1308,y:756});
```
Tool error: False

### 2026-11-22T07:28:05.315Z — 11_followup_appended

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:28:20.948Z — 12_reopen_first

```javascript
await activeTab.cua.click({x:396,y:331});
```
Tool error: False

### 2026-11-22T07:28:29.325Z — 13_first_end

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:28:41.656Z — 14_reopened_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:28:53.664Z — 15_expand_reopened

```javascript
await activeTab.cua.click({x:414,y:779}); await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:29:01.370Z — 16_unchanged_query_snapshot

```javascript
await nodeRepl.write(await activeTab.url()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/18

## Original captures

- [03_first_provenance_control_0.jpg](03_first_provenance_control_0.jpg)
- [05_query_baseline_0.jpg](05_query_baseline_0.jpg)
- [08_followup_composer_0.jpg](08_followup_composer_0.jpg)
- [09_modified_topic_draft_0.jpg](09_modified_topic_draft_0.jpg)
- [11_followup_appended_0.jpg](11_followup_appended_0.jpg)
- [14_reopened_control_0.jpg](14_reopened_control_0.jpg)
- [16_unchanged_query_snapshot_0.jpg](16_unchanged_query_snapshot_0.jpg)
