from django.core.management.base import BaseCommand
from data.utils import create_csv_backup


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f'Creating csv backup ...'))
        try:
            create_csv_backup()
            self.stdout.write(self.style.SUCCESS(f'csv backup successfully created ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when creating csv backup - {e}'))
