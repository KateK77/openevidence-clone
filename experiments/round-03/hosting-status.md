# Free hosting deployment status

Updated November 15, 2026, America/Chicago.

The user authorized a free public test deployment, accepting idle suspension,
and explicitly confirmed Render **My Workspace** and Neon **Jiawen** as the
target accounts. No paid upgrade or payment-method change is authorized.

## Completed

- The local v3 release is preserved at tag `v3.0.0-r3` (`2c9b5ac`).
- The free-hosting implementation is on `v3-round-03`, commit `27d313f`.
- GitHub verification of that commit passed, including backend/frontend tests,
  browser tests, Docker builds and both container integration checks:
  https://github.com/KateK77/openevidence-clone/actions/runs/43803623146
- Neon Free project `medevidence-ai-v3` was created in `aws-us-east-2`, with
  database `medevidence`. No local user data was uploaded. Connection credentials
  were retained in session memory only for server-side configuration.
- The single-service image serves the React app and Django API on one origin,
  refuses ephemeral SQLite, and runs PostgreSQL migrations during startup.

## Current blocker

Render's create-service operation returned HTTP 400: the private repository
`https://github.com/KateK77/openevidence-clone` was invalid or unfetchable. GitHub
metadata and `git ls-remote` independently confirm the repository and branch
exist. The user reported granting Render access to all repositories, but a retry
still failed. The exact cause is not yet confirmed.

No MedEvidence Render service or public URL has been created. Existing services
for other repositories were left unchanged. The user is checking whether the
repository appears in Render's Git Provider list; no repository visibility change
or credential-in-URL workaround has been attempted.

## Remaining verification

Create the Free service after resolving Git provider access, monitor the specific
deployment until live, and verify HTTPS, real registration/login, saved data,
PubMed retrieval and account isolation. Gemini Chinese generation still requires
the operator's server-side Free Tier key; literature-only checks do not satisfy
that acceptance requirement.
