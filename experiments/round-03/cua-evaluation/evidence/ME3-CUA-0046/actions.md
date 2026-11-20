# ME3-CUA-0046

Opened account registration to prepare duplicate-email case. Entire visible form offers Username and Password only, and no synthetic account with an established email identity is available. No duplicate-username substitution or unintended account creation performed.

Required already-registered synthetic email fixture cannot be prepared through current username-only UI. Exact duplicate-email submission and rejection cannot be tested. This does not establish whether duplicate usernames are rejected.

```json
[
  {
    "name": "0046_setup",
    "at": "2026-11-20T07:57:04.579Z",
    "call": "await vp.set({width:1440,height:900}); await tab3.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "start"
  },
  {
    "name": "0046_setup",
    "at": "2026-11-20T07:57:04.579Z",
    "call": "await vp.set({width:1440,height:900}); await tab3.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "end",
    "end_at": "2026-11-20T07:57:06.672Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0046_before",
    "at": "2026-11-20T07:57:12.303Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0046_before",
    "at": "2026-11-20T07:57:12.303Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:57:14.925Z",
    "paths": [
      "evidence/ME3-CUA-0046/0046_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0046_register_open",
    "at": "2026-11-20T07:57:15.146Z",
    "call": "await tab3.cua.click({x:532,y:635});",
    "phase": "start"
  },
  {
    "name": "0046_register_open",
    "at": "2026-11-20T07:57:15.146Z",
    "call": "await tab3.cua.click({x:532,y:635});",
    "phase": "end",
    "end_at": "2026-11-20T07:57:17.308Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0046_after",
    "at": "2026-11-20T07:57:22.378Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0046_after",
    "at": "2026-11-20T07:57:22.378Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:57:24.924Z",
    "paths": [
      "evidence/ME3-CUA-0046/0046_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
