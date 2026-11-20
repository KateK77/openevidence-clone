# ME3-CUA-0040

Changed Last name to CuaLast0040, saved, navigated away and returned. Exact last name persisted and First name CuaMobile0039 plus username remained unchanged. No email field exists in the available registration/profile workflow.

Frozen criterion requires unchanged email. Available synthetic account has no visible registered email and UI exposes no email for before/after comparison, so the complete assertion cannot be verified. Observed surname persistence is preserved but not scored PASS.

```json
[
  {
    "name": "0040_setup",
    "at": "2026-11-20T07:47:58.916Z",
    "call": "await vp.set({width:1440,height:900});",
    "phase": "start"
  },
  {
    "name": "0040_setup",
    "at": "2026-11-20T07:47:58.916Z",
    "call": "await vp.set({width:1440,height:900});",
    "phase": "end",
    "end_at": "2026-11-20T07:48:00.253Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0040_before",
    "at": "2026-11-20T07:48:03.225Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0040_before",
    "at": "2026-11-20T07:48:03.225Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:48:05.913Z",
    "paths": [
      "evidence/ME3-CUA-0040/0040_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0040_edit",
    "at": "2026-11-20T07:48:11.572Z",
    "call": "await tab3.cua.click({x:465,y:599}); await tab3.cua.type({text:'CuaLast0040'}); await tab3.cua.click({x:368,y:663});",
    "phase": "start"
  },
  {
    "name": "0040_edit",
    "at": "2026-11-20T07:48:11.572Z",
    "call": "await tab3.cua.click({x:465,y:599}); await tab3.cua.type({text:'CuaLast0040'}); await tab3.cua.click({x:368,y:663});",
    "phase": "end",
    "end_at": "2026-11-20T07:48:15.662Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0040_saved",
    "at": "2026-11-20T07:48:19.947Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0040_saved",
    "at": "2026-11-20T07:48:19.947Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:48:27.056Z",
    "paths": [
      "evidence/ME3-CUA-0040/0040_saved_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0040_away",
    "at": "2026-11-20T07:48:27.263Z",
    "call": "await tab3.cua.click({x:80,y:237});",
    "phase": "start"
  },
  {
    "name": "0040_away",
    "at": "2026-11-20T07:48:27.263Z",
    "call": "await tab3.cua.click({x:80,y:237});",
    "phase": "end",
    "end_at": "2026-11-20T07:48:29.144Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0040_return",
    "at": "2026-11-20T07:48:33.015Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "start"
  },
  {
    "name": "0040_return",
    "at": "2026-11-20T07:48:33.015Z",
    "call": "await tab3.cua.click({x:80,y:600});",
    "phase": "end",
    "end_at": "2026-11-20T07:48:35.425Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0040_after",
    "at": "2026-11-20T07:48:38.226Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0040_after",
    "at": "2026-11-20T07:48:38.226Z",
    "call": "await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:48:41.331Z",
    "paths": [
      "evidence/ME3-CUA-0040/0040_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
