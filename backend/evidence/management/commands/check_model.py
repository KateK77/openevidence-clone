import json

from django.core.management.base import BaseCommand, CommandError
from evidence.llm import check_connection


class Command(BaseCommand):
    help = 'Check configured model connectivity, JSON and Chinese output with a nonmedical prompt.'

    def handle(self, *args, **options):
        result = check_connection()
        self.stdout.write(json.dumps(result, ensure_ascii=False, indent=2))
        if result['state'] != 'ready':
            raise CommandError('Model readiness check did not pass; no clinical synthesis was tested.')
