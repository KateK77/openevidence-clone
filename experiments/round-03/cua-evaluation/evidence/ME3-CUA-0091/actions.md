# ME3-CUA-0091: Unicode text remains readable

Status: **PASS**
Executed: 2026-11-22T04:31:55.936Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Submitted mixed Unicode question 脊髓空洞症 MRI / CSF：影像与随访？. Reopened it from Research history and then answer detail. Chinese characters, Latin MRI/CSF and punctuation remain readable without loss. Safe unmapped-term route; no synthesis asserted.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: before_0.jpg; after.png: after_0.jpg

## Actions

### 2026-11-22T04:30:46.165Z — open_composer

```javascript
await tab.cua.click({x:109,y:135}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:02.102Z — before

```javascript
await tab.cua.click({x:642,y:674}); await tab.cua.type({text:'脊髓空洞症 MRI / CSF：影像与随访？'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:13.589Z — submit

```javascript
await tab.cua.click({x:1175,y:770}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:20.597Z — conversation

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:27.125Z — history

```javascript
await tab.cua.click({x:110,y:282}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:34.282Z — reopened

```javascript
await tab.cua.click({x:608,y:433}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

### 2026-11-22T04:31:42.588Z — after

```javascript
await tab.cua.click({x:396,y:646}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## Original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [conversation_0.jpg](conversation_0.jpg)
- [history_0.jpg](history_0.jpg)
- [open_composer_0.jpg](open_composer_0.jpg)
- [reopened_0.jpg](reopened_0.jpg)
- [submit_0.jpg](submit_0.jpg)
