# ME3-CUA-0035

Signed in as synthetic portfolio_researcher, opened Profile, clicked Sign out. Without reload, account header changed to Sign in and profile/session content was replaced by public login form. Sidebar links also present for anonymous users remain public navigation.



```json
[
  {
    "name": "0035_before",
    "at": "2026-11-20T07:42:36.915Z",
    "call": "await tab3.reload(); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0035_before",
    "at": "2026-11-20T07:42:36.915Z",
    "call": "await tab3.reload(); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:41.008Z",
    "paths": [
      "evidence/ME3-CUA-0035/0035_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0035_login",
    "at": "2026-11-20T07:42:46.821Z",
    "call": "Click username; type documented synthetic portfolio_researcher; Tab; type documented demo password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0035_login",
    "at": "2026-11-20T07:42:46.821Z",
    "call": "Click username; type documented synthetic portfolio_researcher; Tab; type documented demo password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T07:42:51.099Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0035_profile",
    "at": "2026-11-20T07:42:54.558Z",
    "call": "await tab3.cua.click({x:80,y:600}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0035_profile",
    "at": "2026-11-20T07:42:54.558Z",
    "call": "await tab3.cua.click({x:80,y:600}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:58.289Z",
    "paths": [
      "evidence/ME3-CUA-0035/0035_profile_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0035_profile_ready",
    "at": "2026-11-20T07:43:01.842Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0035_profile_ready",
    "at": "2026-11-20T07:43:01.842Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:43:04.569Z",
    "paths": [
      "evidence/ME3-CUA-0035/0035_profile_ready_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0035_signout",
    "at": "2026-11-20T07:43:12.023Z",
    "call": "await tab3.cua.click({x:360,y:693});",
    "phase": "start"
  },
  {
    "name": "0035_signout",
    "at": "2026-11-20T07:43:12.023Z",
    "call": "await tab3.cua.click({x:360,y:693});",
    "phase": "end",
    "end_at": "2026-11-20T07:43:20.783Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0035_after",
    "at": "2026-11-20T07:43:25.144Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0035_after",
    "at": "2026-11-20T07:43:25.144Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:43:27.696Z",
    "paths": [
      "evidence/ME3-CUA-0035/0035_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
