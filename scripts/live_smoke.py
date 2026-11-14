"""Opt-in browser acceptance against real Django and official live PubMed APIs."""
import os
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
for port in (8022, 5174):
    try:
        connection = socket.create_connection(('127.0.0.1', port), timeout=.5)
    except OSError:
        continue
    connection.close()
    raise RuntimeError(f'Port {port} is occupied. Stop the other test run before continuing.')
runtime = repo / ".runtime"
runtime.mkdir(exist_ok=True)
env = os.environ.copy()
env["DATABASE_URL"] = "sqlite:///" + (runtime / "live-test.sqlite3").as_posix()
env["DJANGO_CSRF_TRUSTED_ORIGINS"] = "http://127.0.0.1:5174"
env["DJANGO_ALLOWED_HOSTS"] = "127.0.0.1,localhost"
env["LLM_API_KEY"] = ""  # Explicit retrieval-only integration test, without model charges.
env["DJANGO_DEBUG"] = "1"
subprocess.run([sys.executable, "backend/manage.py", "migrate", "--noinput"], cwd=repo, env=env, check=True)
with (runtime / "live-backend.log").open("w") as log:
    server = subprocess.Popen([sys.executable, "backend/manage.py", "runserver", "127.0.0.1:8022", "--noreload"],
        cwd=repo, env=env, stdout=log, stderr=log, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    try:
        ready = False
        for _ in range(60):
            if server.poll() is not None:
                raise RuntimeError("The test backend could not start; port 8022 may be occupied.")
            try:
                with urllib.request.urlopen("http://127.0.0.1:8022/api/health/", timeout=2):
                    ready = True
                    break
            except OSError:
                time.sleep(.25)
        if not ready:
            raise RuntimeError("The isolated test backend did not become ready.")
        subprocess.run(["node", str(repo / "scripts/live_smoke.cjs")], cwd=repo, check=True, timeout=300)
    finally:
        if os.name == 'nt' and server.poll() is None:
            subprocess.run(['taskkill', '/PID', str(server.pid), '/T', '/F'], capture_output=True)
        else:
            server.terminate()
        server.wait(timeout=10)
