# ME3-CUA-0328: History reopen retains follow-up sequence

Status: **PASS**
Executed: 2026-11-22T07:42:56.534Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Reopened three-turn/thread15 and reloaded.01 A150 then02 B150 then03 C309 retained with same saved response text,language,dates and0PubMed record association for each. Tests real translation-limited records; no nonempty-source association or generated claims inferred.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_third_before_reload_0.jpg; after.png: 07_third_retained_0.jpg

## Actions

### 2026-11-22T07:41:42.602Z — 01_open_three_turns

```javascript
await activeTab.cua.click({x:169,y:642}); await viewport.set({width:1440,height:900});
```
Tool error: False

### 2026-11-22T07:41:51.199Z — 02_first_second_turns

```javascript
await nodeRepl.write(await activeTab.url()); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/15

### 2026-11-22T07:42:03.742Z — 03_three_turn_scroll

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T07:42:12.886Z — 04_third_before_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.reload();
```
Tool error: False

### 2026-11-22T07:42:24.905Z — 05_third_after_reload

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.keypress({keys:['CTRL','HOME']});
```
Tool error: False

### 2026-11-22T07:42:38.017Z — 06_after_reload_scroll

```javascript
await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T07:42:44.819Z — 07_third_retained

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [02_first_second_turns_0.jpg](02_first_second_turns_0.jpg)
- [04_third_before_reload_0.jpg](04_third_before_reload_0.jpg)
- [05_third_after_reload_0.jpg](05_third_after_reload_0.jpg)
- [07_third_retained_0.jpg](07_third_retained_0.jpg)
