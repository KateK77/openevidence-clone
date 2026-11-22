# ME3-CUA-0087: Unsupported Chinese glossary term

Status: **FAIL**
Executed at: 2026-11-22T04:23:21.944Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 390x844

Mobile-pointer submission of verified unsupported 脊髓空洞症 created /thread/12. Conversation and answer detail show Evidence gap / 0 PubMed records alongside mapping-limitation text and actionable English keywords/PMID guidance. Requested Chrome viewport390x844; tool image375x812 preserved without resizing.

Same false Evidence gap classification as desktop. Body explicitly states this is not evidence that no studies exist.

## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_0.jpg
- after.png from detail_open_0.jpg

## Action trace

### 2026-11-22T04:22:27.525Z — mobile_setup

```javascript
await tab.cua.click({x:115,y:134}); await viewport.set({width:390,height:844}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:22:33.599Z — before

```javascript
await tab.cua.click({x:165,y:660}); await tab.cua.type({text:'脊髓空洞症'}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:22:42.477Z — submit

```javascript
await tab.cua.click({x:278,y:766}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:22:50.922Z — after

```javascript
await nodeRepl.write(await tab.screenshot({})); await nodeRepl.write(await tab.url());
```
Tool error: False

https://medevidence-ai-v3.onrender.com/
### 2026-11-22T04:22:58.312Z — retarget_submit

```javascript
await tab.cua.click({x:290,y:797}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:23:04.366Z — conversation

```javascript
await nodeRepl.write(await tab.screenshot({})); await nodeRepl.write(await tab.url());
```
Tool error: False

https://medevidence-ai-v3.onrender.com/thread/12
### 2026-11-22T04:23:13.920Z — detail_open

```javascript
await tab.cua.click({x:132,y:706}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_0.jpg](before_0.jpg)
- [conversation_0.jpg](conversation_0.jpg)
- [detail_open_0.jpg](detail_open_0.jpg)
- [mobile_setup_0.jpg](mobile_setup_0.jpg)
- [retarget_submit_0.jpg](retarget_submit_0.jpg)
- [submit_0.jpg](submit_0.jpg)
