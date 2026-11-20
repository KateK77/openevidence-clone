# ME3-CUA-0005 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 1440x900
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Sign in with a dedicated synthetic account
2. open research home
3. locate multiline composer, examples, recent research and mode notice

## Observation

Created a dedicated synthetic evaluation account as setup, signed it out, and logged it in for this test. Desktop home shows a multiline composer and AI synthesis configured notice. Scrolling reveals three topic examples and Recent conversations with the honest empty state Your next question starts here.

## Action and screenshot timeline

- 2026-11-20T05:09:23.278Z — cua.click(360,835) sign out; screenshot
  Screenshot: `evidence/ME3-CUA-0005/0005_before.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:09:30.264Z — screenshot after sign out
  Screenshot: `evidence/ME3-CUA-0005/0005_signin_form.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:09:40.062Z — click username; type synthetic username; Tab; type [credential omitted]; Tab; Enter; screenshot
  Screenshot: `evidence/ME3-CUA-0005/0005_login.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:09:48.918Z — screenshot after login
  Screenshot: `evidence/ME3-CUA-0005/0005_home.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:10:00.048Z — cua.scroll(1196,718,0,552); screenshot
  Screenshot: `evidence/ME3-CUA-0005/0005_after.jpg` (original JPEG, [1425, 891] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0005_signin_form.jpg`; `after.png` is from `0005_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
