# ME3-CUA-0001 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 1440x900
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Open landing page
2. inspect logo, product name and header
3. inspect medical-use disclaimer

## Observation

Desktop landing displays MedEvidence research-workspace branding, version 3.0, and Research demonstration — not for clinical use. No OpenEvidence affiliation claim was visible.

## Action and screenshot timeline

- 2026-11-20T05:06:38.389Z — tab.goto(target); tab.screenshot({})
  Screenshot: `evidence/ME3-CUA-0001/0001_before.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:06:41.557Z — screenshot: branding and disclaimer inspected
  Screenshot: `evidence/ME3-CUA-0001/0001_after.jpg` (original JPEG, [1425, 891] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0001_before.jpg`; `after.png` is from `0001_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
