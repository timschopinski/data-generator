from django.core.management.base import BaseCommand
from data.utils import load_database_backup
from django.core.management import call_command
from datetime import date


class Command(BaseCommand):
    help = 'Load sample data into the database'

    def add_arguments(self, parser):
        default_date = date.today().strftime('%Y-%m-%d')
        parser.add_argument('--date', type=str, default=default_date, help='Date of the database backup in the format YYYY-MM-DD')

    def handle(self, *args, **options):
        backup_date = options.get('date')
        print(backup_date)
        call_command('clear_database')
        if not backup_date:
            self.stdout.write(self.style.ERROR('Please provide a valid --date argument in the format YYYY-MM-DD'))
            return

        self.stdout.write(self.style.WARNING(f'Loading database backup for date: {backup_date} ...'))
        try:
            load_database_backup(date=backup_date)
            self.stdout.write(self.style.SUCCESS(f'Database backup successfully loaded ...'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error when loading database backup - {e}'))
