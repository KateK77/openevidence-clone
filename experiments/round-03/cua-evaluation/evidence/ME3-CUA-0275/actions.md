# ME3-CUA-0275: Original revision metadata visible

Status: **FAIL**
Executed: 2026-11-22T07:06:27.584Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Original owned /answer/18 has stable URL and provenance shows retrieved-at timestamp11/21/2026 11:55:20PM, original query and executed queries. Inspected header and expanded provenance through page end: no Original revision/parent relationship label shown; answer creation header remains date-only.

Required original revision relationship metadata is not labelled. Retrieved-at timestamp is source retrieval time, not labelled answer creation/revision metadata.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_original_provenance_before_0.jpg; after.png: 05_no_revision_label_0.jpg

## Actions

### 2026-11-22T07:05:29.392Z — 01_original_provenance_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:423,y:780});
```
Tool error: False

### 2026-11-22T07:05:43.532Z — 02_expanded_provenance

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T07:05:52.024Z — 03_provenance_metadata

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:06:05.100Z — 04_provenance_tail

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T07:06:13.968Z — 05_no_revision_label

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/18

## Original captures

- [01_original_provenance_before_0.jpg](01_original_provenance_before_0.jpg)
- [03_provenance_metadata_0.jpg](03_provenance_metadata_0.jpg)
- [05_no_revision_label_0.jpg](05_no_revision_label_0.jpg)
