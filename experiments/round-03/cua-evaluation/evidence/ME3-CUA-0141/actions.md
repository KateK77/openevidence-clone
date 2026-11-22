# ME3-CUA-0141: Unavailable full text not implied

Status: **PASS**
Executed: 2026-11-22T05:36:44.858Z
Requested Chrome viewport: 1440x900
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

Inspected full expanded PMID6373426 card (official fixture provides abstract and no full-text link). Content explicitly headed Source abstract; controls are official PMID link and Save publication, with no Download full text or claim to have read restricted full text. Scope remains abstract/publication metadata.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 01_abstract_scope_before_0.jpg; after.png: 02_abstract_scope_and_controls_0.jpg

## Actions

### 2026-11-22T05:36:30.244Z — 01_abstract_scope_before

```javascript
await nodeRepl.write(await activeTab.screenshot({})); await activeTab.cua.click({x:1380,y:750}); await activeTab.cua.keypress({keys:['PAGEDOWN']});
```
Tool error: False

### 2026-11-22T05:36:40.767Z — 02_abstract_scope_and_controls

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_abstract_scope_before_0.jpg](01_abstract_scope_before_0.jpg)
- [02_abstract_scope_and_controls_0.jpg](02_abstract_scope_and_controls_0.jpg)
