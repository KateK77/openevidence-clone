"""Opt-in, idempotent shared synthetic accounts; never reset visitor data."""
from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from evidence.models import Conversation, Preferences, Turn


class Command(BaseCommand):
    help = 'Seed protected public portfolio accounts only with PUBLIC_DEMO=1.'

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.PUBLIC_DEMO:
            raise CommandError('Set PUBLIC_DEMO=1 explicitly to enable shared synthetic accounts.')
        group, _ = Group.objects.get_or_create(name='MedEvidence public demonstration')
        for username in settings.PUBLIC_DEMO_USERS:
            user, created = User.objects.get_or_create(username=username)
            if not created:
                if not user.groups.filter(pk=group.pk).exists():
                    raise CommandError('Reserved demo username belongs to another account; no changes made.')
                continue
            # Public demonstration credential, intentionally documented; never a server secret.
            user.set_password('MedEvidence-Demo-2026!')
            user.first_name = 'Synthetic researcher' if username.endswith('researcher') else 'Synthetic reader'
            user.save()
            user.groups.add(group)
            Preferences.objects.create(user=user, language='English', detail='Concise')
            conversation = Conversation.objects.create(owner=user, title='Welcome to the synthetic research workspace')
            Turn.objects.create(conversation=conversation, question='How can I explore MedEvidence AI?', status='demo',
                result={'message': 'Synthetic onboarding example, not an AI-generated medical answer. Search a PMID in Evidence Library or ask a new research question to retrieve real PubMed publications.'},
                provenance={'fixture': True, 'source': 'seed_public_demo; no fabricated publications'})
        self.stdout.write('Public demo accounts ready; existing data and credentials preserved.')
