# Local development and optional models

Follow the [README quick start](../README.md#run-locally). Requirements: Python 3.12+, Node.js 24 and npm. Windows uses `.venv/Scripts/python.exe`; macOS/Linux uses `.venv/bin/python`.

The Windows launcher resolves paths relative to its script, reuses a suitable project environment, backs up local SQLite, checks ports, and writes ignored logs under `.runtime/`. Custom ports: `./start.ps1 -BackendPort 8023 -FrontendPort 5175`. The stop script only stops matching launcher-owned processes.

## Configuration

Copy `.env.example` to `.env`. SQLite is the local default; set `DATABASE_URL` for PostgreSQL. Hosted startup refuses SQLite. Keep secrets and local databases out of Git.

| Setting | Purpose |
|---|---|
| DJANGO_SECRET_KEY | Private signing secret; required for hosting |
| DJANGO_DEBUG | Local debugging; forced off by hosted startup |
| DATABASE_URL | PostgreSQL connection string |
| NCBI_EMAIL, NCBI_API_KEY | Optional server-side NCBI configuration |
| LLM_PROVIDER | Provider label, such as gemini or ollama |
| LLM_BASE_URL | Compatible chat-completions base; HTTPS except loopback development |
| LLM_MODEL, LLM_API_KEY | Server-only model and credential; omit for literature-only mode |
| LLM_TIMEOUT_SECONDS | Timeout per provider request |
| LLM_MAX_OUTPUT_TOKENS | Output limit; public deployment uses 3000 |
| REDIS_URL | Optional shared cache for the multi-service profile |

Gemini compatible base: `https://generativelanguage.googleapis.com/v1beta/openai`. Select an available model and verify its tier in your provider project. The public service reports `gemini-3.5-flash-lite`; this does not promise future availability or free pricing. The local `configure-model.ps1` uses a hidden credential prompt. A model is optional; do not activate billing merely to start the application.

Settings distinguishes configuration from a real connection check. Checking connectivity makes a provider request and consumes the demo allowance. Citation checks can withhold an answer even with successful connectivity. Chinese prose has at most one corrective language attempt; transport failures are not automatically retried.

## Synthetic shared accounts

Opt in with `PUBLIC_DEMO=1`, then run:

```bash
python backend/manage.py migrate
python backend/manage.py seed_public_demo
```

The [published credentials](../README.md#demo-accounts) then work locally. Seeding is idempotent and preserves existing research/passwords. A conflicting non-demo username is rejected. Set `PUBLIC_DEMO_LIVE_AI=1` separately to permit generation in demo mode. Daily/lifetime allowances are persistent.

## Verification

With the Python environment active:

```bash
python -m pytest -q
python backend/manage.py check
python backend/manage.py makemigrations --check --dry-run
python backend/manage.py spectacular --validate --fail-on-warn --file docs/openapi.yaml
npm --prefix frontend ci
npm --prefix frontend run build
npm --prefix frontend test
cd frontend
npx playwright install chromium
npm run e2e
```

The browser regression suite uses mocked API responses, not native CUA. The optional live PubMed pytest contract is skipped by default; real retrieval is checked separately by the public smoke.

With Docker running, from the repository root:

```bash
docker build -f deploy/Dockerfile.hosted -t medevidence-portfolio:test .
python scripts/portfolio_hosted_smoke.py
```

This uses disposable PostgreSQL and makes no model requests. The separate public runner is an explicit live verification: it writes synthetic demo data and can submit an initial research question and a follow-up. Do not run it as an unattended recurring job. It is not a paid native-CUA harness.
