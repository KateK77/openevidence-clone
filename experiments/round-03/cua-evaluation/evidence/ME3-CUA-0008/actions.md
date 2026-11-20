# ME3-CUA-0008 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 390x844
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Sign in
2. visit Research history, Saved answers, Search PubMed, Saved publications, Settings and Profile using navigation

## Observation

After a fresh mobile login, used the drawer to visit Research history, Saved answers, Search PubMed, Saved publications, Settings, and Profile in order. Each destination opened with its own heading; relevant navigation, status, and empty-state content remained readable without observed page-wide overflow.

## Action and screenshot timeline

- 2026-11-20T05:13:59.543Z — cua.click(360,835) sign out; vp.reset(); vp.set(390,844)
- 2026-11-20T05:14:07.498Z — screenshot login form
  Screenshot: `evidence/ME3-CUA-0008/0008_before.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:14:17.699Z — click(163,437); type synthetic username; Tab; type [credential omitted]; Tab; Enter
- 2026-11-20T05:14:26.336Z — screenshot after login
  Screenshot: `evidence/ME3-CUA-0008/0008_home.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:14:33.425Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_1.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:14:42.181Z — cua.click(106,283); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_history.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:14:50.486Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_2.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:14:57.429Z — cua.click(103,325); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_answers.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:15:06.163Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_3.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:15:13.305Z — cua.click(106,405); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_pubmed.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:15:21.335Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_4.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:15:33.751Z — cua.click(113,447); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_publications.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:15:43.833Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_5.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:15:50.775Z — cua.click(87,526); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_settings.jpg` (original JPEG, [375, 812] raster pixels).
- 2026-11-20T05:15:59.630Z — cua.click(28,30); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_menu_6.jpg` (original JPEG, [390, 844] raster pixels).
- 2026-11-20T05:16:06.648Z — cua.click(83,569); screenshot
  Screenshot: `evidence/ME3-CUA-0008/0008_after.jpg` (original JPEG, [375, 812] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0008_before.jpg`; `after.png` is from `0008_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
