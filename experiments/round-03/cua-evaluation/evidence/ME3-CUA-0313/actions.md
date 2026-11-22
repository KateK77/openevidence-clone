# ME3-CUA-0313: Provenance survives export

Status: **BLOCKED**
Executed: 2026-11-22T07:26:02.120Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Saved context-heavy answer20, clicked Export>Markdown, observed Markdown export downloaded. Actual downloaded file could not be opened: browser security policy rejects chrome://downloads; Ctrl+J exposed no accessible download tab.

Tool boundary prevents inspecting/retaining actual download. No bypass attempted and toast/clipboard not substituted for export contents.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 05_saved_export_before_0.jpg; after.png: 08_download_result_0.jpg

## Actions

### 2026-11-22T07:23:34.855Z — 01_context_heavy_answer

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/answer/20');
```
Tool error: False

### 2026-11-22T07:23:47.061Z — 02_export_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:23:57.824Z — 03_prepare_save

```javascript
await activeTab.cua.click({x:357,y:407});
```
Tool error: False

### 2026-11-22T07:24:07.844Z — 04_save_persistence

```javascript
await activeTab.reload();
```
Tool error: False

### 2026-11-22T07:24:16.833Z — 05_saved_export_before

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:24:27.945Z — 06_open_export

```javascript
await activeTab.cua.click({x:1331,y:407}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:24:38.331Z — 07_download_markdown

```javascript
await activeTab.cua.click({x:1292,y:456}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:25:08.811Z — 08_download_result

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T07:25:19.286Z — 09_browser_downloads

```javascript
await activeTab.cua.keypress({keys:['CTRL','j']}); await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238168","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238168\"]","url":"https://medevidence-ai-v3.onrender.com/answer/20","title":"MedEvidence AI 3.0"}]

## Original captures

- [02_export_before_0.jpg](02_export_before_0.jpg)
- [05_saved_export_before_0.jpg](05_saved_export_before_0.jpg)
- [06_open_export_0.jpg](06_open_export_0.jpg)
- [07_download_markdown_0.jpg](07_download_markdown_0.jpg)
- [08_download_result_0.jpg](08_download_result_0.jpg)
