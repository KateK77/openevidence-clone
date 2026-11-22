# ME3-CUA-0453: Mobile narrow keyboard focus order

Status: **PASS**
Executed: 2026-11-22T22:43:01.090Z
Requested Chrome viewport: 390x844
Tested SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Application: https://medevidence-ai-v3.onrender.com/

At 390px, Tab traversed visible drawer controls, wrapping to Close; Escape returned to menu trigger. Tab then reached account, notice, settings, composer, examples, recent items and visible footer; Shift+Tab reversed with visible outlines. No off-screen trap or horizontal clipping.



## Screenshot provenance

PNGs faithfully convert original tool-returned JPEGs without resizing/cropping/annotation. Original captures retain extension scaling and transient states. Later settled screenshots govern conclusions. Precondition-only BLOCKED cases use the same real precondition capture for before/after; no scored actions were executed in those cases.
before.png: 03_menu_open_0.jpg; after.png: 21_last_recent_0.jpg

## Actions

### 2026-11-22T22:38:09.133Z — 01_home_setup

```javascript
await activeTab.goto('https://medevidence-ai-v3.onrender.com/'); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:13.636Z — 02_menu_trigger

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:17.640Z — 03_menu_open

```javascript
await activeTab.cua.keypress({keys:['ENTER']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:29.014Z — 04_drawer_tab_1

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:32.035Z — 05_drawer_tab_2

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:35.683Z — 06_drawer_tab_3

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:39.288Z — 07_drawer_tab_4

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:42.908Z — 08_drawer_tab_5

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:46.854Z — 09_drawer_tab_6

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:50.251Z — 10_drawer_tab_7

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:53.681Z — 11_drawer_tab_8

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:38:57.491Z — 12_drawer_tab_9

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:39:01.169Z — 13_drawer_tab_10

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:41:39.171Z — 14_escape

```javascript
await activeTab.cua.keypress({keys:['ESC']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:41:50.084Z — 15_account

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:41:54.702Z — 16_notice

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:41:58.382Z — 17_settings

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:03.117Z — 18_composer

```javascript
for(let i=0;i<1;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:07.257Z — 19_examples

```javascript
for(let i=0;i<3;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:11.646Z — 20_recent

```javascript
for(let i=0;i<4;i++)await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:32.077Z — 21_last_recent

```javascript
await activeTab.cua.keypress({keys:['TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:35.268Z — 22_reverse

```javascript
await activeTab.cua.keypress({keys:['SHIFT','TAB']}); await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

### 2026-11-22T22:42:38.971Z — 23_settled

```javascript
await nodeRepl.write(await activeTab.screenshot({}));
```
Tool error: False

## Original captures

- [01_home_setup_0.jpg](01_home_setup_0.jpg)
- [02_menu_trigger_0.jpg](02_menu_trigger_0.jpg)
- [03_menu_open_0.jpg](03_menu_open_0.jpg)
- [04_drawer_tab_1_0.jpg](04_drawer_tab_1_0.jpg)
- [05_drawer_tab_2_0.jpg](05_drawer_tab_2_0.jpg)
- [06_drawer_tab_3_0.jpg](06_drawer_tab_3_0.jpg)
- [07_drawer_tab_4_0.jpg](07_drawer_tab_4_0.jpg)
- [08_drawer_tab_5_0.jpg](08_drawer_tab_5_0.jpg)
- [09_drawer_tab_6_0.jpg](09_drawer_tab_6_0.jpg)
- [10_drawer_tab_7_0.jpg](10_drawer_tab_7_0.jpg)
- [11_drawer_tab_8_0.jpg](11_drawer_tab_8_0.jpg)
- [12_drawer_tab_9_0.jpg](12_drawer_tab_9_0.jpg)
- [13_drawer_tab_10_0.jpg](13_drawer_tab_10_0.jpg)
- [14_escape_0.jpg](14_escape_0.jpg)
- [15_account_0.jpg](15_account_0.jpg)
- [16_notice_0.jpg](16_notice_0.jpg)
- [17_settings_0.jpg](17_settings_0.jpg)
- [18_composer_0.jpg](18_composer_0.jpg)
- [19_examples_0.jpg](19_examples_0.jpg)
- [20_recent_0.jpg](20_recent_0.jpg)
- [21_last_recent_0.jpg](21_last_recent_0.jpg)
- [22_reverse_0.jpg](22_reverse_0.jpg)
- [23_settled_0.jpg](23_settled_0.jpg)
