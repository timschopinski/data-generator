from django.core.management.base import BaseCommand
from data.utils import clear_models


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS(f'Deleting instances ...'))
        try:
            clear_models()
            self.stdout.write(self.style.SUCCESS(f'Instances successfully deleted ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when deleting instances - {e}'))
