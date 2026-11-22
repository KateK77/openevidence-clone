# ME3-CUA-0373: Edited saved-search form can resave

Status: **PASS**
Executed: 2026-11-22T22:02:44.103Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Changed supported Year field from2024 to2023, reran real search and saved. Saved searches now contains distinct2023 and2024 diabetes/Clinical Trial/pub-date rows; current unchanged parameters show Search saved guard.

Single-year editing verified in available Year control; no claim of a separate start/end-year interval editor. Intermediate02 accidentally appended digits and was corrected before searching.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_before_year_edit_0.jpg; after.png: 06_save_edited_search_0.jpg

## Actions

### 2026-11-22T22:00:41.767Z — 01_before_year_edit

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:00:46.293Z — 02_modify_year

```javascript
await activeTab.cua.click({x:427,y:249}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.type({text:'2023'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:01:09.123Z — 03_correct_year_field

```javascript
await activeTab.cua.click({x:420,y:249}); await activeTab.cua.keypress({keys:['CTRL','a']}); await activeTab.cua.keypress({keys:['BACKSPACE']}); await activeTab.cua.type({text:'2023'}); await activeTab.cua.click({x:750,y:320}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:01:31.878Z — 04_search_edited_parameters

```javascript
await activeTab.cua.click({x:1230,y:161}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:02:01.450Z — 05_edited_result_before_save

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:02:22.635Z — 06_save_edited_search

```javascript
await activeTab.cua.click({x:1310,y:770}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_before_year_edit_0.jpg](01_before_year_edit_0.jpg)
- [02_modify_year_0.jpg](02_modify_year_0.jpg)
- [03_correct_year_field_0.jpg](03_correct_year_field_0.jpg)
- [04_search_edited_parameters_0.jpg](04_search_edited_parameters_0.jpg)
- [05_edited_result_before_save_0.jpg](05_edited_result_before_save_0.jpg)
- [06_save_edited_search_0.jpg](06_save_edited_search_0.jpg)
