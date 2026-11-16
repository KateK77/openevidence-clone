"""Synthetic security/allowance checks, not live AI quality tests."""
from datetime import timedelta
from unittest.mock import Mock
import pytest
import requests
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core.management import call_command
from django.core.management.base import CommandError
from django.utils import timezone
from rest_framework.test import APIClient
from evidence import llm
from evidence.models import Conversation, ModelCallBudget

pytestmark = pytest.mark.django_db


@pytest.fixture
def demo(settings):
    settings.PUBLIC_DEMO = True
    settings.PUBLIC_DEMO_LIVE_AI = True
    settings.LLM_MODEL = 'synthetic-model'
    settings.LLM_API_KEY = 'synthetic-test-only'
    settings.LLM_BASE_URL = 'https://example.test/v1'
    settings.PUBLIC_DEMO_DAILY_CALLS = 2
    settings.PUBLIC_DEMO_TOTAL_CALLS = 3
    cache.clear()


def test_seed_requires_explicit_opt_in(settings):
    settings.PUBLIC_DEMO = False
    with pytest.raises(CommandError):
        call_command('seed_public_demo')


def test_seed_preserves_edits_and_never_grants_staff(demo):
    call_command('seed_public_demo')
    u = User.objects.get(username='portfolio_researcher')
    password = u.password
    Conversation.objects.filter(owner=u).update(title='Visitor edit')
    call_command('seed_public_demo')
    u.refresh_from_db()
    assert u.password == password and u.check_password('MedEvidence-Demo-2026!')
    assert not u.is_staff and not u.is_superuser
    assert Conversation.objects.get(owner=u).title == 'Visitor edit'
    assert User.objects.count() == 2


def test_seed_does_not_take_over_existing_account(demo):
    User.objects.create_user(username='portfolio_researcher', password='PrivatePass-123!')
    with pytest.raises(CommandError):
        call_command('seed_public_demo')
    assert User.objects.get(username='portfolio_researcher').check_password('PrivatePass-123!')


def test_public_ai_is_opt_in_and_has_no_credential_in_session(demo, settings):
    settings.PUBLIC_DEMO_LIVE_AI = False
    assert not llm.configuration()['configured']
    response = APIClient().get('/api/session/')
    assert response.json()['public_demo']
    assert settings.LLM_API_KEY not in response.content.decode()


def test_shared_profile_credential_mutation_denied(demo):
    call_command('seed_public_demo')
    c = APIClient();c.force_authenticate(User.objects.get(username='portfolio_researcher'))
    assert c.patch('/api/profile/', {'username': 'takeover', 'password': 'Changed-123!', 'first_name': 'Changed'}, format='json').status_code == 403
    assert User.objects.get(username='portfolio_researcher').check_password('MedEvidence-Demo-2026!')


def test_regular_profile_still_editable(demo):
    c = APIClient();c.force_authenticate(User.objects.create_user(username='own_account'))
    assert c.patch('/api/profile/', {'first_name': 'Synthetic'}, format='json').status_code == 200


def test_failed_http_calls_consume_durable_allowance(demo, monkeypatch):
    post = Mock(side_effect=requests.Timeout)
    monkeypatch.setattr(llm.requests, 'post', post)
    for _ in range(2):
        with pytest.raises(llm.ModelError, match='timed out'):
            llm.complete_json('Synthetic', {})
        cache.clear()  # Simulate a restart: durable allowance must remain.
    with pytest.raises(llm.ModelError, match='allowance is exhausted'):
        llm.complete_json('Synthetic', {})
    assert post.call_count == 2
    assert ModelCallBudget.objects.get().total_calls == 2


def test_day_rollover_does_not_reset_lifetime_allowance(demo):
    ModelCallBudget.objects.create(key='public-demo', day=timezone.now().date()-timedelta(days=1), daily_calls=2, total_calls=2)
    llm.reserve_demo_call()
    budget = ModelCallBudget.objects.get()
    assert budget.daily_calls == 1 and budget.total_calls == 3
    with pytest.raises(llm.ModelError):
        llm.reserve_demo_call()


def test_oversized_input_is_rejected_before_http(demo, monkeypatch):
    post = Mock();monkeypatch.setattr(llm.requests, 'post', post)
    with pytest.raises(llm.ModelError, match='input allowance'):
        llm.complete_json('Synthetic', {'text': 'x'*100001})
    post.assert_not_called()
    assert not ModelCallBudget.objects.exists()


def test_database_failure_fails_closed(demo, monkeypatch):
    from django.db import DatabaseError
    monkeypatch.setattr(ModelCallBudget.objects, 'get_or_create', Mock(side_effect=DatabaseError))
    with pytest.raises(llm.ModelError, match='No model request'):
        llm.reserve_demo_call()
