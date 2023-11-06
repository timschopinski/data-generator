from django.core.management.base import BaseCommand
from data.utils import load_backup


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f'Loadin Backups ...'))
        try:
            load_backup()
            self.stdout.write(self.style.SUCCESS(f'Backup successfully loaded ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when loading backup - {e}'))
