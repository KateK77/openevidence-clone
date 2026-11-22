# ME3-CUA-0115: Journal filter

Status: **PASS**
Executed: 2026-11-22T05:05:32.500Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

diabetes + Journal Nature returned 16 publications. Scrolled through all 16 cards; every visible journal label was Nature. Examples PMID17167471,17167474,35296864,31802013,20432533,22616093,11742412,37648852,38538784,31142853,34012112,30651639,32814902,35614212,26633628,11742414.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_journal_before_0.jpg; after.png: 10_journal_records_page6_0.jpg

## Actions

### 2026-11-22T05:04:12.537Z — 01_desktop_journal_setup

```javascript
await viewport.set({width:1440,height:900}); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T05:04:19.731Z — 02_journal_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:686,y:577}); await activeTab.cua.type({text:'Nature'});
```
Tool error: False

### 2026-11-22T05:04:27.630Z — 03_apply_nature

```javascript
await activeTab.cua.click({x:1210,y:488});
```
Tool error: False

### 2026-11-22T05:04:35.407Z — 04_nature_result

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:715}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:04:42.493Z — 05_journal_records_page1

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:04:50.465Z — 06_journal_records_page2

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:04:56.137Z — 07_journal_records_page3

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:05:05.939Z — 08_journal_records_page4

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:05:13.077Z — 09_journal_records_page5

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:05:24.013Z — 10_journal_records_page6

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_journal_before_0.jpg](02_journal_before_0.jpg)
- [04_nature_result_0.jpg](04_nature_result_0.jpg)
- [05_journal_records_page1_0.jpg](05_journal_records_page1_0.jpg)
- [06_journal_records_page2_0.jpg](06_journal_records_page2_0.jpg)
- [07_journal_records_page3_0.jpg](07_journal_records_page3_0.jpg)
- [08_journal_records_page4_0.jpg](08_journal_records_page4_0.jpg)
- [09_journal_records_page5_0.jpg](09_journal_records_page5_0.jpg)
- [10_journal_records_page6_0.jpg](10_journal_records_page6_0.jpg)
