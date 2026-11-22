# ME3-CUA-0310: Unknown Chinese mapping limitation provenance

Status: **PASS**
Executed: 2026-11-22T07:22:49.564Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Fresh unsupported glossary term脊髓空洞症 submitted, thread18/answer21 created. Provenance preserves original, explicitly shows No reliable mapping / unmapped Chinese terms, translation limitation not absence of studies, and no executed queries. This case scopes normalized/mapping fields; separate Evidence gap badge defect from86/87 persists and is not considered repaired.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_unmapped_term_draft_0.jpg; after.png: 10_unmapped_provenance_0.jpg

## Actions

### 2026-11-22T07:21:06.534Z — 01_new_research

```javascript
await activeTab.cua.click({x:123,y:136});
```
Tool error: False

### 2026-11-22T07:21:13.174Z — 02_home

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:21:21.175Z — 03_unmapped_term_draft

```javascript
await activeTab.cua.click({x:737,y:130}); await activeTab.cua.type({text:'脊髓空洞症'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:21:28.346Z — 04_submit

```javascript
await activeTab.cua.click({x:1191,y:226});
```
Tool error: False

### 2026-11-22T07:21:33.977Z — 05_limitation_outcome

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:21:41.748Z — 06_open_detail

```javascript
await nodeRepl.write(await activeTab.url()); await activeTab.cua.click({x:396,y:638});
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/18

### 2026-11-22T07:21:49.676Z — 07_detail_end

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/21

### 2026-11-22T07:21:57.771Z — 08_provenance_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:22:06.658Z — 09_expand_mapping

```javascript
await activeTab.cua.click({x:414,y:779}); await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:22:15.610Z — 10_unmapped_provenance

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_home_0.jpg](02_home_0.jpg)
- [03_unmapped_term_draft_0.jpg](03_unmapped_term_draft_0.jpg)
- [05_limitation_outcome_0.jpg](05_limitation_outcome_0.jpg)
- [08_provenance_control_0.jpg](08_provenance_control_0.jpg)
- [10_unmapped_provenance_0.jpg](10_unmapped_provenance_0.jpg)
