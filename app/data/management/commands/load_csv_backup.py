from django.core.management.base import BaseCommand
from data.utils import load_csv_backup


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def add_arguments(self, parser):
        parser.add_argument('--date', type=str, help='Date of the csv backup in the format YYYY-MM-DD')

    def handle(self, *args, **options):
        backup_date = options.get('date')

        self.stdout.write(self.style.WARNING(f'Loadin csv backup ...'))
        try:
            load_csv_backup(backup_date)
            self.stdout.write(self.style.SUCCESS(f'Csv backup successfully loaded ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when loading csv backup - {e}'))
