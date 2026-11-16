# Long-running research test deployment

For the verified public Render + Neon portfolio site, use [Public demo deployment](public-demo.md). This page describes the separate self-managed multi-service option.

The local `127.0.0.1:5173` address is available only on the computer running it.
A GitHub repository stores source code; it does not run this Django application.
To let testers visit independently of the owner's PC, use an always-on Linux
server with Docker Compose and a domain pointing to it. This repository includes
a self-managed deployment recipe; no always-on paid server was provisioned. The separate free public Render site is linked above.

## Services and persistence

`compose.yaml` runs Caddy (HTTPS and the built React application), Gunicorn/Django,
PostgreSQL and Redis. Only Caddy exposes ports. Django sessions and research data
persist in PostgreSQL. Redis shares cache and model-call limits between workers.
The default limit is 12 model calls per minute across users, not a guarantee of
matching a provider's free tier. Each generated answer normally needs two calls
(generation and claim review); a language retry can require a third.

Model keys remain server-side. Testers register separate accounts; they do not
need the owner's Gemini key. All tester calls share the configured Gemini project
quota. Verify the project's Free billing tier in Google AI Studio. The application
cannot verify billing status or promise zero charges on an already billed project.
It never enables billing or switches to a paid model when quota is exhausted.
Free hosting can sleep or have persistence limits. Choose hosting intentionally.

## Operator procedure

1. Provision a Linux host, point a domain's DNS to it, and allow inbound ports
   80 and 443. Install Docker with the Compose plugin.
2. Check out the release. Copy `deploy/production.env.example` to
   `.env.production` in the repository root, fill the domain and secrets, and
   restrict that file to the operator (`chmod 600 .env.production`). Use a long
   random hexadecimal database password so the connection URL remains valid.
3. Keep Gemini on a Free Tier project. Obtain a key and confirm the selected model
   is available to that project. Never upload `.env.production` to GitHub.
4. Run the commands below. Migrate before starting the web service.

```sh
docker compose --env-file .env.production build
docker compose --env-file .env.production up -d db redis
docker compose --env-file .env.production run --rm api python manage.py migrate --noinput
docker compose --env-file .env.production up -d
```

Caddy provisions HTTPS when the real domain resolves and certificate validation
succeeds. Open `https://YOUR_DOMAIN`, create a test account, and run the Settings
connection check. Verify login, a Chinese answer with inspected citations, account
isolation, reload persistence and export before inviting testers. A connection
probe is not sufficient to establish medical answer quality.

The existing local SQLite database is not automatically copied to PostgreSQL.
This recipe starts a separate deployment database. Keep the local project and its
backups intact. Plan and validate a separate migration if local research must move.

## Operations

- Back up PostgreSQL regularly using `pg_dump` from the db container, store backups
  outside the host, and rehearse restoration. Do not remove Docker volumes to update.
- Before updating the release, take a backup; rebuild and run migrations, then
  restart services. Preserve `.env.production` and the named database volume.
- Inspect application and proxy logs, avoid recording question bodies or keys,
  and monitor model quota and availability.
- Give testers public research scenarios, not patient records. Gemini free-tier
  data-use conditions differ from paid service terms; consult the provider.
- The app has no email verification, administrator invitation workflow or password
  reset UI. Restrict initial external testing to a known cohort with a host-level
  access gate if necessary. The development acceptance is not a security audit,
  load benchmark or clinical validation.

## Provider sources

- https://ai.google.dev/gemini-api/docs/billing
- https://ai.google.dev/gemini-api/docs/pricing
- https://ai.google.dev/gemini-api/docs/openai

Documentation consulted November 15, 2026. Model availability and quotas can change.
