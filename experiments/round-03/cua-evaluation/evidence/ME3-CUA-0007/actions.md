# ME3-CUA-0007 — visual Chrome CUA action record

Result: PASS
Application URL: https://medevidence-ai-v3.onrender.com/
Application Git SHA: c903b65ce3f8f49fe72416ca8948d215a0690a49
Frozen baseline import: 66432c918cc981e3a0e28b21df69ce4ec4ba3347
Requested CSS viewport: 1440x900
Browser: Google Chrome, connected extension (exact build not independently verified).
Controller: ChatGPT Work visual CUA; exact model ID/reasoning setting not exposed by browser runtime.

## Frozen steps

1. Sign in
2. visit Research history, Saved answers, Search PubMed, Saved publications, Settings and Profile using navigation

## Observation

After a fresh desktop login, clicked Research history, Saved answers, Search PubMed, Saved publications, Settings, and Profile in that order. Each opened its distinct page with the expected heading and, where relevant, an honest empty state.

## Action and screenshot timeline

- 2026-11-20T05:12:13.924Z — screenshot after desktop viewport and /profile navigation; cua.click(360,835) sign out
  Screenshot: `evidence/ME3-CUA-0007/0007_setup.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:12:49.085Z — screenshot login form
  Screenshot: `evidence/ME3-CUA-0007/0007_before.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:13:00.298Z — click username; type synthetic username; Tab; type [credential omitted]; Tab; Enter
- 2026-11-20T05:13:06.689Z — screenshot after login
  Screenshot: `evidence/ME3-CUA-0007/0007_home.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:13:13.695Z — cua.click(112,283); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_history.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:13:20.683Z — cua.click(108,329); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_answers.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:13:28.093Z — cua.click(103,420); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_pubmed.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:13:34.886Z — cua.click(113,465); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_publications.jpg` (original JPEG, [1440, 900] raster pixels).
- 2026-11-20T05:13:42.671Z — cua.click(87,554); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_settings.jpg` (original JPEG, [1425, 891] raster pixels).
- 2026-11-20T05:13:50.387Z — cua.click(84,598); screenshot
  Screenshot: `evidence/ME3-CUA-0007/0007_after.jpg` (original JPEG, [1425, 891] raster pixels).

## Evidence encoding

`before.png` is a pixel-preserving PNG encoding of `0007_before.jpg`; `after.png` is from `0007_after.jpg`. Original JPEG bytes are retained. No cropping, resizing, annotation, or fabricated screenshot content.
Requested CSS viewport and screenshot raster dimensions are recorded separately; the browser screenshot surface can return differing raster dimensions. Severely scaled transient captures in 0006 were retained but excluded from the acceptance decision.
