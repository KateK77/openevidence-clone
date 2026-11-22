# ME3-CUA-0344: Saved answers and publications separate

Status: **PASS**
Executed: 2026-11-22T21:32:24.826Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At390x844 opened sidebar and visited both distinct destinations. Saved answers shows only exact baseline three response rows; Saved publications shows independently saved PMID33551565 card/title. No answer auto-created; mobile headings/actions/status readable with no horizontal overflow.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_mobile_publications_0.jpg; after.png: 05_mobile_publications_distinct_0.jpg

## Actions

### 2026-11-22T21:31:46.562Z — 01_mobile_publications

```javascript
await viewport.set({width:390,height:844}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:31:52.025Z — 02_mobile_sidebar

```javascript
await activeTab.cua.click({x:29,y:31}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:31:58.788Z — 03_mobile_answers_separate

```javascript
await activeTab.cua.click({x:116,y:324}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:08.232Z — 04_publications_navigation

```javascript
await activeTab.cua.click({x:28,y:30}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T21:32:17.129Z — 05_mobile_publications_distinct

```javascript
await activeTab.cua.click({x:128,y:447}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_mobile_publications_0.jpg](01_mobile_publications_0.jpg)
- [02_mobile_sidebar_0.jpg](02_mobile_sidebar_0.jpg)
- [03_mobile_answers_separate_0.jpg](03_mobile_answers_separate_0.jpg)
- [04_publications_navigation_0.jpg](04_publications_navigation_0.jpg)
- [05_mobile_publications_distinct_0.jpg](05_mobile_publications_distinct_0.jpg)
