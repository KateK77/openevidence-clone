# ME3-CUA-0033

Entered synthetic username, left password blank, clicked Sign in. Submission was rejected and focus visibly moved to the empty password field with a green focus outline. No authenticated content.



```json
[
  {
    "name": "0033_before",
    "at": "2026-11-20T07:41:37.426Z",
    "call": "await tab3.reload(); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0033_before",
    "at": "2026-11-20T07:41:37.426Z",
    "call": "await tab3.reload(); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:41:41.285Z",
    "paths": [
      "evidence/ME3-CUA-0033/0033_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0033_submit",
    "at": "2026-11-20T07:41:48.014Z",
    "call": "await tab3.cua.click({x:465,y:415}); await tab3.cua.type({text:'me3cua_20261120_0509'}); await tab3.cua.click({x:532,y:573}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0033_submit",
    "at": "2026-11-20T07:41:48.014Z",
    "call": "await tab3.cua.click({x:465,y:415}); await tab3.cua.type({text:'me3cua_20261120_0509'}); await tab3.cua.click({x:532,y:573}); await nodeRepl.write(await tab3.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T07:41:52.110Z",
    "paths": [
      "evidence/ME3-CUA-0033/0033_submit_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
