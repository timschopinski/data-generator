from django.core.management.base import BaseCommand
from data.utils import create_csv_data


class Command(BaseCommand):
    help = 'Load sample data into the Excel Sheet'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f'Loading csv data ...'))
        try:
            create_csv_data()
            self.stdout.write(self.style.SUCCESS(f'Csv data successfully saved.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred when loading csv data. {e}'))
