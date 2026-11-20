# ME3-CUA-0010 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 390x844
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Set actual Chrome viewport to 390x844
2. open mobile menu
3. locate every research and account destination
4. close menu

## Observation

At the requested 390x844 viewport, opened the mobile drawer and visually located New research, Ask AI, Research history, Saved answers, Search PubMed, Saved publications, Settings, Profile, and the visible close button. Closing returned to the homepage; no required navigation destination was clipped and no page-wide horizontal overflow was observed.

## Action and screenshot timeline

- 2026-11-20T05:17:51.388Z — goto homepage; vp.reset(); vp.set(390,844)
- 2026-11-20T05:17:58.793Z — screenshot at 390x844
  Screenshot: `evidence/ME3-CUA-0010/0010_before.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:18:06.105Z — cua.click(28,30); screenshot; visually inspect all destinations and close control
  Screenshot: `evidence/ME3-CUA-0010/0010_menu.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:18:15.813Z — cua.click(279,28) close menu; screenshot
  Screenshot: `evidence/ME3-CUA-0010/0010_after.jpg` (original JPEG, [375, 812] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0010_before.jpg`; `after.png` is from `0010_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
