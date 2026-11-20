# ME3-CUA-0067

At 390x844 typed first line, Shift+Enter, second line. One unsent two-line draft and 56/2,000 counter remain visible, no pending/result/navigation. Both lines, action and status fit without horizontal overflow.



```json
[
  {
    "name": "0067_setup",
    "at": "2026-11-20T09:28:18.513Z",
    "call": "await tab4.reload(); await vp.set({width:390,height:844});",
    "phase": "start"
  },
  {
    "name": "0067_setup",
    "at": "2026-11-20T09:28:18.513Z",
    "call": "await tab4.reload(); await vp.set({width:390,height:844});",
    "phase": "end",
    "end_at": "2026-11-20T09:28:21.001Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0067_before",
    "at": "2026-11-20T09:28:23.872Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0067_before",
    "at": "2026-11-20T09:28:23.872Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:28:26.198Z",
    "paths": [
      "evidence/ME3-CUA-0067/0067_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0067_multiline",
    "at": "2026-11-20T09:28:30.445Z",
    "call": "await tab4.cua.click({x:160,y:344}); await tab4.cua.type({text:'Synthetic research draft 0067'}); await tab4.cua.keypress({keys:['Shift','Enter']}); await tab4.cua.type({text:'Second line remains unsent'});",
    "phase": "start"
  },
  {
    "name": "0067_multiline",
    "at": "2026-11-20T09:28:30.445Z",
    "call": "await tab4.cua.click({x:160,y:344}); await tab4.cua.type({text:'Synthetic research draft 0067'}); await tab4.cua.keypress({keys:['Shift','Enter']}); await tab4.cua.type({text:'Second line remains unsent'});",
    "phase": "end",
    "end_at": "2026-11-20T09:28:34.258Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0067_after",
    "at": "2026-11-20T09:28:38.086Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0067_after",
    "at": "2026-11-20T09:28:38.086Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:28:40.542Z",
    "paths": [
      "evidence/ME3-CUA-0067/0067_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
