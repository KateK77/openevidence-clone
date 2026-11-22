# ME3-CUA-0261: Article card and table association

Status: **PASS**
Executed: 2026-11-22T06:54:12.567Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Opened source card then switched to Evidence table for same stored answer18. Both show identical Cardiovascular Disease, Drug Therapy, and Mortality in Covid-19 title, year2020 and source link labelled PMID32356626. Same sole stored source and retracted type, no neighbor substitution.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_table_identity_before_0.jpg; after.png: 06_matching_table_identity_0.jpg

## Actions

### 2026-11-22T06:53:25.221Z — 01_table_identity_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1261,y:576});
```
Tool error: False

### 2026-11-22T06:53:34.060Z — 02_card_identity

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:53:45.263Z — 03_card_link_scroll

```javascript
await activeTab.cua.click({x:1050,y:630}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T06:53:52.816Z — 04_card_title_year_pmid

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T06:54:01.426Z — 05_compare_table

```javascript
await activeTab.cua.click({x:1330,y:314});
```
Tool error: False

### 2026-11-22T06:54:09.614Z — 06_matching_table_identity

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_table_identity_before_0.jpg](01_table_identity_before_0.jpg)
- [02_card_identity_0.jpg](02_card_identity_0.jpg)
- [04_card_title_year_pmid_0.jpg](04_card_title_year_pmid_0.jpg)
- [06_matching_table_identity_0.jpg](06_matching_table_identity_0.jpg)
