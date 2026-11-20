# ME3-CUA-0059

Opened advertised demo instructions. README explicitly states each shared account is visible to anyone using its published credentials. Signed in public demo account; persistent banner says shared accounts are visible to other visitors and synthetic information only. No private-workspace promise observed.



```json
[
  {
    "name": "0059_setup_profile",
    "at": "2026-11-20T09:19:10.639Z",
    "call": "await tab4.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "start"
  },
  {
    "name": "0059_setup_profile",
    "at": "2026-11-20T09:19:10.639Z",
    "call": "await tab4.goto('https://medevidence-ai-v3.onrender.com/profile');",
    "phase": "end",
    "end_at": "2026-11-20T09:19:12.686Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_setup_logout",
    "at": "2026-11-20T09:19:17.754Z",
    "call": "await tab4.cua.click({x:360,y:693});",
    "phase": "start"
  },
  {
    "name": "0059_setup_logout",
    "at": "2026-11-20T09:19:17.754Z",
    "call": "await tab4.cua.click({x:360,y:693});",
    "phase": "end",
    "end_at": "2026-11-20T09:19:20.320Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_before",
    "at": "2026-11-20T09:19:24.288Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0059_before",
    "at": "2026-11-20T09:19:24.288Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:19:27.185Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_before_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0059_instructions_open",
    "at": "2026-11-20T09:19:27.385Z",
    "call": "await tab4.cua.click({x:924,y:129});",
    "phase": "start"
  },
  {
    "name": "0059_instructions_open",
    "at": "2026-11-20T09:19:27.385Z",
    "call": "await tab4.cua.click({x:924,y:129});",
    "phase": "end",
    "end_at": "2026-11-20T09:19:31.302Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_instructions",
    "at": "2026-11-20T09:19:35.868Z",
    "call": "await nodeRepl.write(await tab4.screenshot({})); await nodeRepl.write(await browser.tabs.list());",
    "phase": "start"
  },
  {
    "name": "0059_instructions",
    "at": "2026-11-20T09:19:35.868Z",
    "call": "await nodeRepl.write(await tab4.screenshot({})); await nodeRepl.write(await browser.tabs.list());",
    "phase": "end",
    "end_at": "2026-11-20T09:19:38.785Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_instructions_0.jpg"
    ],
    "error": false,
    "text": [
      "[{\"id\":\"432238140\",\"providerTabId\":\"[\\\"8a19e180-9845-4231-b347-f7aeb3745c79\\\",\\\"432238140\\\"]\",\"url\":\"https://medevidence-ai-v3.onrender.com/profile\",\"title\":\"MedEvidence AI 3.0\"},{\"id\":\"432238141\",\"providerTabId\":\"[\\\"8a19e180-9845-4231-b347-f7aeb3745c79\\\",\\\"432238141\\\"]\",\"url\":\"about:blank\",\"title\":\"about:blank\"},{\"id\":\"432238142\",\"providerTabId\":\"[\\\"8a19e180-9845-4231-b347-f7aeb3745c79\\\",\\\"432238142\\\"]\",\"url\":\"https://github.com/KateK77/openevidence-clone#demo-accounts\",\"title\":\"GitHub - KateK77/openevidence-clone · GitHub\"}]"
    ]
  },
  {
    "name": "0059_docs_select",
    "at": "2026-11-20T09:19:43.801Z",
    "call": "let demoDocs4=await browser.tabs.get('432238142'); await vp.set({width:1440,height:900});",
    "phase": "start"
  },
  {
    "name": "0059_docs_select",
    "at": "2026-11-20T09:19:43.801Z",
    "call": "let demoDocs4=await browser.tabs.get('432238142'); await vp.set({width:1440,height:900});",
    "phase": "end",
    "end_at": "2026-11-20T09:19:48.508Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_docs",
    "at": "2026-11-20T09:19:52.774Z",
    "call": "await nodeRepl.write(await demoDocs4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0059_docs",
    "at": "2026-11-20T09:19:52.774Z",
    "call": "await nodeRepl.write(await demoDocs4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:20:02.737Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_docs_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0059_docs_scroll",
    "at": "2026-11-20T09:20:13.618Z",
    "call": "await demoDocs4.cua.keypress({keys:['PageDown']}); await demoDocs4.cua.keypress({keys:['PageDown']});",
    "phase": "start"
  },
  {
    "name": "0059_docs_scroll",
    "at": "2026-11-20T09:20:13.618Z",
    "call": "await demoDocs4.cua.keypress({keys:['PageDown']}); await demoDocs4.cua.keypress({keys:['PageDown']});",
    "phase": "end",
    "end_at": "2026-11-20T09:20:18.973Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_docs_notice",
    "at": "2026-11-20T09:20:24.304Z",
    "call": "await nodeRepl.write(await demoDocs4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0059_docs_notice",
    "at": "2026-11-20T09:20:24.304Z",
    "call": "await nodeRepl.write(await demoDocs4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:20:28.123Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_docs_notice_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0059_return_login",
    "at": "2026-11-20T09:22:40.233Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0059_return_login",
    "at": "2026-11-20T09:22:40.233Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:22:48.834Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_return_login_0.jpg"
    ],
    "error": false,
    "text": []
  },
  {
    "name": "0059_signin",
    "at": "2026-11-20T09:22:53.997Z",
    "call": "CUA type public demo username and [REDACTED] password; click Sign in",
    "phase": "start"
  },
  {
    "name": "0059_signin",
    "at": "2026-11-20T09:22:53.997Z",
    "call": "CUA type public demo username and [REDACTED] password; click Sign in",
    "phase": "end",
    "end_at": "2026-11-20T09:22:58.042Z",
    "paths": [],
    "error": false,
    "text": []
  },
  {
    "name": "0059_after",
    "at": "2026-11-20T09:23:01.319Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "start"
  },
  {
    "name": "0059_after",
    "at": "2026-11-20T09:23:01.319Z",
    "call": "await nodeRepl.write(await tab4.screenshot({}));",
    "phase": "end",
    "end_at": "2026-11-20T09:23:04.432Z",
    "paths": [
      "evidence/ME3-CUA-0059/0059_after_0.jpg"
    ],
    "error": false,
    "text": []
  }
]
```
