# ME3-CUA-0006 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 390x844
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Sign in with a dedicated synthetic account
2. open research home
3. locate multiline composer, examples, recent research and mode notice

## Observation

Logged into the dedicated synthetic account at the requested mobile viewport. Home shows the composer and AI mode notice; after scrolling, all three topic examples and the empty Recent conversations state are visible within the page. A screenshot-size anomaly was resolved by resetting/reapplying the viewport. A scroll command timed out but the next screenshot confirmed the actual completed scroll; no result was inferred from the timeout.

## Action and screenshot timeline

- 2026-11-20T05:10:11.274Z — goto documented /profile; screenshot
  Screenshot: `evidence/ME3-CUA-0006/0006_setup_profile.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:10:19.030Z — cua.click(360,835) sign out; vp.set(390,844); screenshot
  Screenshot: `evidence/ME3-CUA-0006/0006_before.jpg` (original JPEG, [390, 244] raster pixels).
- 2026-11-20T05:10:28.805Z — screenshot after viewport and sign out settle
  Screenshot: `evidence/ME3-CUA-0006/0006_signin_form.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:10:41.786Z — click(163,437); type synthetic username; Tab; type [credential omitted]; Tab; Enter; screenshot
  Screenshot: `evidence/ME3-CUA-0006/0006_login.jpg` (original JPEG, [390, 161] raster pixels).
- 2026-11-20T05:10:50.026Z — screenshot after login settles
  Screenshot: `evidence/ME3-CUA-0006/0006_home.jpg` (original JPEG, [375, 155] raster pixels).
- 2026-11-20T05:11:10.036Z — vp.reset(); vp.set(390,844); screenshot in subsequent call
  Screenshot: `evidence/ME3-CUA-0006/0006_home_restored.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:11:34.204Z — cua.scroll(284,681,0,564); screenshot
  Tool observation: Error: Timed out after 10000ms waiting for CDP command Input.synthesizeScrollGesture.
- 2026-11-20T05:11:51.823Z — screenshot after scroll timeout; no assumed outcome
  Screenshot: `evidence/ME3-CUA-0006/0006_scroll_recovery.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:12:06.256Z — screenshot after complete mobile inspection
  Screenshot: `evidence/ME3-CUA-0006/0006_after.jpg` (original JPEG, [375, 812] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0006_signin_form.jpg`; `after.png` is from `0006_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
