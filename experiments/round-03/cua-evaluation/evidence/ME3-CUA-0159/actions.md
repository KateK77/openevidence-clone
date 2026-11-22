# ME3-CUA-0159: Source snapshot discoverable

Status: **PASS**
Executed: 2026-11-22T05:57:31.772Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared an owned saved excluded-source outcome using verified retracted PMID32356626, with no eligible abstracts for generation. Reopened it from Saved answers (/answer/18), expanded publication details and retrieval provenance: original abstract, PMID/DOI, original/normalized question, bare query1 PMID and quoted query0 PMIDs are inspectable. Saved state persisted across navigation. This tests retrieved-source persistence, not accepted AI synthesis.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 16_saved_fixture_ready_0.jpg; after.png: 24_source_provenance_visible_0.jpg

## Actions

### 2026-11-22T05:53:54.594Z — 01_prepare_retracted_source

```javascript
await activeTab.cua.click({x:600,y:487}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'32418117'}); await activeTab.cua.click({x:1200,y:487});
```
Tool error: False

### 2026-11-22T05:54:03.942Z — 02_candidate_record

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:54:15.806Z — 03_correct_source_identifier

```javascript
await activeTab.cua.click({x:620,y:460}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'32356626'}); await activeTab.cua.click({x:1220,y:460});
```
Tool error: False

### 2026-11-22T05:54:26.138Z — 04_retracted_lookup

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1390,y:770}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:54:33.751Z — 05_retracted_card

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:54:41.382Z — 06_verify_second_planned_query

```javascript
await activeTab.cua.click({x:600,y:272}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'"32356626"'}); await activeTab.cua.click({x:1220,y:272});
```
Tool error: False

### 2026-11-22T05:54:50.476Z — 07_zero_second_query

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:115,y:135});
```
Tool error: False

### 2026-11-22T05:55:02.609Z — 08_prepare_composer

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:55:18.321Z — 09_create_excluded_source_fixture

```javascript
await activeTab.cua.click({x:650,y:680}); await activeTab.cua.type({text:'32356626'}); await activeTab.cua.click({x:1190,y:780});
```
Tool error: False

### 2026-11-22T05:55:27.220Z — 10_fixture_outcome

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:55:33.592Z — 11_open_persisted_answer

```javascript
await nodeRepl.write(await activeTab.url()); await activeTab.cua.click({x:397,y:618});
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/16

### 2026-11-22T05:55:40.393Z — 12_answer_detail_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:55:49.003Z — 13_save_fixture_and_scroll

```javascript
await activeTab.cua.click({x:353,y:401}); await activeTab.cua.click({x:1390,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:55:56.338Z — 14_source_snapshot

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:56:05.119Z — 15_open_saved_list

```javascript
await activeTab.cua.click({x:108,y:325});
```
Tool error: False

### 2026-11-22T05:56:11.285Z — 16_saved_fixture_ready

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:56:17.314Z — 17_scored_open_saved_answer

```javascript
await activeTab.cua.click({x:645,y:367});
```
Tool error: False

### 2026-11-22T05:56:23.759Z — 18_saved_answer_persisted

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1390,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:56:32.849Z — 19_persisted_source_card

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:422,y:596});
```
Tool error: False

### 2026-11-22T05:56:41.836Z — 20_expanded_source

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1390,y:760}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:56:50.223Z — 21_abstract_middle

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:56:59.250Z — 22_provenance_control

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T05:57:06.715Z — 23_expand_provenance

```javascript
await activeTab.cua.click({x:404,y:758}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:57:12.729Z — 24_source_provenance_visible

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/18

## Original captures

- [02_candidate_record_0.jpg](02_candidate_record_0.jpg)
- [04_retracted_lookup_0.jpg](04_retracted_lookup_0.jpg)
- [05_retracted_card_0.jpg](05_retracted_card_0.jpg)
- [07_zero_second_query_0.jpg](07_zero_second_query_0.jpg)
- [08_prepare_composer_0.jpg](08_prepare_composer_0.jpg)
- [10_fixture_outcome_0.jpg](10_fixture_outcome_0.jpg)
- [12_answer_detail_before_0.jpg](12_answer_detail_before_0.jpg)
- [14_source_snapshot_0.jpg](14_source_snapshot_0.jpg)
- [16_saved_fixture_ready_0.jpg](16_saved_fixture_ready_0.jpg)
- [18_saved_answer_persisted_0.jpg](18_saved_answer_persisted_0.jpg)
- [19_persisted_source_card_0.jpg](19_persisted_source_card_0.jpg)
- [20_expanded_source_0.jpg](20_expanded_source_0.jpg)
- [21_abstract_middle_0.jpg](21_abstract_middle_0.jpg)
- [22_provenance_control_0.jpg](22_provenance_control_0.jpg)
- [24_source_provenance_visible_0.jpg](24_source_provenance_visible_0.jpg)
