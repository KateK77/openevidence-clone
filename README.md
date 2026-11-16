# MedEvidence AI 3.0

**RESEARCH DEMONSTRATION — NOT FOR CLINICAL USE.**

An independent biomedical literature workspace with live PubMed retrieval, optional abstract-grounded AI synthesis, source inspection, persistent conversations, and research exports. This project is not affiliated with OpenEvidence.

Version 3 addresses Round 2 manual feedback with Gemini configuration, explicit language availability, audited answer revisions and clearer retrieval provenance. Reports and repository documentation are in English. The original requirements and first version remain available in the experiment history and the **v0.1.0-r1** tag.

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

## What changed in 3.0

- Gemini free-tier setup using **configure-model.ps1** and a hidden local key prompt.
- Settings distinguishes missing configuration, unchecked configuration, a passed
  connection check, and provider errors. No key is sent to the browser.
- Chinese preferences show a bilingual explanation while AI is unavailable.
  The submit button says **Search literature** when no model is configured.
- Generated Chinese section prose is checked; a wrong-language draft is retried
  once, then withheld on failure. Source quotations remain in their original language.
- Each source-linked claim passes source/quote checks, a conservative numeric
  check and a separate automated review pass. This is not clinical validation.
- **Generate new answer** creates a new revision from the stored source snapshot
  with current preferences, preserving the original answer and bookmarks.
- Provenance separates the original question, normalization, available prior
  questions and executed PubMed queries, including in Markdown/PDF exports.
- A shared model-call budget and a [persistent HTTPS deployment recipe](docs/deployment.md).

## Retained improvements from 2.0

- A new responsive research interface, scrollable mobile navigation, keyboard focus handling, and clearer account and literature pages.
- Save controls show progress, success, and errors. Unchanged forms and already-saved records cannot be submitted repeatedly. Editing a saved form enables saving again.
- Dedicated **Saved answers** and **Saved publications** destinations; collections and saved searches.
- One-character non-whitespace queries are allowed. Common Chinese medical terminology is mapped to English with the exact transformation recorded in provenance. Unknown Chinese terms produce an actionable message instead of a misleading zero-result claim.
- Idempotent, CSRF-protected logout, app-specific cookies, cross-tab session updates, and rejection of responses that arrive after an account switch.
- Distinct electronic and journal-issue publication dates. Legacy snapshots explicitly label unspecified date types.
- Card and structured table views of evidence. Findings that were not synthesized and limitations that were not extracted are explicitly identified.
- Unicode Markdown, Excel-friendly UTF-8 CSV, BibTeX, and PDFs with an embedded Chinese/Latin font, headings, and page numbers.
- Safer startup with an explicit API port, existing-service detection, backup, and migration checks.

## Gemini configuration

Use a Google AI Studio **Free Tier** project. This application does not enable
billing and cannot inspect your project's billing tier. Confirm model availability
and quota in your account. The provided default is `gemini-3.5-flash-lite`, listed
with a free tier in the provider documentation consulted November 15, 2026.
Provider availability and limits can change.

From the project folder on Windows:

~~~powershell
.\configure-model.ps1
.\stop.ps1
.\start.ps1
~~~

Enter the key only at the hidden local terminal prompt. Then sign in, open
**Settings**, click **Check AI connection**, choose **Chinese** and save. Ask a
new question, or open an old answer and click **Generate new answer**. A probe
checks connectivity, JSON and a short Chinese sentence; it does not prove that
research synthesis or claim verification will succeed.

The cross-platform equivalent is `python backend/manage.py configure_model`, then
restart the backend. `python backend/manage.py check_model` runs the same fixed
nonmedical readiness check. Never put keys in command-line arguments or Git.

