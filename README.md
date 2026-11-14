# MedEvidence AI

**RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.**

MedEvidence AI is an independent clinical literature research workspace inspired by OpenEvidence. It uses public PubMed records and an optional OpenAI-compatible model to produce abstract-grounded research summaries. Use synthetic research examples only.

## Run locally

Requires Python 3.12+ and Node.js 24 with npm. Run from the repository root.

```powershell
Copy-Item .env.example .env
python -m venv .venv
& .venv/Scripts/python.exe -m pip install -r backend/requirements.txt
& .venv/Scripts/python.exe backend/manage.py migrate
& .venv/Scripts/python.exe backend/manage.py runserver 127.0.0.1:8000
```

In another terminal:

```powershell
Set-Location frontend
npm ci
npm run dev -- --host 127.0.0.1
```

Open [http://127.0.0.1:5173](http://127.0.0.1:5173) and create a research account. On macOS or Linux use `cp .env.example .env` and `.venv/bin/python` instead of the PowerShell file and executable commands. Vite proxies `/api` to Django. For a production-style deployment, serve the built frontend and Django API on the same HTTPS origin, route SPA paths to `index.html`, and use PostgreSQL.

### Configuration

| Variable | Purpose |
| --- | --- |
| `LLM_API_KEY`, `LLM_MODEL` | Required for synthesis. Omit either to run retrieval-only. The selected model must handle Chat Completions JSON mode. |
| `LLM_BASE_URL` | OpenAI-compatible base URL including API version. Defaults to `https://api.openai.com/v1`. |
| `NCBI_EMAIL`, `NCBI_API_KEY` | PubMed contact and optional rate-limit key. Public smoke tests can run without a key. |
| `DATABASE_URL` | PostgreSQL URL for deployed environments. Local default is SQLite. |
| `DJANGO_DEBUG`, `DJANGO_SECRET_KEY` | Local debug defaults to 1. Set debug to 0 and set a private random secret in production. |
| `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS` | Comma-separated hosts and space-separated trusted origins. |
| `DEMO_PASSWORD` | Optional local environment variable for the synthetic account seed command. |

Optional synthetic demo account, with a locally chosen password:

```powershell
$env:DEMO_PASSWORD = 'Choose-a-unique-demo-password'
& .venv/Scripts/python.exe backend/manage.py seed_demo
Remove-Item Env:DEMO_PASSWORD
```

Sign in as `demo_researcher`. The seeded conversation contains a synthetic question and a demo notice.

## Verify

```powershell
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe backend/manage.py check
& .venv/Scripts/python.exe backend/manage.py makemigrations --check --dry-run
& .venv/Scripts/python.exe backend/manage.py spectacular --validate --fail-on-warn --file docs/openapi.yaml
$env:RUN_LIVE_PUBMED = '1'
& .venv/Scripts/python.exe -m pytest -m live -q
Set-Location frontend
npm run build
npm test
npx playwright install chromium
npm run e2e
```

### Manual walkthrough

1. Register and submit an example question. With no model key, the conversation displays a retrieval-only status and its source records when PubMed responds.
2. Open the answer details, expand an article, follow the PMID link, and download Markdown, PDF, BibTeX and CSV.
3. Ask a follow-up in the same conversation, rename it, and find it using history search.
4. Search the library by keyword, PMID or DOI. Inspect a source, save it, assign a collection, then remove it.
5. Save an answer, log out, sign back in and confirm history and saved answers persisted. A second account has its own history.
6. Configure a compatible model and repeat the question. Inspect the quoted abstracts and compare the generated claims with the source.
7. On a narrow screen, open the navigation drawer and verify that the evidence table scrolls inside the page.

## Project files

- `frontend/` is the React research workspace.
- `backend/` is the Django REST API, persistence, PubMed and generation pipeline.
- `tests/` contains deterministic backend coverage and the optional live smoke test. Browser tests live under `frontend/e2e/`.
- [Architecture and API](docs/architecture.md)
- [Round 1 results](experiments/round-01/results.md)
