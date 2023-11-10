import datetime
from data.decorators import performance_measure
from django.core.management import call_command
from django.core.management.base import BaseCommand
import time
import freezegun


class Command(BaseCommand):
    help = 'Load sample data into the database'
    default_workers_amount = 5
    default_departments_amount = 2
    default_cars_amount = 10
    default_clients_amount = 10
    default_rentals_amount = 20

    def add_arguments(self, parser):
        parser.add_argument('--workers', type=int, nargs='?', default=self.default_workers_amount,
                            help='Number of Pracownik entities to create')
        parser.add_argument('--departments', type=int, nargs='?', default=self.default_departments_amount,
                            help='Number of Oddzial entities to create')
        parser.add_argument('--cars', type=int, nargs='?', default=self.default_cars_amount,
                            help='Number of Samochod entities to create')
        parser.add_argument('--clients', type=int, nargs='?', default=self.default_clients_amount,
                            help='Number of Klient entities to create')
        parser.add_argument('--rentals', type=int, nargs='?', default=self.default_rentals_amount,
                            help='Number of Wypozyczenie entities to create')

    @performance_measure
    def handle(self, *args, **options):
        worker_amount = options['workers'] or self.default_workers_amount
        department_amount = options['departments'] or self.default_departments_amount
        car_amount = options['cars'] or self.default_cars_amount
        client_amount = options['clients'] or self.default_clients_amount
        rental_amount = options['rentals'] or self.default_rentals_amount

        self.stdout.write(self.style.SUCCESS(f'Loading data for T1 ...'))
        # Load data
        time.sleep(3)
        call_command(
            'load_database_data',
            workers=worker_amount,
            departments=department_amount,
            cars=car_amount,
            clients=client_amount,
            rentals=rental_amount
        )
        call_command('load_csv_data')

        # Create backups
        time.sleep(3)
        call_command('create_database_backup')
        call_command('create_csv_backup')

        self.stdout.write(self.style.SUCCESS(f'Loading data for T2 ...'))
        with freezegun.freeze_time(datetime.date.today() + datetime.timedelta(days=30)):
            # Update Databsse object
            time.sleep(3)
            call_command('update_database_entry')

            # Load data
            time.sleep(3)
            call_command(
                'load_database_data',
                workers=worker_amount,
                departments=department_amount,
                cars=car_amount,
                clients=client_amount,
                rentals=rental_amount
            )
            call_command('load_csv_data')

            # Create backups
            time.sleep(3)
            call_command('create_database_backup')
            call_command('create_csv_backup')
