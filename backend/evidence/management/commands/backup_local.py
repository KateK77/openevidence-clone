"""Consistent SQLite backup before an additive local migration."""
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Back up the configured local SQLite database without changing its contents.'

    def handle(self, *args, **options):
        database = settings.DATABASES['default']
        if database['ENGINE'] != 'django.db.backends.sqlite3':
            self.stdout.write('External database: manage backups through your database service.')
            return
        source = Path(database['NAME'])
        if not source.exists():
            self.stdout.write('New local database; no backup needed.')
            return
        folder = settings.BASE_DIR.parent / '.runtime' / 'backups'
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / ('before-migration-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ') + '.sqlite3')
        try:
            with sqlite3.connect(source.resolve().as_uri() + '?mode=ro', uri=True) as original, sqlite3.connect(target) as backup:
                original.backup(backup)
        except sqlite3.Error as error:
            raise CommandError('Could not create a consistent local database backup.') from error
        self.stdout.write('Local database backup created in .runtime/backups.')
