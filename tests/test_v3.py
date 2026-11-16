"""Synthetic model fixtures test contracts and failures, not real model quality."""
import json
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
import requests
from rest_framework.test import APIClient

from evidence import llm, rag, exports
from evidence.models import Turn
from test_platform import register, mock_search, reset_cache, RECORD, ask


@pytest.fixture
def configured(settings):
    settings.LLM_PROVIDER = 'gemini'
    settings.LLM_BASE_URL = 'https://generativelanguage.googleapis.com/v1beta/openai'
    settings.LLM_MODEL = 'synthetic-model'
    settings.LLM_API_KEY = 'synthetic-secret-not-real'


def answer(text='这是用于测试的合成研究描述，不包含真实医学结论。', **changes):
    return {'sections': [{'text': text, 'status': 'supported', 'kind': 'finding',
                          'citations': [{'pmid': '123', 'quote': RECORD['abstract']}], **changes}]}


def model_responses(monkeypatch, *payloads):
    rows = []
    for payload in payloads:
        response = Mock(status_code=200)
        response.json.return_value = {'choices': [{'message': {'content': json.dumps(payload)}}]}
        rows.append(response)
    post = Mock(side_effect=rows)
    monkeypatch.setattr(llm.requests, 'post', post)
    return post


REVIEW = {'reviews': [{'index': 0, 'verdict': 'supported'}]}
PREFS = SimpleNamespace(language='Chinese', detail='Detailed')


def test_chinese_generation_requires_quote_and_claim_review(configured, monkeypatch):
    post = model_responses(monkeypatch, answer(), REVIEW)
    status, _, result = rag.synthesize('Test question', [], [RECORD], PREFS)
    assert status == 'complete'
    assert result['language_check'] == 'passed'
    assert result['verification']['claim_review'] == 'passed'
    assert result['verification']['clinical_validation'] is False
    assert result['sections'][0]['verification'] == 'automated_checks_passed'
    assert post.call_count == 2
    system = post.call_args_list[0].kwargs['json']['messages'][0]['content']
    assert 'Simplified Chinese' in system and '6 to 10 sections' in system


@pytest.mark.parametrize('recovers', [True, False])
def test_wrong_language_retries_once_and_never_publishes_english(configured, monkeypatch, recovers):
    english = answer('A synthetic English claim for testing.')
    post = model_responses(monkeypatch, english, answer() if recovers else english, REVIEW)
    status, _, result = rag.synthesize('Question', [], [RECORD], PREFS)
    assert status == ('complete' if recovers else 'generation_error')
    assert post.call_count == (3 if recovers else 2)
    if not recovers:
        assert result['code'] == 'language_mismatch'
        assert 'sections' not in result
        assert '英文草稿未发布' in result['message']


@pytest.mark.parametrize('review', [
    {'reviews': [{'index': 0, 'verdict': 'unsupported'}]},
    {'reviews': []}, {'reviews': [{'index': 1, 'verdict': 'supported'}]},
    {'reviews': [{'index': 0, 'verdict': 'supported'}, {'index': 0, 'verdict': 'supported'}]},
    {'reviews': [{'index': False, 'verdict': 'supported'}]}, {},
])
def test_failed_or_malformed_review_withholds_all_claims(configured, monkeypatch, review):
    model_responses(monkeypatch, answer(), review)
    status, _, result = rag.synthesize('Question', [], [RECORD], PREFS)
    assert status == 'generation_error' and result['code'] == 'verification_failed'
    assert 'sections' not in result


def test_numeric_hallucination_blocked_before_review(configured, monkeypatch):
    post = model_responses(monkeypatch, answer('测试声称改善了99.5%，但原文并没有这个数字。'))
    status, _, result = rag.synthesize('Question', [], [RECORD], PREFS)
    assert status == 'generation_error'
    assert post.call_count == 1
    assert result['code'] == 'verification_failed'


@pytest.mark.parametrize('code,expected', [(401,'authentication'), (403,'authentication'), (429,'quota'), (404,'model_unavailable'), (503,'provider_error'), (302,'provider_error')])
def test_provider_errors_do_not_leak_credentials(configured, monkeypatch, code, expected):
    response = Mock(status_code=code, text='secret-provider-response')
    post = Mock(return_value=response)
    monkeypatch.setattr(llm.requests, 'post', post)
    with pytest.raises(llm.ModelError) as caught:
        llm.complete_json('test', {})
    assert caught.value.code == expected
    assert 'secret' not in str(caught.value)
    assert post.call_args.kwargs['allow_redirects'] is False


def test_unconfigured_chinese_is_an_explicit_system_notice(settings):
    settings.LLM_API_KEY = ''
    status, _, result = rag.synthesize('糖尿病', [], [RECORD], PREFS)
    assert status == 'retrieval_only'
    assert '没有生成中文医学回答' in result['message']
    assert '不是 AI 回答' in result['message']
    assert 'sections' not in result


