# Free public test hosting

The user authorized a public test site on Render **My Workspace** and a separate
database in the Neon **Jiawen** Free organization. Existing apps and databases
belong to other projects and must not be changed. This profile supplements the
multi-service production recipe; it is intended for limited research testing.

## Deployment profile

- Render web service: Free plan, Ohio region, `v3-round-03` branch, Docker runtime,
  `deploy/Dockerfile.hosted`. Auto-deploy follows this branch.
- A single Gunicorn worker with four threads serves the built React app and API
  on the same HTTPS origin. No cross-origin cookie configuration is required.
- PostgreSQL lives in the separate Neon project `medevidence-ai-v3`, database
  `medevidence`. The account's current plan is Free; no plan change is authorized.
- Hosted startup refuses SQLite, runs migrations, and derives the exact allowed
  host and trusted HTTPS origin from Render's assigned hostname.
- The database URL, Django secret and optional Gemini key are server environment
  variables, never frontend assets or repository files.
- This single-worker profile uses an in-process cache. The shared model-call cap
  applies across its users but resets on restart. Use the Redis profile before
  adding workers or instances. User records and sessions remain in PostgreSQL.
- Local SQLite data is not transferred. Testers create new research accounts.

## Free-tier limits

Render documents idle suspension after 15 minutes and an approximately one-minute
wake-up. Its free-instance hour allowance is shared across a workspace, including
other free apps. Bandwidth and build limits also apply; these can suspend service
or produce overages if the operator has enabled billing. This deployment does
not add a payment method or upgrade a service.

Neon Free is advertised without a time limit, with compute, storage and network
quotas. Quotas and availability are not an uptime guarantee. Database inactivity
does not mean user records are deleted. Do not use an expiring Render Free
Postgres database for this deployment.

Gemini remains unconfigured until the operator supplies a Free Tier key. In the
Render service's Environment page, add `LLM_API_KEY` privately; never send the key
through a public form, report or repository. After redeployment, sign in and run
**Settings → Check AI connection**. This does not enable billing.

## Verification

Build and run `python scripts/hosted_smoke.py` locally after building the image as
`medevidence-v3-hosted:test`. It checks automatic database migration, real Gunicorn
startup, SPA deep links, asset delivery and API/asset 404 behavior on disposable
PostgreSQL. It never reads the operator's environment or calls Gemini.

Public acceptance must separately verify HTTPS, registration, secure sessions,
reload persistence, a known PubMed result, saving and account isolation. Record
the real URL and deployment result in the Round 3 hosting report. Do not call a
pending Render build a successful publication.

## References

- https://render.com/docs/free
- https://render.com/docs/deploy-django
- https://neon.com/pricing
- https://neon.com/docs/introduction/plans

Consulted November 15, 2026. Provider conditions can change.
