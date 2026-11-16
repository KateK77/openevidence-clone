import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR.parent / '.env')
DEBUG = os.getenv('DJANGO_DEBUG', '1') == '1'
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or ('unsafe-local-development-only' if DEBUG else '')
if not SECRET_KEY:
    raise RuntimeError('DJANGO_SECRET_KEY is required outside development')
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('DJANGO_CSRF_TRUSTED_ORIGINS', '').split() or (
    ['http://localhost:5173', 'http://127.0.0.1:5173'] if DEBUG else []
)
ROOT_URLCONF = 'evidence.urls'
WSGI_APPLICATION = 'evidence.wsgi.application'
INSTALLED_APPS = [
    'django.contrib.auth', 'django.contrib.contenttypes', 'django.contrib.sessions',
    'rest_framework', 'drf_spectacular', 'evidence',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]
DATABASES = {'default': dj_database_url.parse(
    os.getenv('DATABASE_URL') or f'sqlite:///{BASE_DIR / "local.sqlite3"}', conn_max_age=0,
)}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
USE_TZ = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = 'medevidence_session_v2'
CSRF_COOKIE_NAME = 'medevidence_csrf_v2'
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_CONTENT_TYPE_NOSNIFF = True
DATA_UPLOAD_MAX_MEMORY_SIZE = 32768
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'django.contrib.auth.password_validation.{name}'}
    for name in ('UserAttributeSimilarityValidator', 'MinimumLengthValidator',
                 'CommonPasswordValidator', 'NumericPasswordValidator')
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
    'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser'],
    'DEFAULT_THROTTLE_RATES': {'auth': '12/min', 'research': '8/min', 'literature': '24/min', 'model_check': '4/min'},
}
SPECTACULAR_SETTINGS = {'TITLE': 'MedEvidence AI API', 'VERSION': '3.0.0'}
NCBI_EMAIL = os.getenv('NCBI_EMAIL', '')
NCBI_API_KEY = os.getenv('NCBI_API_KEY', '')
LLM_BASE_URL = os.getenv('LLM_BASE_URL', 'https://api.openai.com/v1').rstrip('/')
LLM_API_KEY = os.getenv('LLM_API_KEY', '')
LLM_MODEL = os.getenv('LLM_MODEL', '')
LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'compatible')
LLM_TIMEOUT_SECONDS = max(10, min(120, int(os.getenv('LLM_TIMEOUT_SECONDS', '60'))))
LLM_MAX_OUTPUT_TOKENS = max(512, min(16000, int(os.getenv('LLM_MAX_OUTPUT_TOKENS', '6000'))))
LLM_CALLS_PER_MINUTE = max(1, min(1000, int(os.getenv('LLM_CALLS_PER_MINUTE', '12'))))
if cache_url := os.getenv('REDIS_URL'):
    CACHES = {'default': {'BACKEND': 'django.core.cache.backends.redis.RedisCache', 'LOCATION': cache_url}}
if os.getenv('TRUST_PROXY_HTTPS') == '1':
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
