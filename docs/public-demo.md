# Public demo deployment

**[Live workspace](https://medevidence-ai-v3.onrender.com)** · **[Sign in](https://medevidence-ai-v3.onrender.com/profile)**

## Verified infrastructure

Snapshot: November 16, 2026.

| Component | Configuration |
|---|---|
| Render | medevidence-ai-v3, Docker, Free plan, Ohio |
| Git source | KateK77/openevidence-clone, deployment branch v3-round-03 |
| Application commit | c903b65ce3f8f49fe72416ca8948d215a0690a49 |
| Deployment | dep-dbtbu4p9aqoc73akvgl0, live at 08:32 UTC |
| Image | deploy/Dockerfile.hosted; React + Django/Gunicorn/WhiteNoise |
| Database | Existing Neon medevidence-ai-v3 project, PostgreSQL 17, Free plan |
| Persistence | Accounts, sessions, research snapshots, saved items and AI allowance |
| Model | Existing server-side Gemini compatible configuration; actual outcome in release report |

The default branch receives the portfolio code for readers. The existing service continues to deploy from `v3-round-03`, preserving its URL and database. Documentation-only commits can use `[skip render]`. The [new-service Blueprint](../render.yaml) follows main.

## Free-tier limits and expiration

- **Render Free web:** sleeps after 15 minutes idle; wake-up can take about a minute or longer. Free hours are shared across the workspace. Build, bandwidth, memory and compute limits apply. [Official documentation](https://render.com/docs/free).
- **Neon Free PostgreSQL:** no fixed 30-day expiration. Compute, storage and transfer quotas apply. The observed December 1, 2026 quota reset is a quota-cycle boundary, **not a database deletion date**. [Neon plans](https://neon.com/docs/introduction/plans).
- **Gemini:** the operator selected a free-tier project. Availability depends on provider/model limits. The app never enables billing or replenishes quotas.
- This release created no paid instance, expiring Render PostgreSQL trial, automatic recharge or paid native-CUA run. Free services do not provide an uptime guarantee; recheck provider terms before public events.

## Deploy another instance

1. Connect GitHub and create a Blueprint from `render.yaml`, or create a Docker web service using `deploy/Dockerfile.hosted` with context `.`.
2. Select **Free**. Supply an existing PostgreSQL URL privately as `DATABASE_URL`; the live site uses Neon. Document any trial database deletion deadline if choosing a different database.
3. Supply a private `DJANGO_SECRET_KEY`; the Blueprint generates one for a new service.
4. Set `PUBLIC_DEMO=1` to seed synthetic accounts. The Blueprint defaults `PUBLIC_DEMO_LIVE_AI=0`. Enable separately only after configuring intended provider limits. [Model setup](local-development.md).
5. Deploy. Startup disables debug, derives the trusted Render hostname, requires PostgreSQL, runs additive migrations, seeds demo accounts idempotently, and starts Gunicorn.
6. Verify health, login, known PMID lookup, saved-state reload and owner isolation. Configure `/api/health/` as the new service health-check path.

The existing service retains its previous platform health-check setting; the database-aware endpoint itself was verified over HTTPS. The Blueprint passed the published JSON schema. Render CLI validation was not run because that CLI was unavailable; the existing service was not created from this new template.

## Public AI usage controls

Live flags: `PUBLIC_DEMO=1`, `PUBLIC_DEMO_LIVE_AI=1`.

| Control | Setting / behavior |
|---|---|
| Daily allowance | 30 provider attempts per UTC day |
| Total allowance | 200 attempts; no automatic reset |
| Short-window cap | 6 calls/minute, supplemental cache-based limit |
| Output | 3000 tokens per provider response |
| Payload | At most 100,000 UTF-8 bytes in demo mode |
| Reservation | Atomic PostgreSQL row lock and increment before dispatch |
| Failed requests | Consume allowance; no automatic transport retry |
| Database errors | Fail closed, without a provider request |
| Restart | Persistent daily/total counters survive deployment |
| Exhaustion | AI stops; operator intervention needed for more allowance |

Probes, drafts, claim reviews and the optional single wrong-language correction each consume an attempt. New accounts cannot bypass the global limit. Public output is additionally clamped at 6000 tokens if an environment setting exceeds it.

These controls bound request volume; **they do not guarantee an invoice-level dollar cap**. Provider pricing, other traffic, billing tiers and in-flight charges are outside the app. Retain the intended free provider tier and monitor usage. The separate native-CUA budget remains blocked pending explicit paid approval and reliable cost controls.

## Accounts, data and operations

The [published passwords](../README.md#demo-accounts) are intentionally public demo credentials, not server secrets. Accounts are non-staff. Shared profiles cannot be modified server-side, and there is no password-change API. Seeding refuses unrelated username collisions, preserves credentials and does not overwrite research.

Welcome turns are explicitly **Synthetic demo**, without invented papers. Gallery publications were retrieved from PubMed. Other visitors can modify shared saved research, so screenshots document a moment in time. Never enter patient or confidential information.

Keep database URLs, signing secrets and provider credentials exclusively in Render Environment. Disable generation using `PUBLIC_DEMO_LIVE_AI=0`; literature features remain available after redeployment.

The only new migration adds the allowance table. Earlier rounds, tags and research remain intact. Back up PostgreSQL before operator-led rollback. Rolling back the application removes these protections; disable public live AI first. No automatic destructive reset is installed.

[Release verification, screenshots and limitations](../experiments/portfolio-release/REPORT.md).