| Variable | Purpose |
| --- | --- |
| LLM_PROVIDER | `gemini` (selected for this release), `compatible`, or `ollama`. |
| LLM_MODEL | Compatible model identifier. |
| LLM_API_KEY | Server-only provider credential. |
| LLM_BASE_URL | Gemini: `https://generativelanguage.googleapis.com/v1beta/openai`. |
| LLM_TIMEOUT_SECONDS | Per-call read timeout, 60 seconds by default. |
| LLM_MAX_OUTPUT_TOKENS | Output limit per call, 6000 by default. |
| LLM_CALLS_PER_MINUTE | Shared application model-call cap; defaults to 12. |
| REDIS_URL | Shared cache and limits for multi-worker deployment; optional locally. |
| NCBI_EMAIL / NCBI_API_KEY | Optional PubMed contact and API credential. |
| DATABASE_URL | PostgreSQL URL; empty or omitted uses local SQLite. |
| DJANGO_DEBUG / DJANGO_SECRET_KEY | Local debug defaults to 1; production requires debug 0 and a private random secret. |
| DJANGO_ALLOWED_HOSTS / DJANGO_CSRF_TRUSTED_ORIGINS | Allowed backend hostnames and trusted frontend origins. |
| BACKEND_URL | Development proxy target; default `http://127.0.0.1:8021`. |

A source-linked answer normally requires two model calls: draft and claim review.
A language retry can add a third. Quota errors leave sources available; the app
does not switch providers or enable billing automatically. Testers share the
server project quota. Keep real patient information out of this research app.

For a local Ollama model, use `LLM_PROVIDER=ollama`, the actual installed model
name, and `LLM_BASE_URL=http://127.0.0.1:11434/v1`. Local Ollama does not require
a key. Hosted HTTP endpoints are rejected; remote providers must use HTTPS.

## Evidence boundaries

Search uses official ESearch, ESummary, and EFetch interfaces, deterministic ranking, PMID/DOI deduplication, request pacing, and caching. The synthesis context contains **abstracts and metadata**, not unavailable full text.

Every returned citation must refer to a retrieved record, and every quotation must match the supplied abstract excerpt. Round 3 also checks numeric consistency and runs an automated claim-support review. These checks do **not** independently prove clinical claim support. Review interpretations against the original sources.

Chinese normalization is a **bounded terminology glossary**, not unrestricted translation. The glossary fails closed for unrecognized Chinese text. Query provenance exposes the exact mapping. Other languages may be sent to PubMed as entered. The answer-language preference affects future model responses; it does not translate publication metadata.

This is a local research prototype. It has not been validated for clinical decisions. See the Round 3 report for the exact verification scope. Live Gemini generation requires an operator-supplied key; passing synthetic tests must not be reported as live model acceptance.

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

The live smoke runner uses **8022/5174**, leaves the normal app database untouched, shuts down its own test servers, and writes English results and screenshots under **experiments/round-03/**. It explicitly tests retrieval-only mode. Do not run it concurrently with the other browser suite.

For the smaller live PubMed contract check:

~~~powershell
$env:RUN_LIVE_PUBMED = '1'
& .venv/Scripts/python.exe -m pytest -m live -q
Remove-Item Env:RUN_LIVE_PUBMED
~~~

## Demo data

Set a locally chosen **DEMO_PASSWORD** of at least 12 characters, then run **python backend/manage.py seed_demo** using the project virtual environment. The account **demo_researcher** and its conversation are explicitly synthetic. Submit a new question to retrieve real sources.

## Experiment records

- [Round 3 consolidated prompt](experiments/round-03/consolidated-prompt.md)
- [Round 3 feedback](experiments/round-03/feedback.md)
- [Round 3 verification report](experiments/round-03/results.md)
- [Long-running deployment](docs/deployment.md)
- [Round 2 release and verification report](experiments/round-02/results.md)
- [Round 2 illustrated report](experiments/round-02/report.html)
- [Round 1 original requirements](experiments/round-01/description.md)
- [Round 1 manual acceptance report](experiments/round-01/manual-acceptance/report.html)
- [Architecture and API](docs/architecture.md)
- [Changelog](CHANGELOG.md)

For deployment, serve the built frontend and Django API on the same HTTPS origin. Production operations require PostgreSQL, shared caching/rate limits, monitoring, backup policies, and independent validation.
