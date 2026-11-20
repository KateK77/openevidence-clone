# ME3-CUA-0042

At mobile viewport signed in A, opened Profile, signed out, and signed in B. Header/card identify B and B-specific first/last names; B History shows No conversations found with neither known A record. Mobile navigation and required fields/status fit without horizontal overflow.



```json
[
  {
    "name": "0042_setup_profile",
    "at": "2026-11-20T07:50:36.848Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "start"
  },
  {
    "name": "0042_setup_profile",
    "at": "2026-11-20T07:50:36.848Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "end",
    "end_at": "2026-11-20T07:50:38.883Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_setup_logout",
    "at": "2026-11-20T07:50:43.216Z",
    "call": "await tab3.cua.click({x:360,y:834}); await vp.set({width:390,height:844});",
    "phase": "start"
  },
  {
    "name": "0042_setup_logout",
    "at": "2026-11-20T07:50:43.216Z",
    "call": "await tab3.cua.click({x:360,y:834}); await vp.set({width:390,height:844});",
    "phase": "end",
    "end_at": "2026-11-20T07:50:45.366Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_before",
    "at": "2026-11-20T07:50:50.676Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_before",
    "at": "2026-11-20T07:50:50.676Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:50:52.738Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_login_A",
    "at": "2026-11-20T07:50:59.392Z",
    "call": "Enter synthetic A portfolio_researcher and demo password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0042_login_A",
    "at": "2026-11-20T07:50:59.392Z",
    "call": "Enter synthetic A portfolio_researcher and demo password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T07:51:04.611Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_A_logged",
    "at": "2026-11-20T07:51:08.859Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_A_logged",
    "at": "2026-11-20T07:51:08.859Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:51:11.211Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_A_logged_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_A_profile_open",
    "at": "2026-11-20T07:51:11.417Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "start"
  },
  {
    "name": "0042_A_profile_open",
    "at": "2026-11-20T07:51:11.417Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "end",
    "end_at": "2026-11-20T07:51:12.980Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_A_profile",
    "at": "2026-11-20T07:51:18.003Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_A_profile",
    "at": "2026-11-20T07:51:18.003Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:51:20.823Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_A_profile_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_logout_A",
    "at": "2026-11-20T07:51:21.046Z",
    "call": "await tab3.cua.click({x:79,y:726});",
    "phase": "start"
  },
  {
    "name": "0042_logout_A",
    "at": "2026-11-20T07:51:21.046Z",
    "call": "await tab3.cua.click({x:79,y:726});",
    "phase": "end",
    "end_at": "2026-11-20T07:51:23.470Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_logged_out",
    "at": "2026-11-20T07:51:30.160Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_logged_out",
    "at": "2026-11-20T07:51:30.160Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:51:32.444Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_logged_out_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_login_B",
    "at": "2026-11-20T07:51:32.660Z",
    "call": "Enter synthetic B and temporary password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0042_login_B",
    "at": "2026-11-20T07:51:32.660Z",
    "call": "Enter synthetic B and temporary password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T07:51:37.719Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_B_profile_open",
    "at": "2026-11-20T07:51:40.814Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "start"
  },
  {
    "name": "0042_B_profile_open",
    "at": "2026-11-20T07:51:40.814Z",
    "call": "await tab3.cua.click({x:300,y:31});",
    "phase": "end",
    "end_at": "2026-11-20T07:51:42.620Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_B_profile",
    "at": "2026-11-20T07:51:47.457Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_B_profile",
    "at": "2026-11-20T07:51:47.457Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:51:51.411Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_B_profile_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_menu_open",
    "at": "2026-11-20T07:51:51.612Z",
    "call": "await tab3.cua.click({x:28,y:31});",
    "phase": "start"
  },
  {
    "name": "0042_menu_open",
    "at": "2026-11-20T07:51:51.612Z",
    "call": "await tab3.cua.click({x:28,y:31});",
    "phase": "end",
    "end_at": "2026-11-20T07:51:54.470Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_menu",
    "at": "2026-11-20T07:51:57.342Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_menu",
    "at": "2026-11-20T07:51:57.342Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:51:59.452Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_menu_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0042_history_open",
    "at": "2026-11-20T07:52:05.658Z",
    "call": "await tab3.cua.click({x:110,y:282});",
    "phase": "start"
  },
  {
    "name": "0042_history_open",
    "at": "2026-11-20T07:52:05.658Z",
    "call": "await tab3.cua.click({x:110,y:282});",
    "phase": "end",
    "end_at": "2026-11-20T07:52:07.369Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0042_after",
    "at": "2026-11-20T07:52:10.204Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0042_after",
    "at": "2026-11-20T07:52:10.204Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:52:12.920Z",
    "paths": [
      "evidence/ME3-CUA-0042/0042_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
