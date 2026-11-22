# ME3-CUA-0469: Hosting quota/idle notice

Status: **PASS**
Executed: 2026-11-22T22:51:43.214Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Followed actual app Demo accounts & usage limits link to public repository README. Visible Try the public demo section states Render Free sleeps, wake may take around a minute, availability depends on quotas and is not always-on; public provider allowance30/day and200 total described. No unlimited-uptime promise. Documentation evidence only, not hosting-internal verification.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 04_read_below_0.jpg; after.png: 05_limits_read_0.jpg

## Actions

### 2026-11-22T22:50:45.437Z — 01_notice_link

```javascript
await activeTab.cua.click({x:936,y:129});await nodeRepl.write(await activeTab.screenshot({}));await nodeRepl.write(await browser.tabs.list());
```
Tool error: False
[{"id":"432238168","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238168\"]","url":"https://medevidence-ai-v3.onrender.com/","title":"MedEvidence AI 3.0"},{"id":"432238196","providerTabId":"[\"8a19e180-9845-4231-b347-f7aeb3745c79\",\"432238196\"]","url":"https://github.com/KateK77/openevidence-clone#demo-accounts","title":"GitHub - KateK77/openevidence-clone · GitHub"}]

### 2026-11-22T22:50:54.625Z — 02_linked_notice

```javascript
let docs469=await browser.tabs.get('432238196');await nodeRepl.write(await docs469.screenshot({}));await nodeRepl.write(await docs469.url());
```
Tool error: False
https://github.com/KateK77/openevidence-clone#demo-accounts

### 2026-11-22T22:51:13.368Z — 03_find_free

```javascript
await docs469.cua.keypress({keys:['CTRL','f']});await docs469.cua.type({text:'free'});await docs469.cua.keypress({keys:['ESC']});await nodeRepl.write(await docs469.screenshot({}));
```
Tool error: False

### 2026-11-22T22:51:21.709Z — 04_read_below

```javascript
await docs469.cua.scroll({x:1036,y:740,scrollY:718,scrollX:0});await nodeRepl.write(await docs469.screenshot({}));
```
Tool error: False

### 2026-11-22T22:51:32.038Z — 05_limits_read

```javascript
await docs469.cua.scroll({x:1038,y:743,scrollY:420,scrollX:0});await nodeRepl.write(await docs469.screenshot({}));
```
Tool error: False

## Original captures

- [01_notice_link_0.jpg](01_notice_link_0.jpg)
- [04_read_below_0.jpg](04_read_below_0.jpg)
- [05_limits_read_0.jpg](05_limits_read_0.jpg)

## Publication exclusion

Two original intermediate captures (02_linked_notice,03_find_free) showed publicly posted shared-demo login credentials. They are excluded from committed evidence to comply with the frozen no-demo-credentials rule. No pixels were redacted/reconstructed. Scoring rests on genuine credential-free captures04/05 of hosting restrictions. Action calls remain in the trace.