def test_local_ollama_and_secure_url_validation(settings):
    settings.LLM_PROVIDER = 'ollama'
    settings.LLM_BASE_URL = 'http://127.0.0.1:11434/v1'
    settings.LLM_MODEL = 'synthetic-local-model'
    settings.LLM_API_KEY = ''
    assert llm.configuration()['configured']
    settings.LLM_BASE_URL = 'http://external.test/v1'
    assert not llm.configuration()['configured']
    settings.LLM_API_KEY = 'test'
    settings.LLM_BASE_URL = 'https://user:secret@external.test/v1'
    assert not llm.configuration()['configured']


@pytest.mark.django_db
def test_readiness_requires_auth_and_csrf_and_never_uses_user_prompt(register, configured, monkeypatch, settings):
    assert APIClient().get('/api/synthesis/').status_code == 403
    client = register('connection_check')
    assert client.get('/api/session/').json()['synthesis']['state'] == 'unchecked'
    post = model_responses(monkeypatch, {'text': '研究工作区连接测试成功。'})
    response = client.post('/api/synthesis/', {'url': 'https://attacker.test', 'prompt': 'private research'}, format='json')
    assert response.json()['state'] == 'ready'
    assert 'synthetic-secret' not in response.content.decode()
    assert 'private research' not in json.dumps(post.call_args.kwargs)
    assert client.get('/api/session/').json()['synthesis']['state'] == 'ready'
    client.credentials(HTTP_X_CSRFTOKEN='wrong')
    assert client.post('/api/synthesis/', {}, format='json').status_code == 403
    settings.LLM_API_KEY = 'changed-key'
    assert llm.capability()['state'] == 'unchecked'


@pytest.mark.django_db
def test_regeneration_preserves_original_and_owner_isolation(register, mock_search, configured, monkeypatch):
    owner, stranger = register('revision_owner'), register('revision_stranger')
    model_responses(monkeypatch, answer(), REVIEW)
    original = ask(owner).json()
    owner.put(f'/api/answers/{original["id"]}/save/', {}, format='json')
    path = f'/api/answers/{original["id"]}/regenerate/'
    assert stranger.post(path, {}, format='json').status_code == 404
    owner.patch('/api/settings/', {'language': 'Chinese'}, format='json')
    post = model_responses(monkeypatch, answer(kind='limitation'), REVIEW)
    fresh = owner.post(path, {}, format='json')
    assert fresh.status_code == 201
    fresh = fresh.json()
    assert fresh['id'] != original['id'] and fresh['conversation'] == original['conversation']
    assert fresh['provenance']['revision_of'] == original['id']
    assert fresh['provenance']['evidence_reused']
    assert fresh['sources'] == original['sources']
    assert fresh['result']['language'] == 'Chinese'
    assert post.call_count == 2
    old = Turn.objects.get(pk=original['id'])
    assert old.saved and old.result == original['result']
    assert not fresh['saved']
    markdown = exports.markdown(Turn.objects.get(pk=fresh['id']))
    assert 'Automated claim review: passed' in markdown and 'Normalized question before context:' in markdown


@pytest.mark.django_db
def test_unconfigured_regeneration_does_not_add_empty_turn(register, mock_search):
    client = register('missing_model')
    original = ask(client).json()
    assert client.post(f'/api/answers/{original["id"]}/regenerate/', {}, format='json').status_code == 409
    assert Turn.objects.count() == 1


def test_model_review_timeout_withholds_draft(configured, monkeypatch):
    draft = Mock(status_code=200)
    draft.json.return_value = {'choices':[{'message':{'content':json.dumps(answer())}}]}
    monkeypatch.setattr(llm.requests, 'post', Mock(side_effect=[draft, requests.Timeout()]))
    status, _, result = rag.synthesize('Question', [], [RECORD], PREFS)
    assert status == 'generation_error' and result['code'] == 'timeout'
    assert 'sections' not in result


def test_shared_model_budget_applies_across_calls(configured, monkeypatch, settings):
    settings.LLM_CALLS_PER_MINUTE = 1
    post = model_responses(monkeypatch, {'text': '研究工作区连接测试成功。'})
    llm.complete_json('test', {})
    with pytest.raises(llm.ModelError) as caught:
        llm.complete_json('test', {})
    assert caught.value.code == 'quota'
    assert post.call_count == 1


@pytest.mark.parametrize('verdict,expected', [('supported', 'insufficient'), ('unsupported', 'generation_error')])
def test_uncited_gap_sections_are_also_reviewed(configured, monkeypatch, verdict, expected):
    draft = answer('现有摘要不足以说明长期结局，需要进一步查阅原始研究。', status='insufficient', citations=[])
    post = model_responses(monkeypatch, draft, {'reviews':[{'index':0, 'verdict':verdict}]})
    status, _, result = rag.synthesize('Question', [], [RECORD], PREFS)
    assert post.call_count == 2 and status == expected
    assert ('sections' in result) == (expected == 'insufficient')
