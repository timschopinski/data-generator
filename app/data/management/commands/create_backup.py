from django.core.management.base import BaseCommand
from data.utils import create_backup


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f'Creating Backups ...'))
        try:
            create_backup()
            self.stdout.write(self.style.SUCCESS(f'Backup successfully created ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when creating backup - {e}'))
