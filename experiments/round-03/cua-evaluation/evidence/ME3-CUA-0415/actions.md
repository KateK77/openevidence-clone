# ME3-CUA-0415: Script-like research text inert

Status: **PASS**
Executed: 2026-11-22T22:18:33.618Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Submitted harmless <script>text</script> plus unmappedChinese CUA415 through real UI. Thread22 title/question and reopened History entry preserve literal angle-bracket markup as readable text; no unexpected navigation or visible execution.

Known unmapped-Chinese branch avoids provider calls. This tests harmless supplied script-like text, not comprehensive XSS security. Existing Evidence gap label issue remains separately recorded86/87.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_harmless_scriptlike_input_0.jpg; after.png: 06_reopened_literal_content_0.jpg

## Actions

### 2026-11-22T22:17:30.998Z — 01_scriptlike_form

```javascript
await activeTab.cua.click({x:120,y:135}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:17:43.343Z — 02_harmless_scriptlike_input

```javascript
await activeTab.cua.click({x:800,y:650}); await activeTab.cua.type({text:'<script>text</script> 脊髓空洞症 CUA415'}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:17:52.245Z — 03_submit_inert_text

```javascript
await activeTab.cua.click({x:1190,y:755}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:18:01.695Z — 04_literal_scriptlike_thread

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await nodeRepl.write(await activeTab.url());
```
Tool error: False
https://medevidence-ai-v3.onrender.com/thread/22

### 2026-11-22T22:18:12.034Z — 05_history_literal_title

```javascript
await activeTab.cua.click({x:110,y:284}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:18:30.264Z — 06_reopened_literal_content

```javascript
await activeTab.cua.click({x:620,y:432}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_scriptlike_form_0.jpg](01_scriptlike_form_0.jpg)
- [02_harmless_scriptlike_input_0.jpg](02_harmless_scriptlike_input_0.jpg)
- [03_submit_inert_text_0.jpg](03_submit_inert_text_0.jpg)
- [04_literal_scriptlike_thread_0.jpg](04_literal_scriptlike_thread_0.jpg)
- [05_history_literal_title_0.jpg](05_history_literal_title_0.jpg)
- [06_reopened_literal_content_0.jpg](06_reopened_literal_content_0.jpg)
