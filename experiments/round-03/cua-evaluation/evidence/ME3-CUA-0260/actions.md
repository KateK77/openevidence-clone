# ME3-CUA-0260: Source table limitations unavailable labelled

Status: **PASS**
Executed: 2026-11-22T06:53:24.973Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Opened Evidence table for owned source-backed outcome18. Limitations column explicitly says Unavailable: not extracted from the supplied abstracts; findings Unavailable: not synthesized. No fabricated study weakness presented.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_table_control_0.jpg; after.png: 04_unextracted_limitations_column_0.jpg

## Actions

### 2026-11-22T06:52:49.080Z — 01_source_table_before

```javascript
await activeTab.cua.click({x:1020,y:344}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:53:00.694Z — 02_table_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:53:08.298Z — 03_open_evidence_table

```javascript
await activeTab.cua.click({x:1330,y:314});
```
Tool error: False

### 2026-11-22T06:53:14.796Z — 04_unextracted_limitations_column

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_table_control_0.jpg](02_table_control_0.jpg)
- [04_unextracted_limitations_column_0.jpg](04_unextracted_limitations_column_0.jpg)
