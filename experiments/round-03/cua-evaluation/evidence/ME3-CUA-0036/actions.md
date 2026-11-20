# ME3-CUA-0036

At mobile viewport signed in, opened Profile using account header, and selected Sign out. Without reload, header and view immediately returned to public login form; identity and session content disappeared. Required controls and states fit mobile width.



```json
[
  {
    "name": "0036_setup",
    "at": "2026-11-20T07:43:33.376Z",
    "call": "await vp.set({width:390,height:844});",
    "phase": "start"
  },
  {
    "name": "0036_setup",
    "at": "2026-11-20T07:43:33.376Z",
    "call": "await vp.set({width:390,height:844});",
    "phase": "end",
    "end_at": "2026-11-20T07:43:34.669Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0036_before",
    "at": "2026-11-20T07:43:39.063Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0036_before",
    "at": "2026-11-20T07:43:39.063Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:43:41.410Z",
    "paths": [
      "evidence/ME3-CUA-0036/0036_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0036_login",
    "at": "2026-11-20T07:43:46.178Z",
    "call": "Enter documented synthetic portfolio_researcher and demo password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0036_login",
    "at": "2026-11-20T07:43:46.178Z",
    "call": "Enter documented synthetic portfolio_researcher and demo password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T07:43:49.758Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0036_logged",
    "at": "2026-11-20T07:43:54.864Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0036_logged",
    "at": "2026-11-20T07:43:54.864Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:43:57.138Z",
    "paths": [
      "evidence/ME3-CUA-0036/0036_logged_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0036_open_profile",
    "at": "2026-11-20T07:44:00.967Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "start"
  },
  {
    "name": "0036_open_profile",
    "at": "2026-11-20T07:44:00.967Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "end",
    "end_at": "2026-11-20T07:44:03.186Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0036_profile",
    "at": "2026-11-20T07:44:06.109Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0036_profile",
    "at": "2026-11-20T07:44:06.109Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:44:08.210Z",
    "paths": [
      "evidence/ME3-CUA-0036/0036_profile_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0036_signout",
    "at": "2026-11-20T07:44:11.565Z",
    "call": "await tab3.cua.click({x:79,y:726});",
    "phase": "start"
  },
  {
    "name": "0036_signout",
    "at": "2026-11-20T07:44:11.565Z",
    "call": "await tab3.cua.click({x:79,y:726});",
    "phase": "end",
    "end_at": "2026-11-20T07:44:14.157Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0036_after",
    "at": "2026-11-20T07:44:17.005Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0036_after",
    "at": "2026-11-20T07:44:17.005Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:44:19.569Z",
    "paths": [
      "evidence/ME3-CUA-0036/0036_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
