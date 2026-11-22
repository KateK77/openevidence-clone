# ME3-CUA-0470: Hosting database expiry documented

Status: **PASS**
Executed: 2026-11-22T22:52:12.742Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Followed hosting details link to docs/public-demo.md and visually read Free-tier limits and expiration. Documentation distinguishes Neon no fixed30-day expiry from observed December1 quota-cycle boundary, explicitly not database deletion date; Render sleep/quota/no uptime guarantee also stated. Documentation wording only, not an audit of database internals.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 02_hosting_settled_0.jpg; after.png: 03_expiration_policy_0.jpg

## Actions

### 2026-11-22T22:51:43.465Z — 01_linked_hosting

```javascript
await docs469.cua.click({x:306,y:426});await nodeRepl.write(await docs469.screenshot({}));await nodeRepl.write(await docs469.url());
```
Tool error: False
https://github.com/KateK77/openevidence-clone/blob/main/docs/public-demo.md

### 2026-11-22T22:51:47.287Z — 02_hosting_settled

```javascript
await nodeRepl.write(await docs469.screenshot({}));
```
Tool error: False

### 2026-11-22T22:51:57.805Z — 03_expiration_policy

```javascript
await docs469.cua.scroll({x:1290,y:743,scrollY:548,scrollX:0});await nodeRepl.write(await docs469.screenshot({}));
```
Tool error: False

## Original captures

- [01_linked_hosting_0.jpg](01_linked_hosting_0.jpg)
- [02_hosting_settled_0.jpg](02_hosting_settled_0.jpg)
- [03_expiration_policy_0.jpg](03_expiration_policy_0.jpg)
