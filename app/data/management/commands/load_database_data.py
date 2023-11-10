from data.decorators import performance_measure
from django.core.management.base import BaseCommand
from data.factories import create_cars, create_clients, create_rentals, create_workers, create_departments


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

    @performance_measure
    def handle(self, *args, **options):
        worker_amount = options['workers'] or self.default_workers_amount
        department_amount = options['departments'] or self.default_departments_amount
        car_amount = options['cars'] or self.default_cars_amount
        client_amount = options['clients'] or self.default_clients_amount
        rental_amount = options['rentals'] or self.default_rentals_amount

        self.stdout.write(self.style.WARNING(f'Generating instances ...'))
        try:
            create_departments(department_amount)
            create_workers(worker_amount)
            create_cars(car_amount)
            create_clients(client_amount)
            create_rentals(rental_amount)
            self.stdout.write(self.style.SUCCESS(f'Successfully generated instances'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to generate instances - {e}'))
