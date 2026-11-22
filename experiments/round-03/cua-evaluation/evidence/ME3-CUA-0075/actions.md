# ME3-CUA-0075: Exactly 2000 characters accepted

Status: **PASS**
Executed at: 2026-11-22T04:11:25.264Z
Tested application: https://medevidence-ai-v3.onrender.com/
Tested Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Requested Chrome viewport: 1440x900

Pasted exactly 2,000 characters through clipboard; UI counter read 2000/2,000. Submitted and reached persisted research conversation with entire question ending 'foll?' and terminology-limitation outcome, without a length-validation error. No live synthesis claimed. Scroll timeout recovered by fresh screenshot; no submission repeated.



## Evidence provenance

Canonical PNGs are faithful conversions of original tool-returned JPEGs; no resizing, cropping or annotation. Capture dimensions may differ from the requested Chrome viewport because of extension scaling. Original captures are retained. Some immediate captures are stale; later settled captures are authoritative.
- before.png from before_settled_0.jpg
- after.png from recover_state_0.jpg

## Action trace

### 2026-11-22T04:09:44.748Z — setup

```javascript
await tab.cua.click({x:119,y:135}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:09:58.953Z — before

```javascript
const boundaryPrefix = '脊髓空洞症: What evidence describes treatment outcomes? '; const boundaryBody = 'This synthetic research question concerns study design, source abstracts, follow up duration and limitations. '; const q2000=(boundaryPrefix+boundaryBody.repeat(30)).slice(0,1999)+'?'; await tab.cua.click({x:649,y:674}); await tab.clipboard.writeText(q2000); await tab.cua.keypress({keys:["CTRL","v"]}); await nodeRepl.write({input:q2000,length:q2000.length}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

{"input":"脊髓空洞症: What evidence describes treatment outcomes? This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, follow up duration and limitations. This synthetic research question concerns study design, source abstracts, foll?","length":2000}
### 2026-11-22T04:10:19.730Z — before_settled

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:10:33.554Z — submitted

```javascript
await tab.cua.click({x:1174,y:770}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:10:40.368Z — after

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False
### 2026-11-22T04:10:53.301Z — outcome_status

```javascript
await tab.cua.scroll({x:1317,y:757,scrollY:683,scrollX:0}); await nodeRepl.write(await tab.screenshot({}));
```
Tool error: True

Error: Timed out after 10000ms waiting for CDP command Input.synthesizeScrollGesture.
### 2026-11-22T04:11:13.754Z — recover_state

```javascript
await nodeRepl.write(await tab.screenshot({}));
```
Tool error: False

## All original captures

- [after_0.jpg](after_0.jpg)
- [before_settled_0.jpg](before_settled_0.jpg)
- [recover_state_0.jpg](recover_state_0.jpg)
- [setup_0.jpg](setup_0.jpg)
- [submitted_0.jpg](submitted_0.jpg)
