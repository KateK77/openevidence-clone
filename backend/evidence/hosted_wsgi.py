"""Serve the built SPA and API from one origin on a small hosted instance."""
import os
import re
from pathlib import Path

from whitenoise import WhiteNoise
from .wsgi import application as django_application

frontend = Path(os.environ['FRONTEND_DIST'])
if not (frontend / 'index.html').is_file():
    raise RuntimeError('The compiled frontend is missing.')


def headers(response_headers, path, url):
    response_headers['X-Content-Type-Options'] = 'nosniff'
    response_headers['X-Frame-Options'] = 'DENY'
    response_headers['Referrer-Policy'] = 'same-origin'
    if url == '/index.html':
        response_headers['Cache-Control'] = 'no-cache'


files = WhiteNoise(django_application, root=str(frontend), max_age=3600,
                   add_headers_function=headers)
route = re.compile(r'^/(?:|profile|history|saved|library|publications|settings|thread/\d+|answer/\d+)/?$')


def application(environ, start_response):
    # API and asset misses must remain real 404s, not HTML masquerading as JSON/JS.
    if environ.get('REQUEST_METHOD') in ('GET', 'HEAD') and route.fullmatch(environ.get('PATH_INFO', '')):
        environ = {**environ, 'PATH_INFO': '/index.html'}
    return files(environ, start_response)
