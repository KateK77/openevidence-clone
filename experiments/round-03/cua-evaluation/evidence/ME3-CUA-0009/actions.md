# ME3-CUA-0009 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 1440x900
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Create or select an owned research answer
2. open its detail from conversation
3. return through conversation link

## Observation

Using the documented public synthetic portfolio_researcher account read-only, selected Portfolio · GLP-1 evidence review. Opened View answer and evidence from /thread/5 to /answer/5, then used Conversation to return to /thread/5 with the same title and questions. The stored answer displayed Generation unavailable; this PASS is for navigation only and makes no claim of successful synthesis. No generation, probe, regeneration, save, rename, or deletion was invoked.

## Action and screenshot timeline

- 2026-11-20T05:16:25.410Z — vp.reset(); vp.set(1440,900)
- 2026-11-20T05:16:38.443Z — screenshot
  Screenshot: `evidence/ME3-CUA-0009/0009_setup_profile.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:16:47.330Z — cua.click(360,835) sign out
- 2026-11-20T05:16:54.310Z — screenshot
  Screenshot: `evidence/ME3-CUA-0009/0009_signin_form.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:17:05.535Z — click username; type published synthetic demo username; Tab; type [published demo password omitted]; Tab; Enter
- 2026-11-20T05:17:13.404Z — screenshot after demo login
  Screenshot: `evidence/ME3-CUA-0009/0009_demo_home.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:17:20.753Z — cua.click(105,283); screenshot
  Screenshot: `evidence/ME3-CUA-0009/0009_before.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:17:28.899Z — cua.click(637,436); screenshot
  Screenshot: `evidence/ME3-CUA-0009/0009_conversation.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:17:36.249Z — record conversation URL; cua.click(401,624); screenshot; record answer URL
  Screenshot: `evidence/ME3-CUA-0009/0009_answer.jpg` (original JPEG, [1425, 891] raster pixels).
  Tool observation: https://medevidence-ai-v3.onrender.com/thread/5
  Tool observation: https://medevidence-ai-v3.onrender.com/answer/5
- 2026-11-20T05:17:44.210Z — cua.click(349,344) Conversation; screenshot; record URL
  Screenshot: `evidence/ME3-CUA-0009/0009_after.jpg` (original JPEG, [1425, 891] raster pixels).
  Tool observation: https://medevidence-ai-v3.onrender.com/thread/5

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0009_before.jpg`; `after.png` is from `0009_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.

Fixture: existing documented synthetic portfolio research thread, owned by the signed-in public demo account. Shared data was read-only; exclusive fixture ownership is not claimed.
