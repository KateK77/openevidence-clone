# ME3-CUA-0299: Prior-question list distinct from queries

Status: **PASS**
Executed: 2026-11-22T07:17:47.798Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Prepared two-turn thread15: second answer17 Original question B150 shown; Previous questions separately contains exact A150 first question. Executed PubMed queries separately states none recorded because unsupported mapping. This verifies context-field separation on real translation-limited outcomes; no successful retrieval/generation claimed.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_existing_two_turn_thread_0.jpg; after.png: 09_context_fields_0.jpg

## Actions

### 2026-11-22T07:16:17.876Z — 01_existing_two_turn_thread

```javascript
await viewport.set({width:1440,height:900}); await activeTab.goto('https://medevidence-ai-v3.onrender.com/thread/15'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:16:28.578Z — 02_thread_loaded

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:16:36.787Z — 03_second_turn

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:16:43.745Z — 04_second_link

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:16:52.092Z — 05_open_second

```javascript
await activeTab.cua.click({x:394,y:331}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:17:02.098Z — 06_provenance_location

```javascript
await activeTab.cua.keypress({keys:['CTRL','END']}); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/answer/17

### 2026-11-22T07:17:09.944Z — 07_provenance_closed

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:17:19.027Z — 08_expand_second_provenance

```javascript
await activeTab.cua.click({x:413,y:779}); await activeTab.cua.keypress({keys:['CTRL','END']});
```
Tool error: False

### 2026-11-22T07:17:32.073Z — 09_context_fields

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_existing_two_turn_thread_0.jpg](01_existing_two_turn_thread_0.jpg)
- [02_thread_loaded_0.jpg](02_thread_loaded_0.jpg)
- [03_second_turn_0.jpg](03_second_turn_0.jpg)
- [04_second_link_0.jpg](04_second_link_0.jpg)
- [05_open_second_0.jpg](05_open_second_0.jpg)
- [07_provenance_closed_0.jpg](07_provenance_closed_0.jpg)
- [09_context_fields_0.jpg](09_context_fields_0.jpg)
