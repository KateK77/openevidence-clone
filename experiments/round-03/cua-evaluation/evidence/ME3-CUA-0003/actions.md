# ME3-CUA-0003 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 1440x900
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Open homepage in signed-out state
2. locate Sign in and Register
3. activate each and return

## Observation

From the signed-out desktop homepage, Sign in opens Welcome back. Create a research account opens Create your workspace. Use an existing account returns to sign-in, and Ask AI returns to the homepage. No private research was displayed.

## Action and screenshot timeline

- 2026-11-20T05:06:59.045Z — vp.set(1440,900); screenshot
  Screenshot: `evidence/ME3-CUA-0003/0003_before.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:07:06.587Z — cua.click(1324,35); screenshot
  Screenshot: `evidence/ME3-CUA-0003/0003_signin.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:07:15.942Z — cua.click(516,636); screenshot
  Screenshot: `evidence/ME3-CUA-0003/0003_register.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:07:24.645Z — cua.click(533,702); screenshot
  Screenshot: `evidence/ME3-CUA-0003/0003_return_signin.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:07:24.645Z — cua.click(104,239); screenshot
  Screenshot: `evidence/ME3-CUA-0003/0003_after.jpg` (original JPEG, [1425, 891] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0003_before.jpg`; `after.png` is from `0003_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
