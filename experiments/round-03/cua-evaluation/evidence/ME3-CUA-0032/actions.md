# ME3-CUA-0032

Unregistered synthetic email-shaped identity entered in the visible Username input, with arbitrary password, yielded generic Invalid username or password. No enumeration details or private content; header remains Sign in. Form labels identity as Username, not Email.



```json
[
  {
    "name": "0032_setup",
    "at": "2026-11-20T07:40:54.100Z",
    "call": "await vp.set({width:1440,height:900}); await tab3.reload();",
    "phase": "start"
  },
  {
    "name": "0032_setup",
    "at": "2026-11-20T07:40:54.100Z",
    "call": "await vp.set({width:1440,height:900}); await tab3.reload();",
    "phase": "end",
    "end_at": "2026-11-20T07:40:56.573Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0032_before",
    "at": "2026-11-20T07:41:08.045Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0032_before",
    "at": "2026-11-20T07:41:08.045Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:41:10.618Z",
    "paths": [
      "evidence/ME3-CUA-0032/0032_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0032_submit",
    "at": "2026-11-20T07:41:17.023Z",
    "call": "await tab3.cua.click({x:465,y:415}); await tab3.cua.type({text:'unregistered-me3-0032-20261120@example.invalid'}); await tab3.cua.keypress({keys:['Tab']}); await tab3.cua.type({text:'Arbitrary-0032!'}); await tab3.cua.click({x:532,y:573});",
    "phase": "start"
  },
  {
    "name": "0032_submit",
    "at": "2026-11-20T07:41:17.023Z",
    "call": "await tab3.cua.click({x:465,y:415}); await tab3.cua.type({text:'unregistered-me3-0032-20261120@example.invalid'}); await tab3.cua.keypress({keys:['Tab']}); await tab3.cua.type({text:'Arbitrary-0032!'}); await tab3.cua.click({x:532,y:573});",
    "phase": "end",
    "end_at": "2026-11-20T07:41:21.098Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0032_after",
    "at": "2026-11-20T07:41:26.609Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0032_after",
    "at": "2026-11-20T07:41:26.609Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:41:29.440Z",
    "paths": [
      "evidence/ME3-CUA-0032/0032_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
