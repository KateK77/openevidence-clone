# ME3-CUA-0047

Edited First name to CuaPending0047 and saved once. Captures show Unsaved changes then Saved/Changes saved successfully. Clicking the unchanged Saved control caused no visible mutation; reload preserved new first name and CuaLast0040, with No unsaved changes. In-flight saving progress was not captured.

Frozen expected result requires both progress and outcome visible. Screenshot timing captured pre-save and completed states but not in-flight progress; cannot verify or infer that assertion, and no repeat save was used to manufacture evidence.

```json
[
  {
    "name": "0047_setup_login_open",
    "at": "2026-11-20T07:57:33.622Z",
    "call": "await tab3.cua.click({x:530,y:702});",
    "phase": "start"
  },
  {
    "name": "0047_setup_login_open",
    "at": "2026-11-20T07:57:33.622Z",
    "call": "await tab3.cua.click({x:530,y:702});",
    "phase": "end",
    "end_at": "2026-11-20T07:57:37.878Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_setup_login_form",
    "at": "2026-11-20T07:57:45.839Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_setup_login_form",
    "at": "2026-11-20T07:57:45.839Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:57:48.441Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_setup_login_form_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_setup_login",
    "at": "2026-11-20T07:57:48.649Z",
    "call": "Enter dedicated synthetic B and temporary password [REDACTED]; click Sign in.",
    "phase": "start"
  },
  {
    "name": "0047_setup_login",
    "at": "2026-11-20T07:57:48.649Z",
    "call": "Enter dedicated synthetic B and temporary password [REDACTED]; click Sign in.",
    "phase": "end",
    "end_at": "2026-11-20T07:57:52.731Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_profile_open",
    "at": "2026-11-20T07:57:59.212Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "start"
  },
  {
    "name": "0047_profile_open",
    "at": "2026-11-20T07:57:59.212Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "end",
    "end_at": "2026-11-20T07:58:01.283Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_before",
    "at": "2026-11-20T07:58:07.971Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_before",
    "at": "2026-11-20T07:58:07.971Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:58:10.560Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_edit",
    "at": "2026-11-20T07:58:10.764Z",
    "call": "await tab3.cua.click({x:465,y:506}); await tab3.cua.keypress({keys:['Control','a']}); await tab3.cua.type({text:'CuaPending0047'});",
    "phase": "start"
  },
  {
    "name": "0047_edit",
    "at": "2026-11-20T07:58:10.764Z",
    "call": "await tab3.cua.click({x:465,y:506}); await tab3.cua.keypress({keys:['Control','a']}); await tab3.cua.type({text:'CuaPending0047'});",
    "phase": "end",
    "end_at": "2026-11-20T07:58:13.764Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_edited",
    "at": "2026-11-20T07:58:24.635Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_edited",
    "at": "2026-11-20T07:58:24.635Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:58:27.124Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_edited_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_save_once",
    "at": "2026-11-20T07:58:27.343Z",
    "call": "await tab3.cua.click({x:368,y:663}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_save_once",
    "at": "2026-11-20T07:58:27.343Z",
    "call": "await tab3.cua.click({x:368,y:663}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:58:30.889Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_save_once_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_result",
    "at": "2026-11-20T07:58:35.949Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_result",
    "at": "2026-11-20T07:58:35.949Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:58:39.510Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_result_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_duplicate",
    "at": "2026-11-20T07:58:45.793Z",
    "call": "await tab3.cua.click({x:368,y:663});",
    "phase": "start"
  },
  {
    "name": "0047_duplicate",
    "at": "2026-11-20T07:58:45.793Z",
    "call": "await tab3.cua.click({x:368,y:663});",
    "phase": "end",
    "end_at": "2026-11-20T07:58:51.657Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_duplicate_result",
    "at": "2026-11-20T07:58:55.919Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_duplicate_result",
    "at": "2026-11-20T07:58:55.919Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:58:58.975Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_duplicate_result_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0047_reload",
    "at": "2026-11-20T07:58:59.180Z",
    "call": "await tab3.reload();",
    "phase": "start"
  },
  {
    "name": "0047_reload",
    "at": "2026-11-20T07:58:59.180Z",
    "call": "await tab3.reload();",
    "phase": "end",
    "end_at": "2026-11-20T07:59:01.593Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0047_after",
    "at": "2026-11-20T07:59:05.280Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0047_after",
    "at": "2026-11-20T07:59:05.280Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:59:08.861Z",
    "paths": [
      "evidence/ME3-CUA-0047/0047_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
