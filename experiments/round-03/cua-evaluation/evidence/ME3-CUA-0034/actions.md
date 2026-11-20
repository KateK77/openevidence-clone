# ME3-CUA-0034

Keyboard-only scored actions: Tab visibly focused Sign in, then Enter with blank password. Browser returned focus to password and displayed Please fill out this field. No pointer used within scored workflow.



```json
[
  {
    "name": "0034_before",
    "at": "2026-11-20T07:41:58.583Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0034_before",
    "at": "2026-11-20T07:41:58.583Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:01.046Z",
    "paths": [
      "evidence/ME3-CUA-0034/0034_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0034_focus",
    "at": "2026-11-20T07:42:01.271Z",
    "call": "await tab3.cua.keypress({keys:['Tab']}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0034_focus",
    "at": "2026-11-20T07:42:01.271Z",
    "call": "await tab3.cua.keypress({keys:['Tab']}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:03.929Z",
    "paths": [
      "evidence/ME3-CUA-0034/0034_focus_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0034_focus_confirm",
    "at": "2026-11-20T07:42:08.475Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0034_focus_confirm",
    "at": "2026-11-20T07:42:08.475Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:11.126Z",
    "paths": [
      "evidence/ME3-CUA-0034/0034_focus_confirm_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0034_submit",
    "at": "2026-11-20T07:42:21.389Z",
    "call": "await tab3.cua.keypress({keys:['Enter']});",
    "phase": "start"
  },
  {
    "name": "0034_submit",
    "at": "2026-11-20T07:42:21.389Z",
    "call": "await tab3.cua.keypress({keys:['Enter']});",
    "phase": "end",
    "end_at": "2026-11-20T07:42:23.667Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0034_after",
    "at": "2026-11-20T07:42:26.452Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0034_after",
    "at": "2026-11-20T07:42:26.452Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:42:29.354Z",
    "paths": [
      "evidence/ME3-CUA-0034/0034_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
