# MedEvidence AI 2.0

**RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.**

An independent biomedical literature workspace with live PubMed retrieval, optional abstract-grounded AI synthesis, source inspection, persistent conversations, and research exports. This project is not affiliated with OpenEvidence.

Version 2 rebuilds the interface and addresses Round 1 manual acceptance feedback. Reports and repository documentation are in English. The original requirements and first version remain available in the experiment history and the **v0.1.0-r1** tag.

## Start on Windows

Open PowerShell in this project folder. Run each command separately.

~~~powershell
.\setup.ps1
.\start.ps1
~~~

If dependencies are already installed, run only **start.ps1**. It resolves paths relative to the script, so it also works when called by absolute path from another folder. It detects the existing project or workspace Python environment, locates Node, backs up local SQLite before migration, and checks ports before starting hidden development servers.

Open **http://127.0.0.1:5173**. Create a research account or use an existing one. Version 2 uses app-specific session cookies; users upgrading from v1 must sign in once again. Their accounts, conversations, and saved publications remain intact.

- API default: **127.0.0.1:8021**.
- Frontend default: **127.0.0.1:5173**.
- Choose different ports with **.\start.ps1 -BackendPort 8023 -FrontendPort 5175**.
- **.\stop.ps1** stops only processes recorded by this launcher with matching process start times. Servers launched manually must be stopped in their original terminal.
- Logs and automatic SQLite backups are in **.runtime/**, excluded from Git.
- The launcher refuses to adopt a different service or version on an occupied port.
- If Node/npm is unavailable, install Node.js 24 LTS and reopen PowerShell. Install Python 3.12+ if no project Python environment exists.

## Manual setup / macOS / Linux

Requires Python 3.12+ and Node.js 24 with npm.

~~~bash
cp .env.example .env
python -m venv .venv
.venv/bin/python -m pip install -r backend/requirements.txt
.venv/bin/python backend/manage.py backup_local
.venv/bin/python backend/manage.py migrate
.venv/bin/python backend/manage.py runserver 127.0.0.1:8021
~~~

In a separate terminal:

~~~bash
cd frontend
npm ci
npm run dev -- --host 127.0.0.1 --port 5173 --strictPort
~~~

On Windows, the Python executable is **.venv/Scripts/python.exe**. Keep each server in its own terminal when using manual commands.

## What changed in 2.0

- A new responsive research interface, scrollable mobile navigation, keyboard focus handling, and clearer account and literature pages.
- Save controls show progress, success, and errors. Unchanged forms and already-saved records cannot be submitted repeatedly. Editing a saved form enables saving again.
- Dedicated **Saved answers** and **Saved publications** destinations; collections and saved searches.
- One-character non-whitespace queries are allowed. Common Chinese medical terminology is mapped to English with the exact transformation recorded in provenance. Unknown Chinese terms produce an actionable message instead of a misleading zero-result claim.
- Idempotent, CSRF-protected logout, app-specific cookies, cross-tab session updates, and rejection of responses that arrive after an account switch.
- Distinct electronic and journal-issue publication dates. Legacy snapshots explicitly label unspecified date types.
- Card and structured table views of evidence. Findings that were not synthesized and limitations that were not extracted are explicitly identified.
- Unicode Markdown, Excel-friendly UTF-8 CSV, BibTeX, and PDFs with an embedded Chinese/Latin font, headings, and page numbers.
- Safer startup with an explicit API port, existing-service detection, backup, and migration checks.

## AI configuration

PubMed retrieval works without a paid model key. **AI-generated synthesis requires both LLM_MODEL and LLM_API_KEY.** Until configured, the application clearly displays Literature mode and never substitutes a hardcoded answer.

Edit the local **.env** file and restart the backend:

| Variable | Purpose |
| --- | --- |
| LLM_MODEL | Model identifier supporting Chat Completions JSON-object output. |
| LLM_API_KEY | Server-side provider credential. Never commit or enter it in the browser. |
| LLM_BASE_URL | OpenAI-compatible API base URL; default https://api.openai.com/v1. |
| NCBI_EMAIL / NCBI_API_KEY | Optional PubMed contact and higher-rate API credential. |
| DATABASE_URL | PostgreSQL connection URL for deployments. Empty or omitted selects local SQLite. |
| DJANGO_DEBUG / DJANGO_SECRET_KEY | Local debug defaults to 1. Set debug to 0 and use a private random secret for deployment. |
| DJANGO_ALLOWED_HOSTS | Comma-separated allowed backend hosts. |
| DJANGO_CSRF_TRUSTED_ORIGINS | Space-separated trusted frontend origins. |
| BACKEND_URL | Frontend dev proxy target; default http://127.0.0.1:8021. |

Model credentials remain server-side. A configured model is not a guarantee that the provider is reachable. Timeout, provider, and citation-validation failures remain explicit while retrieved sources stay available.

## Evidence boundaries

Search uses official ESearch, ESummary, and EFetch interfaces, deterministic ranking, PMID/DOI deduplication, request pacing, and caching. The synthesis context contains **abstracts and metadata**, not unavailable full text.

Every returned citation must refer to a retrieved record, and every quotation must match the supplied abstract excerpt. These checks do **not** independently prove clinical claim support. Review interpretations against the original sources.

Chinese normalization is a **bounded terminology glossary**, not unrestricted translation. The glossary fails closed for unrecognized Chinese text. Query provenance exposes the exact mapping. Other languages may be sent to PubMed as entered. The answer-language preference affects future model responses; it does not translate publication metadata.

This is a local research prototype. It has not been validated for clinical decisions. Live LLM generation and a PostgreSQL deployment were not exercised in this round because no configured model credential or PostgreSQL service was available.

## Verification

From the repository root, use the appropriate virtual-environment Python:

~~~powershell
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe backend/manage.py check
& .venv/Scripts/python.exe backend/manage.py makemigrations --check --dry-run
& .venv/Scripts/python.exe backend/manage.py spectacular --validate --fail-on-warn --file docs/openapi.yaml
~~~

From **frontend/**:

~~~powershell
npm run build
npm test
npx playwright install chromium
npm run e2e
~~~

The browser suite uses isolated port **5174** and synthetic API fixtures. To exercise real Django, a separate SQLite database, Chromium, and live PubMed:

~~~powershell
& .venv/Scripts/python.exe scripts/live_smoke.py
~~~

The live smoke runner uses **8022/5174**, leaves the normal app database untouched, shuts down its own test servers, and writes English results and screenshots under **experiments/round-02/**. It explicitly tests retrieval-only mode. Do not run it concurrently with the other browser suite.

For the smaller live PubMed contract check:

~~~powershell
$env:RUN_LIVE_PUBMED = '1'
& .venv/Scripts/python.exe -m pytest -m live -q
Remove-Item Env:RUN_LIVE_PUBMED
~~~

## Demo data

Set a locally chosen **DEMO_PASSWORD** of at least 12 characters, then run **python backend/manage.py seed_demo** using the project virtual environment. The account **demo_researcher** and its conversation are explicitly synthetic. Submit a new question to retrieve real sources.

## Experiment records

- [Round 2 release and verification report](experiments/round-02/results.md)
- [Round 2 illustrated report](experiments/round-02/report.html)
- [Round 1 original requirements](experiments/round-01/description.md)
- [Round 1 manual acceptance report](experiments/round-01/manual-acceptance/report.html)
- [Architecture and API](docs/architecture.md)
- [Changelog](CHANGELOG.md)

For deployment, serve the built frontend and Django API on the same HTTPS origin. Production operations require PostgreSQL, shared caching/rate limits, monitoring, backup policies, and independent validation.
