# ME3-CUA-0473: Hosted another-user denial

Status: **BLOCKED**
Executed: 2026-11-22T22:53:50.631Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Profile confirms current synthetic accountA. No accountB switch or cross-owner URL access executed.

Two freshly registered isolated synthetic accounts/recoverable credentials unavailable. Public shared demo accounts do not satisfy the disposable account-isolation fixture; no unrelated user records accessed.

## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_account_settled_0.jpg; after.png: 02_account_settled_0.jpg

## Actions

### 2026-11-22T22:53:42.260Z — 01_account_precondition

```javascript
await activeTab.cua.click({x:96,y:602});await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:53:47.244Z — 02_account_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:53:59.125Z — 03_final_review_handoff

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/history');await viewport.reset();await activeTab.markDeliverable();await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:54:09.721Z — 04_final_review_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_account_precondition_0.jpg](01_account_precondition_0.jpg)
- [02_account_settled_0.jpg](02_account_settled_0.jpg)
- [03_final_review_handoff_0.jpg](03_final_review_handoff_0.jpg)
- [04_final_review_settled_0.jpg](04_final_review_settled_0.jpg)
