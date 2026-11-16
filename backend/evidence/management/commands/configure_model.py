"""Interactive local setup. Never accept credentials as command-line arguments."""
import getpass
import os
import re
import sys
import tempfile
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from dotenv import dotenv_values, set_key


class Command(BaseCommand):
    help = 'Configure Gemini in the ignored local .env using a hidden credential prompt.'

    def add_arguments(self, parser):
        parser.add_argument('--model', default='gemini-3.5-flash-lite')

    def handle(self, *args, **options):
        if not sys.stdin.isatty():
            raise CommandError('Use an interactive local terminal. Credentials must not be passed through chat or command arguments.')
        model = options['model'].strip()
        if not re.fullmatch(r'gemini-[A-Za-z0-9._-]{1,120}', model):
            raise CommandError('Enter a Gemini model identifier, not a URL or credential.')
        self.stdout.write('Use a Google AI Studio project whose billing tier is Free. This tool cannot inspect billing and never enables it.')
        self.stdout.write(f'Selected model: {model}. Check availability and quota in your own project.')
        key = getpass.getpass('Gemini API key (hidden; stored only in local .env): ').strip()
        if not key or any(ch.isspace() for ch in key) or len(key) > 512:
            raise CommandError('The credential must be nonempty, contain no whitespace and be at most 512 characters.')
        destination = settings.BASE_DIR.parent / '.env'
        # Atomic replacement preserves unrelated configuration without an on-disk key backup.
        original = destination.read_text(encoding='utf-8-sig') if destination.exists() else ''
        fd, path = tempfile.mkstemp(prefix='.env.setup-', dir=destination.parent, text=True)
        try:
            with os.fdopen(fd, 'w', encoding='utf-8') as handle:
                handle.write(original)
            for name, value in {'LLM_PROVIDER': 'gemini', 'LLM_MODEL': model,
                                'LLM_BASE_URL': 'https://generativelanguage.googleapis.com/v1beta/openai',
                                'LLM_API_KEY': key}.items():
                set_key(path, name, value)
            if dotenv_values(path).get('LLM_API_KEY') != key:
                raise CommandError('Configuration validation failed; the original file is unchanged.')
            os.replace(path, destination)
        finally:
            Path(path).unlink(missing_ok=True)
        self.stdout.write(self.style.SUCCESS('Local model settings saved. Restart the server, then use Check AI connection in Settings.'))
