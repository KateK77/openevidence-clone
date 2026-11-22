# ME3-CUA-0086: Unsupported Chinese glossary term

Status: **FAIL**
Executed at: 2026-11-22T04:22:27.283Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Submitted verified unsupported glossary term 脊髓空洞症. New conversation /thread/11 and answer detail visibly label result Evidence gap / 0 PubMed records. Body correctly explains mapping limitation and recommends English medical keywords or PMID; says not evidence that no studies exist.

Status badge falsely presents translation limitation as Evidence gap in both conversation and answer detail, contrary to frozen expected result.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_0.jpg
- after.png from detail_open_0.jpg

## Action trace

### 2026-11-22T04:21:47.018Z — open_composer

```javascript
await tab.cua.click({x:110,y:134}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:21:57.123Z — before

```javascript
await tab.cua.click({x:683,y:674}); await tab.cua.type({text:'脊髓空洞症'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:22:05.303Z — submit

```javascript
await tab.cua.click({x:1178,y:772}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:22:12.002Z — after

```javascript
await nodeRepl.write(await tab.screenshot({})); await nodeRepl.write(await tab.url());
```
Tool error: False

https://medevidence-ai-v3.onrender.com/thread/11
### 2026-11-22T04:22:18.551Z — detail_open

```javascript
await tab.cua.click({x:400,y:646}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [detail_open_0.jpg](detail_open_0.jpg)
- [open_composer_0.jpg](open_composer_0.jpg)
- [submit_0.jpg](submit_0.jpg)
