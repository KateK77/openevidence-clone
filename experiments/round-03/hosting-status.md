# Free public hosting — deployment and acceptance

Verified November 15, 2026, America/Chicago (November 16 UTC in provider logs).

**Live website:** https://medevidence-ai-v3.onrender.com

Render reports deployment `dep-dbt8dam1egvs73fnjv5g` live. Public HTTPS health
returns version 3.0.0. The browser-based public acceptance run passed all 14 checks
in `public-smoke.json`, using synthetic accounts, real PostgreSQL storage and
live PubMed retrieval. No model calls or private patient data were used.

## Resources and source

- User-confirmed Render workspace: **My Workspace**.
- Service: `medevidence-ai-v3`, ID `srv-dbt8dae1egvs73fnjuf0`, **Free**, Ohio.
- Dashboard: https://dashboard.render.com/web/srv-dbt8dae1egvs73fnjuf0
- Source branch: `v3-round-03`; deployed commit:
  `e171d797069c23873c84063d6888232cf50ab7dd`.
- Hosting implementation `27d313f` passed all GitHub checks, including the
  single-service image and integration checks:
  https://github.com/KateK77/openevidence-clone/actions/runs/43803623146
- Neon organization: **Jiawen**, confirmed Free plan. Project
  `medevidence-ai-v3` (`still-glade-20792292`), `aws-us-east-2`, PostgreSQL 17,
  database `medevidence`. No local SQLite data was uploaded.
- Prior release tags and other Render services were preserved. No paid plan,
  payment method or automatic paid-model fallback was enabled.

## Public verification

Passed: registration and login after reload; Chinese terminology mapping and
live literature retrieval; answer save feedback and persistence; contained mobile
evidence table; authenticated PDF export; Unicode Markdown; known PMID lookup
and publication dates; publication collection persistence; saved preferences;
profile save and logout; answer retention after signing in again; mobile menu;
cross-account data isolation; no uncaught browser exceptions.

Recent Render application logs returned no entries at error level during the
deployment and smoke-test window. Two synthetic test accounts and their public
research fixtures remain in the isolated hosted database. No real user records
were changed. Desktop and mobile screenshots were inspected; the mobile home
capture waits for the capability notice to load.

## Remaining limit: Gemini

`generation_configured` remains false. The site currently supports literature
search, sources, history, saving and exports, but **does not yet generate AI
research answers in Chinese or another language**. The operator must privately
set `LLM_API_KEY` in the Render service's Environment page, save and deploy, then
run **Settings → Check AI connection**. The provider, compatible endpoint and
model name are already configured. Keep the key out of chat and Git.

A passed connection probe is not claim-quality acceptance. A real Chinese answer,
its source support, regeneration and live quota failures still require testing.

## Availability and persistence

The service runs independently of the owner's PC. Free Render instances can
sleep after inactivity; first access may wait for wake-up. Free-instance hours
are shared with the workspace's other free services, and provider quotas apply.
Records live in Neon rather than the disposable service filesystem. This is not
an uptime guarantee or a validated backup/restore process. New testers should
register new accounts; local accounts are not copied automatically.

The earlier repository-access error cleared after the user authorized GitHub
access and confirmed the repository was visible in Render. Creation was retried
successfully; the repository stayed private and no credential-in-URL workaround
was used. Report-only commits may skip Render deployment to avoid unnecessary
builds; the live source commit is recorded above.
