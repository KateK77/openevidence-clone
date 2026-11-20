# ME3-CUA-0002 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 390x844
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Open landing page
2. inspect logo, product name and header
3. inspect medical-use disclaimer

## Observation

At the requested 390x844 Chrome viewport, the research-only warning is visible. Opening the navigation drawer exposes MedEvidence 3.0 branding; its close control returns to the readable homepage without visible page-wide overflow.

## Action and screenshot timeline

- 2026-11-20T05:06:41.557Z — vp.set(390,844); tab.reload(); screenshot
  Screenshot: `evidence/ME3-CUA-0002/0002_before.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:06:49.628Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0002/0002_menu.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:06:59.044Z — cua.click(280,28); screenshot
  Screenshot: `evidence/ME3-CUA-0002/0002_after.jpg` (original JPEG, [375, 812] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0002_before.jpg`; `after.png` is from `0002_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
