# ME3-CUA-0004 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 390x844
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Open homepage in signed-out state
2. locate Sign in and Register
3. activate each and return

## Observation

From the signed-out mobile homepage, Sign in opens the login form and Create a research account opens registration. Browser Back returns to the homepage. Both forms are readable and controls are within the viewport. One attempted Use an existing account click did not visibly change the form; no outcome was assumed from that click.

## Action and screenshot timeline

- 2026-11-20T05:07:34.167Z — vp.set(390,844); screenshot
  Screenshot: `evidence/ME3-CUA-0004/0004_before.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:07:34.167Z — cua.click(318,31); screenshot
  Screenshot: `evidence/ME3-CUA-0004/0004_signin.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:07:43.928Z — cua.click(187,660); screenshot
  Screenshot: `evidence/ME3-CUA-0004/0004_register.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:07:56.842Z — cua.click(181,698); screenshot
  Screenshot: `evidence/ME3-CUA-0004/0004_return_signin.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:07:56.843Z — tab.back(); screenshot
  Screenshot: `evidence/ME3-CUA-0004/0004_after.jpg` (original JPEG, [375, 812] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0004_before.jpg`; `after.png` is from `0004_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
