"""Bounded compatible-model transport and explicit, credential-free readiness state."""
import hashlib
import json
import re
from urllib.parse import urlsplit
import time

import requests
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone


class ModelError(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def configuration():
    url = urlsplit(settings.LLM_BASE_URL)
    local = url.hostname in ('localhost', '127.0.0.1', '::1')
    valid_url = (url.scheme == 'https' or (url.scheme == 'http' and local)) and bool(url.hostname)
    valid_url = valid_url and not (url.username or url.password or url.query or url.fragment)
    missing = []
    if not settings.LLM_MODEL.strip():
        missing.append('model')
    if not settings.LLM_API_KEY.strip() and not (local and settings.LLM_PROVIDER == 'ollama'):
        missing.append('credential')
    if not valid_url:
        missing.append('secure_endpoint')
    return {'configured': not missing, 'provider': settings.LLM_PROVIDER,
            'model': settings.LLM_MODEL, 'missing': missing}


def cache_key():
    # Changes to server credentials invalidate a prior readiness result. No secret is exposed.
    digest = hashlib.sha256('\0'.join([settings.LLM_BASE_URL, settings.LLM_MODEL,
                                      settings.LLM_API_KEY, settings.LLM_PROVIDER]).encode()).hexdigest()
    return 'synthesis-check:' + digest


def capability():
    config = configuration()
    checked = cache.get(cache_key()) if config['configured'] else None
    return {**config, 'state': checked['state'] if checked else
            ('unchecked' if config['configured'] else 'unconfigured'),
            'check': checked, 'scope': 'PubMed abstracts and metadata',
            'verification': 'Source and quotation checks plus automated claim review; not clinical validation.'}


def chinese_prose(text):
    han = len(re.findall(r'[\u3400-\u9fff]', text))
    latin = len(re.findall(r'[A-Za-z]', text))
    return han >= 4 and han / max(1, han + latin) >= .25


def complete_json(system, payload):
    if not configuration()['configured']:
        raise ModelError('unconfigured', 'AI synthesis is not configured. Ask the server operator to complete model setup.')
    # Shared across users and, with Redis configured, across server workers.
    quota_key = f'model-budget:{cache_key()}:{int(time.time()) // 60}'
    if cache.add(quota_key, 1, timeout=65):
        count = 1
    else:
        try:
            count = cache.incr(quota_key)
        except ValueError:
            cache.add(quota_key, 1, timeout=65)
            count = 1
    if count > settings.LLM_CALLS_PER_MINUTE:
        raise ModelError('quota', 'The shared application model-call limit was reached. Wait one minute and retry. Sources remain available.')
    headers = {'Accept': 'application/json'}
    if settings.LLM_API_KEY:
        headers['Authorization'] = f'Bearer {settings.LLM_API_KEY}'
    try:
        response = requests.post(settings.LLM_BASE_URL + '/chat/completions', headers=headers,
            json={'model': settings.LLM_MODEL, 'response_format': {'type': 'json_object'},
                  'max_tokens': settings.LLM_MAX_OUTPUT_TOKENS,
                  'messages': [{'role': 'system', 'content': system},
                               {'role': 'user', 'content': json.dumps(payload, ensure_ascii=False)}]},
            timeout=(5, settings.LLM_TIMEOUT_SECONDS), allow_redirects=False)
        if response.status_code in (401, 403):
            raise ModelError('authentication', 'The model service rejected the credential or model access. Check the server configuration.')
        if response.status_code == 429:
            raise ModelError('quota', 'The model service quota or rate limit was reached. Wait and retry or check the provider quota; billing is not enabled by this application.')
        if response.status_code == 404:
            raise ModelError('model_unavailable', 'The selected model or compatible API endpoint is unavailable. Check the model name and endpoint.')
        if response.status_code >= 300:
            raise ModelError('provider_error', 'The model service could not complete this request. Check the configuration or try again later.')
        raw = response.json()['choices'][0]['message']['content']
        if not isinstance(raw, str) or len(raw) > 100000:
            raise ValueError('Invalid model output')
        result = json.loads(raw)
        if not isinstance(result, dict):
            raise ValueError('Invalid model output')
        return result
    except requests.Timeout:
        raise ModelError('timeout', 'The model request timed out. Your retrieved sources remain available.') from None
    except (requests.RequestException, KeyError, IndexError, TypeError, ValueError):
        raise ModelError('invalid_response', 'The model service returned an unreadable response or could not be reached.') from None


def check_connection():
    """Use a fixed nonclinical prompt, never user research, for readiness checking."""
    if not configuration()['configured']:
        return capability()
    try:
        result = complete_json(
            'Return a JSON object with a text field containing one short sentence in Simplified Chinese. No medical claims.',
            {'task': 'Say that the research workspace connection test succeeded.'})
        if not isinstance(result.get('text'), str) or not chinese_prose(result['text']):
            raise ModelError('language_mismatch', 'The model responded, but the Chinese-output check failed.')
        checked = {'state': 'ready', 'code': 'check_passed', 'checked_at': timezone.now().isoformat(),
                   'message': 'Connection, JSON output and a short Chinese response passed. Research synthesis and clinical accuracy still require evaluation.'}
    except ModelError as error:
        checked = {'state': 'error', 'code': error.code, 'checked_at': timezone.now().isoformat(), 'message': str(error)}
    cache.set(cache_key(), checked, timeout=600)
    return capability()
