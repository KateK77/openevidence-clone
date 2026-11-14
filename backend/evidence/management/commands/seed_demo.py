import os

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from evidence.models import Conversation, Turn


class Command(BaseCommand):
    help = 'Add a clearly labeled synthetic research account and sample conversation locally.'

    @transaction.atomic
    def handle(self, *args, **options):
        if not settings.DEBUG:
            raise CommandError('Demo data is available in development only.')
        password = os.getenv('DEMO_PASSWORD', '')
        if len(password) < 12:
            raise CommandError('Set DEMO_PASSWORD to at least 12 characters.')
        user, created = User.objects.get_or_create(username='demo_researcher')
        if not created:
            raise CommandError('The demo username is already in use.')
        user.set_password(password)
        user.save(update_fields=['password'])
        item = Conversation.objects.create(owner=user, title='Synthetic demo · Clinical documentation research')
        Turn.objects.create(
            conversation=item, question='What studies investigate language models in clinical documentation?',
            status='demo', result={'message': 'Synthetic example. Submit a new question to retrieve live PubMed evidence.'},
        )
        self.stdout.write('Created demo_researcher and a labeled synthetic conversation.')
