"""Round 2 regression tests. All external literature/model responses are synthetic fixtures."""
import csv
import io
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from rest_framework.test import APIClient

from evidence import exports, pubmed, rag
from evidence.models import SavedSearch, SavedPublication
from test_platform import register, mock_search, reset_cache, RECORD, ask


@pytest.mark.django_db
def test_logout_idempotent_but_requires_csrf(register, settings):
    client = register('logout_v2')
    assert settings.SESSION_COOKIE_NAME == 'medevidence_session_v2'
    assert settings.CSRF_COOKIE_NAME == 'medevidence_csrf_v2'
    for _ in range(2):
        response = client.post('/api/logout/', {}, format='json')
        assert response.status_code == 200
        assert response.json()['user'] is None
        client.credentials(HTTP_X_CSRFTOKEN=response.json()['csrf'])
        assert client.get('/api/session/').json()['user'] is None
    assert client.get('/api/settings/').status_code == 403
    anonymous = APIClient(enforce_csrf_checks=True)
    assert anonymous.post('/api/logout/', {}, format='json').status_code == 403


@pytest.mark.django_db
@pytest.mark.parametrize('question,term', [('糖尿病', 'diabetes mellitus'), ('糖尿病怎么治疗', 'diabetes mellitus treatment'), ('高血压', 'hypertension'), ('pain', 'pain')])
def test_short_and_chinese_queries(register, mock_search, question, term):
    client = register('query_v2')
    result = ask(client, question)
    assert result.status_code == 201
    trace = result.json()['provenance']
    assert term in trace['searches'][0]['query']
    assert trace['normalization']['original'] == question
    assert len(result.json()['sources']) == 1


def test_unmapped_chinese_is_not_silently_dropped(monkeypatch):
    search = Mock()
    monkeypatch.setattr(pubmed, 'search_ids', search)
    sources, trace = rag.retrieve('糖尿病伴有罕见未知病名', [])
    assert sources == []
    assert trace['searches'] == []
    assert 'translation limitation' in trace['normalization']['notice']
    search.assert_not_called()


def test_chinese_followup_inherits_topic_but_new_short_topic_does_not(mock_search):
    _, trace = rag.retrieve('这些研究有什么局限性', ['肥胖治疗'])
    assert trace['intent'] == 'limitations'
    assert 'obesity' in trace['searches'][0]['query']
    _, trace = rag.retrieve('pain', ['obesity treatment'])
    assert 'obesity' not in trace['searches'][0]['query']
    assert 'pain' in trace['searches'][0]['query']


@pytest.mark.django_db
def test_save_search_idempotence_and_ownership(register):
    owner, stranger = register('search_owner'), register('search_stranger')
    data = {'q': 'diabetes', 'year': 2021, 'sort': 'relevance'}
    first = owner.post('/api/saved-searches/', data, format='json')
    assert first.status_code == 201
    assert owner.post('/api/saved-searches/', data, format='json').status_code == 200
    assert SavedSearch.objects.count() == 1
    assert stranger.get('/api/saved-searches/').json() == []
    url = '/api/saved-searches/' + str(first.json()['id']) + '/'
    assert stranger.delete(url).status_code == 404
    assert owner.delete(url).status_code == 204
    assert owner.get('/api/saved-searches/').json() == []


@pytest.mark.django_db
def test_saved_collection_and_profile_survive_session(register, mock_search):
    client = register('persistence')
    assert client.patch('/api/profile/', {'first_name': 'Alex'}, format='json').json()['first_name'] == 'Alex'
    assert client.patch('/api/settings/', {'language': 'Chinese', 'display': 'Compact'}, format='json').status_code == 200
    for collection in ['', 'Obesity research', 'Obesity research']:
        client.put('/api/articles/123/save/', {'collection': collection}, format='json')
    assert SavedPublication.objects.count() == 1
    assert client.get('/api/saved-articles/').json()[0]['collection'] == 'Obesity research'
    assert client.get('/api/session/').json()['user']['first_name'] == 'Alex'
    assert client.get('/api/settings/').json()['display'] == 'Compact'


def test_export_unicode_punctuation_and_csv_formula_safety():
    article = {**RECORD, 'title': 'A title with a period.', 'authors': ['Andrej Janež'], 'date_type': 'Electronic publication'}
    turn = SimpleNamespace(pk=42, question='糖尿病', status='retrieval_only', model='', created=SimpleNamespace(isoformat=lambda:'2026-11-14T00:00:00Z'), result={}, provenance={}, evidence=SimpleNamespace(all=lambda:[SimpleNamespace(snapshot=article)]))
    markdown = exports.markdown(turn)
    assert '—' in markdown and 'â€' not in markdown
    assert 'period..' not in markdown
    assert 'Electronic publication' in markdown
    response = exports.export(turn, 'md')
    assert '糖尿病' in response.content.decode('utf-8')
    article['title'] = '=HYPERLINK("bad")'
    response = exports.export(turn, 'csv')
    assert response.content.startswith(b'\xef\xbb\xbf')
    rows = list(csv.reader(io.StringIO(response.content.decode('utf-8-sig'))))
    assert rows[1][1].startswith("'=")
    assert rows[1][2] == 'Andrej Janež'
    assert exports.export(turn, 'pdf').content.startswith(b'%PDF')


def test_distinct_publication_dates(monkeypatch):
    xml = b'<PubmedArticleSet><PubmedArticle><MedlineCitation><PMID>123</PMID><Article><ArticleTitle>Fixture</ArticleTitle><ArticleDate DateType="Electronic"><Year>2021</Year><Month>02</Month><Day>10</Day></ArticleDate><Journal><JournalIssue><PubDate><Year>2021</Year><Month>Mar</Month><Day>18</Day></PubDate></JournalIssue></Journal></Article></MedlineCitation></PubmedArticle></PubmedArticleSet>'
    monkeypatch.setattr(pubmed, 'fetch', lambda *args, **kwargs: xml)
    row = pubmed.records(['123'])[0]
    assert row['electronic_date'] == '2021 02 10'
    assert row['issue_date'] == '2021 Mar 18'
    assert row['date_type'] == 'Electronic publication'


def test_empty_evidence_before_model_configuration(settings):
    settings.LLM_API_KEY = ''
    status, _, result = rag.synthesize('question', [], [], SimpleNamespace())
    assert status == 'insufficient'
    assert 'zero-result search does not establish' in result['message']


@pytest.mark.django_db
def test_unmapped_library_query_returns_actionable_error(register):
    client = register('translation_gap')
    result = client.get('/api/articles/', {'q': '未知罕见疾病名称'})
    assert result.status_code == 422
    assert 'English medical keywords' in result.json()['detail']


def test_unverified_source_id_and_missing_quote_rejected():
    for citation in [{'pmid':'999','quote':RECORD['abstract']}, {'pmid':'123','quote':'fabricated excerpt with sufficient characters'}]:
        with pytest.raises(rag.GenerationError):
            rag.validate_answer({'sections':[{'text':'A claim.', 'status':'supported', 'citations':[citation]}]}, {'123':RECORD['abstract']})


def test_blank_database_url_uses_local_sqlite():
    import os
    import subprocess
    import sys
    from pathlib import Path
    environment = {**os.environ, 'DATABASE_URL': ''}
    backend = Path(__file__).resolve().parents[1] / 'backend'
    result = subprocess.run([sys.executable, '-c',
        'from evidence.settings import DATABASES; assert DATABASES["default"]["ENGINE"] == "django.db.backends.sqlite3"'],
        cwd=backend, env=environment, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
