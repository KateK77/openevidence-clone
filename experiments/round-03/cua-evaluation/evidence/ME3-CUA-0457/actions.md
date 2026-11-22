# ME3-CUA-0457: Mobile deep-link answer details

Status: **PASS**
Executed: 2026-11-22T22:47:15.981Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390px direct saved answer18 loaded; expanded Abstract & publication details for PMID32356626, scrolled readable metadata and source abstract with no clipping, then followed Conversation backlink to thread16 showing CUA342 synchronized thread16. No blank panel; synthesis unavailability shown honestly.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_deep_link_0.jpg; after.png: 10_conversation_settled_0.jpg

## Actions

### 2026-11-22T22:46:11.767Z — 01_deep_link

```javascript
await viewport.set({width:390,height:844});await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/18');await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:14.618Z — 02_scroll_source

```javascript
await activeTab.cua.scroll({x:345,y:710,scrollY:628,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:25.053Z — 03_excerpt_controls

```javascript
await activeTab.cua.scroll({x:345,y:710,scrollY:445,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:35.775Z — 04_expand_excerpt

```javascript
await activeTab.cua.click({x:161,y:577});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:39.155Z — 05_excerpt_scroll

```javascript
await activeTab.cua.scroll({x:343,y:718,scrollY:418,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:43.339Z — 06_return_top

```javascript
await activeTab.cua.keypress({keys:['CTRL','HOME']});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:53.773Z — 07_top_scroll

```javascript
await activeTab.cua.scroll({x:346,y:205,scrollY:-2200,scrollX:0});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:46:56.944Z — 08_top_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:47:10.919Z — 09_conversation_backlink

```javascript
await activeTab.cua.click({x:87,y:313});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:47:13.643Z — 10_conversation_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/16

## Original captures

- [01_deep_link_0.jpg](01_deep_link_0.jpg)
- [02_scroll_source_0.jpg](02_scroll_source_0.jpg)
- [03_excerpt_controls_0.jpg](03_excerpt_controls_0.jpg)
- [04_expand_excerpt_0.jpg](04_expand_excerpt_0.jpg)
- [05_excerpt_scroll_0.jpg](05_excerpt_scroll_0.jpg)
- [06_return_top_0.jpg](06_return_top_0.jpg)
- [07_top_scroll_0.jpg](07_top_scroll_0.jpg)
- [08_top_settled_0.jpg](08_top_settled_0.jpg)
- [09_conversation_backlink_0.jpg](09_conversation_backlink_0.jpg)
- [10_conversation_settled_0.jpg](10_conversation_settled_0.jpg)
