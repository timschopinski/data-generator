from django.core.management.base import BaseCommand
from data.utils import create_database_backup


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):

        self.stdout.write(self.style.WARNING(f'Creating database backup ...'))
        try:
            create_database_backup()
            self.stdout.write(self.style.SUCCESS(f'Database backup successfully created ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when creating database backup - {e}'))
