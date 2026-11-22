# ME3-CUA-0250: Answer identity and timestamp

Status: **FAIL**
Executed: 2026-11-22T06:44:44.902Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Opened owned answer18 from Saved answers. Original query32356626, Evidence gap outcome and bounded reason visible, but creation display only Nov21,2026. Hovering date reveals no time-of-day or fuller timestamp.

Frozen scenario requires creation time/readable timestamp; UI exposes calendar date only. Original question and recorded outcome assertions pass, timestamp assertion does not.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_saved_owned_answer_0.jpg; after.png: 05_date_hover_no_time_0.jpg

## Actions

### 2026-11-22T06:43:54.090Z — 01_open_saved_answers

```javascript
await activeTab.cua.click({x:110,y:328});
```
Tool error: False

### 2026-11-22T06:44:02.941Z — 02_saved_owned_answer

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:44:13.478Z — 03_open_owned_detail

```javascript
await activeTab.cua.click({x:619,y:360});
```
Tool error: False

### 2026-11-22T06:44:21.804Z — 04_identity_status_date

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.move({x:323,y:345});
```
Tool error: False

### 2026-11-22T06:44:29.660Z — 05_date_hover_no_time

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_saved_owned_answer_0.jpg](02_saved_owned_answer_0.jpg)
- [04_identity_status_date_0.jpg](04_identity_status_date_0.jpg)
- [05_date_hover_no_time_0.jpg](05_date_hover_no_time_0.jpg)
