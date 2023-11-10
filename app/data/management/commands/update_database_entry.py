from django.core.management.base import BaseCommand
from data.models import Samochod
from data.decorators import performance_measure


class Command(BaseCommand):
    help = 'Update Car price in the database'

    @performance_measure
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING(f'Updating car price ...'))
        try:
            self.update_car_price()
            self.stdout.write(self.style.SUCCESS(f'Successfully updated car price'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Failed to update car price - {e}'))

    def update_car_price(self):
        car = Samochod.objects.last()
        car.cena = car.cena + 1000
        car.save()
