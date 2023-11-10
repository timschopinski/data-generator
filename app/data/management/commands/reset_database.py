import time
from django.core.management.base import BaseCommand
import os
from data.decorators import performance_measure


class Command(BaseCommand):
    help = 'Reset the database by removing db.sqlite3, clearing migrations, and applying migrations'

    @performance_measure
    def handle(self, *args, **options):

        db_file = 'db.sqlite3'
        if os.path.exists(db_file):
            os.remove(db_file)
            time.sleep(1)
            self.stdout.write(self.style.SUCCESS('Removed db.sqlite3'))

        app_names = ['data']

        for app_name in app_names:
            migrations_dir = os.path.join(app_name, 'migrations')
            if os.path.exists(migrations_dir):
                for root, dirs, files in os.walk(migrations_dir):
                    for file in files:
                        if file != '__init__.py':
                            os.remove(os.path.join(root, file))
                self.stdout.write(self.style.SUCCESS(f'Cleared migrations for {app_name}'))

        from django.core.management import call_command
        call_command('makemigrations')
        self.stdout.write(self.style.SUCCESS('Created new migrations'))

        call_command('migrate')
        self.stdout.write(self.style.SUCCESS('Applied new migrations'))
