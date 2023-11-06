from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Load sample data into the database'
    default_workers_amount = 10
    default_departments_amount = 3
    default_cars_amount = 10
    default_clients_amount = 20
    default_rentals_amount = 30

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

    def handle(self, *args, **options):
        worker_amount = options['workers'] or self.default_workers_amount
        department_amount = options['departments'] or self.default_departments_amount
        car_amount = options['cars'] or self.default_cars_amount
        client_amount = options['clients'] or self.default_clients_amount
        rental_amount = options['rentals'] or self.default_rentals_amount

        self.stdout.write(self.style.SUCCESS(f'Loading data for T1 ...'))
        call_command(
            'load_data',
            workers=worker_amount,
            departments=department_amount,
            cars=car_amount,
            clients=client_amount,
            rentals=rental_amount
        )
        self.stdout.write(self.style.SUCCESS(f'Loading data for T2 ...'))
        call_command('create_backup')
        call_command('clear_db')
        call_command('load_backup')
        call_command(
            'load_data',
            workers=worker_amount,
            departments=department_amount,
            cars=car_amount,
            clients=client_amount,
            rentals=rental_amount
        )
