# ME3-CUA-0053

Used two dedicated editable synthetic accounts: A=batch004, B=batch003. Saved A First name IsolatedA0053, signed in B and confirmed its original CuaPending0047 remained. Saved B as IsolatedB0053 and reloaded to confirm persistence. Signed back into A: IsolatedA0053 and blank last name remained, not B names. No shared demo profile modified.



```json
[
  {
    "name": "0053_before",
    "at": "2026-11-20T09:11:04.890Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_before",
    "at": "2026-11-20T09:11:04.890Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:11:07.822Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_edit_A",
    "at": "2026-11-20T09:11:13.015Z",
    "call": "await tab4.cua.click({x:465,y:506}); await tab4.cua.type({text:'IsolatedA0053'}); await tab4.cua.click({x:368,y:663});",
    "phase": "start"
  },
  {
    "name": "0053_edit_A",
    "at": "2026-11-20T09:11:13.015Z",
    "call": "await tab4.cua.click({x:465,y:506}); await tab4.cua.type({text:'IsolatedA0053'}); await tab4.cua.click({x:368,y:663});",
    "phase": "end",
    "end_at": "2026-11-20T09:11:21.228Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_A_saved",
    "at": "2026-11-20T09:11:25.685Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_A_saved",
    "at": "2026-11-20T09:11:25.685Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:11:28.374Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_A_saved_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_logout_A",
    "at": "2026-11-20T09:11:28.574Z",
    "call": "await tab4.cua.click({x:360,y:834});",
    "phase": "start"
  },
  {
    "name": "0053_logout_A",
    "at": "2026-11-20T09:11:28.574Z",
    "call": "await tab4.cua.click({x:360,y:834});",
    "phase": "end",
    "end_at": "2026-11-20T09:11:31.818Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_login_form",
    "at": "2026-11-20T09:11:39.073Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_login_form",
    "at": "2026-11-20T09:11:39.073Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:11:44.606Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_login_form_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_login_B",
    "at": "2026-11-20T09:11:44.844Z",
    "call": "Enter batch003 synthetic B and password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0053_login_B",
    "at": "2026-11-20T09:11:44.844Z",
    "call": "Enter batch003 synthetic B and password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T09:11:49.153Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_profile_B_open",
    "at": "2026-11-20T09:11:54.926Z",
    "call": "await tab4.cua.click({x:80,y:600});",
    "phase": "start"
  },
  {
    "name": "0053_profile_B_open",
    "at": "2026-11-20T09:11:54.926Z",
    "call": "await tab4.cua.click({x:80,y:600});",
    "phase": "end",
    "end_at": "2026-11-20T09:11:57.436Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_B_before",
    "at": "2026-11-20T09:12:03.110Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_B_before",
    "at": "2026-11-20T09:12:03.110Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:12:06.065Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_B_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_edit_B",
    "at": "2026-11-20T09:12:06.265Z",
    "call": "await tab4.cua.click({x:465,y:506}); await tab4.cua.keypress({keys:['Control','a']}); await tab4.cua.type({text:'IsolatedB0053'}); await tab4.cua.click({x:368,y:663});",
    "phase": "start"
  },
  {
    "name": "0053_edit_B",
    "at": "2026-11-20T09:12:06.265Z",
    "call": "await tab4.cua.click({x:465,y:506}); await tab4.cua.keypress({keys:['Control','a']}); await tab4.cua.type({text:'IsolatedB0053'}); await tab4.cua.click({x:368,y:663});",
    "phase": "end",
    "end_at": "2026-11-20T09:12:12.566Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_B_saved",
    "at": "2026-11-20T09:12:16.669Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_B_saved",
    "at": "2026-11-20T09:12:16.669Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:12:19.410Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_B_saved_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_B_reload",
    "at": "2026-11-20T09:12:19.619Z",
    "call": "await tab4.reload();",
    "phase": "start"
  },
  {
    "name": "0053_B_reload",
    "at": "2026-11-20T09:12:19.619Z",
    "call": "await tab4.reload();",
    "phase": "end",
    "end_at": "2026-11-20T09:12:22.174Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_B_persisted",
    "at": "2026-11-20T09:12:28.063Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_B_persisted",
    "at": "2026-11-20T09:12:28.063Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:12:30.904Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_B_persisted_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_logout_B",
    "at": "2026-11-20T09:12:31.104Z",
    "call": "await tab4.cua.click({x:360,y:834});",
    "phase": "start"
  },
  {
    "name": "0053_logout_B",
    "at": "2026-11-20T09:12:31.104Z",
    "call": "await tab4.cua.click({x:360,y:834});",
    "phase": "end",
    "end_at": "2026-11-20T09:12:33.546Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_A_login_form",
    "at": "2026-11-20T09:12:40.138Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_A_login_form",
    "at": "2026-11-20T09:12:40.138Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:12:42.946Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_A_login_form_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0053_login_A_again",
    "at": "2026-11-20T09:12:43.158Z",
    "call": "Enter batch004 synthetic A and temporary password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0053_login_A_again",
    "at": "2026-11-20T09:12:43.158Z",
    "call": "Enter batch004 synthetic A and temporary password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T09:12:47.829Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_A_reopen",
    "at": "2026-11-20T09:12:51.099Z",
    "call": "await tab4.cua.click({x:80,y:600});",
    "phase": "start"
  },
  {
    "name": "0053_A_reopen",
    "at": "2026-11-20T09:12:51.099Z",
    "call": "await tab4.cua.click({x:80,y:600});",
    "phase": "end",
    "end_at": "2026-11-20T09:12:53.213Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0053_after",
    "at": "2026-11-20T09:12:56.445Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0053_after",
    "at": "2026-11-20T09:12:56.445Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:12:59.135Z",
    "paths": [
      "evidence/ME3-CUA-0053/0053_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
