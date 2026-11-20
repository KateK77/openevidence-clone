# ME3-CUA-0048

Both tabs showed dedicated B authenticated. After signing out tab one, tab two changed to public login and its next Research history navigation showed sign-in gate, with no protected content. Newly created second tab initially used default viewport (screenshot 1265x523); override was corrected before private navigation.

Execution setup error: second tab did not inherit required 1440x900 override during initial authenticated observation/sign-out. The full fixed-viewport scenario was not established. Protective behavior observed, but not scored PASS; no rerun to inflate results.

```json
[
  {
    "name": "0048_before",
    "at": "2026-11-20T07:59:19.197Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0048_before",
    "at": "2026-11-20T07:59:19.197Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:59:22.482Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0048_second_tab",
    "at": "2026-11-20T07:59:22.700Z",
    "call": "let tab48=await browser.tabs.new(); await tab48.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "start"
  },
  {
    "name": "0048_second_tab",
    "at": "2026-11-20T07:59:22.700Z",
    "call": "let tab48=await browser.tabs.new(); await tab48.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "end",
    "end_at": "2026-11-20T07:59:25.996Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0048_second_authenticated",
    "at": "2026-11-20T07:59:32.904Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0048_second_authenticated",
    "at": "2026-11-20T07:59:32.904Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:59:35.103Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_second_authenticated_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0048_logout_first",
    "at": "2026-11-20T07:59:35.308Z",
    "call": "await tab3.cua.click({x:360,y:834});",
    "phase": "start"
  },
  {
    "name": "0048_logout_first",
    "at": "2026-11-20T07:59:35.308Z",
    "call": "await tab3.cua.click({x:360,y:834});",
    "phase": "end",
    "end_at": "2026-11-20T07:59:38.919Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0048_first_logged_out",
    "at": "2026-11-20T07:59:48.215Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0048_first_logged_out",
    "at": "2026-11-20T07:59:48.215Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:59:58.154Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_first_logged_out_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0048_viewport_second",
    "at": "2026-11-20T08:00:02.536Z",
    "call": "await nodeRepl.write(await tab48.screenshot({})); await vp.set({width:1440,height:900});",
    "phase": "start"
  },
  {
    "name": "0048_viewport_second",
    "at": "2026-11-20T08:00:02.536Z",
    "call": "await nodeRepl.write(await tab48.screenshot({})); await vp.set({width:1440,height:900});",
    "phase": "end",
    "end_at": "2026-11-20T08:00:05.494Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_viewport_second_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0048_second_ready",
    "at": "2026-11-20T08:00:12.810Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0048_second_ready",
    "at": "2026-11-20T08:00:12.810Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T08:00:15.684Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_second_ready_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0048_private_navigation",
    "at": "2026-11-20T08:00:19.405Z",
    "call": "await tab48.cua.click({x:107,y:284});",
    "phase": "start"
  },
  {
    "name": "0048_private_navigation",
    "at": "2026-11-20T08:00:19.405Z",
    "call": "await tab48.cua.click({x:107,y:284});",
    "phase": "end",
    "end_at": "2026-11-20T08:00:21.305Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0048_after",
    "at": "2026-11-20T08:00:27.183Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0048_after",
    "at": "2026-11-20T08:00:27.183Z",
    "call": "await nodeRepl.write(await tab48.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T08:00:29.689Z",
    "paths": [
      "evidence/ME3-CUA-0048/0048_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
