from datetime import timedelta, datetime
import random
import factory
from app.settings import manufacturer_models
from .models import Pracownik, Oddzial, Samochod, Klient, Wypozyczenie
from faker import Factory as FakerFactory
import logging


logger = logging.getLogger(__name__)
faker = FakerFactory.create('pl_PL')


class OddzialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Oddzial

    lokalizacja = factory.Faker('city')


class PracownikFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pracownik

    id_oddzialu = factory.SubFactory(OddzialFactory)
    imie = factory.Faker('first_name')
    nazwisko = factory.Faker('last_name')
    wiek = factory.Faker('random_int', min=20, max=60)
    staz_pracy = factory.Faker('random_int', min=1, max=15)

    @factory.post_generation
    def random_oddzial(self, create, extracted, **kwargs):
        if not create:
            return
        oddzial_list = Oddzial.objects.all()
        if oddzial_list:
            oddzial = random.choice(oddzial_list)
            self.id_oddzialu = oddzial


class SamochodFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Samochod

    numer_rejestracyjny = factory.Faker('unique.random_int')
    id_oddzialu = factory.SubFactory(OddzialFactory)
    typ = factory.Faker('word')
    producent = factory.Faker('company')
    model = factory.Faker('word')
    cena = factory.Faker('random_int', min=50, max=500)
    skrzynia_biegow = factory.Faker('random_element', elements=['automatyczna', 'manualna'])
    naped = factory.Faker('random_element', elements=['benzynowy', 'elektryczny', 'diesel'])
    rok_dodania = factory.LazyAttribute(lambda _: random.randint(2010, 2023))
    stan = factory.Faker('word')


class KlientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Klient

    imie = factory.Faker('first_name')
    nazwisko = factory.Faker('last_name')
    wiek = factory.Faker('random_int', min=18, max=80)


class WypozyczenieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wypozyczenie

    id_klienta = factory.SubFactory(KlientFactory)
    numer_rejestracyjny = factory.SubFactory(SamochodFactory)
    id_oddzialu = factory.SubFactory(OddzialFactory)
    data_wynajecia = factory.Faker('date_between', start_date='-30d', end_date='today')
    data_zwrotu = factory.LazyAttribute(lambda obj: obj.data_wynajecia + timedelta(days=faker.random_int(min=1, max=14)))


def create_workers(amount):
    departments = Oddzial.objects.all()[:100]
    workers = []
    for _ in range(amount):
        department = random.choice(departments)
        workers.append(
            Pracownik(
                imie=faker.first_name(),
                nazwisko=faker.last_name(),
                wiek=random.randint(20, 60),
                staz_pracy=random.randint(1, 15),
                id_oddzialu=department
            )
        )
    Pracownik.objects.bulk_create(workers)
    logger.info(f'{amount} {Pracownik.__name__} instances created successfully')


def create_departments(amount):
    departments = []
    for _ in range(amount):
        departments.append(
            Oddzial(lokalizacja=faker.city())
        )
    Oddzial.objects.bulk_create(departments)
    logger.info(f'{amount} {Oddzial.__name__} instances created successfully')


def create_cars(amount):
    departments = Oddzial.objects.all()[:100]

    contidions = [
        'dobry', 'uszkodzony', 'powypadkowy', 'nowy', 'nowy', 'nowy',
        'dobry', 'uszkodzony', 'nowy', 'nowy', 'nowy', 'nowy',
    ]
    cars = []
    for _ in range(amount):
        department = random.choice(departments)
        manufacturer = random.choice(list(manufacturer_models.keys()))
        model_idx = random.randint(0, len(manufacturer_models[manufacturer]['models']) - 1)
        import uuid

        cars.append(
            Samochod(
                numer_rejestracyjny=f'{str(uuid.uuid4())[:15]}',
                id_oddzialu=department,
                producent=manufacturer,
                model=manufacturer_models[manufacturer]['models'][model_idx],
                typ=manufacturer_models[manufacturer]['types'][model_idx],
                cena=random.randint(50, 1000),
                skrzynia_biegow=random.choice(['automatyczna', 'manualna']),
                naped=random.choice(['benzynowy', 'elektryczny', 'diesel']),
                rok_dodania=datetime.strftime(faker.date_of_birth(minimum_age=1, maximum_age=10), '%Y'),
                stan=random.choice(contidions)
            )
        )
    Samochod.objects.bulk_create(cars)
    logger.info(f'{amount} {Samochod.__name__} instances created successfully')


def create_clients(amount):
    clients = []
    for _ in range(amount):
        clients.append(
            Klient(
                imie=faker.first_name(),
                nazwisko=faker.last_name(),
                wiek=random.randint(18, 80),
                lata_od_rejestracji=random.randint(1, 5),
                czy_aktualne=random.choice([True, False])
            )
        )
    Klient.objects.bulk_create(clients)
    logger.info(f'{amount} {Klient.__name__} instances created successfully')


def create_rentals(amount):
    clients = Klient.objects.all()[:100]
    cars = Samochod.objects.all()[:100]
    departments = Oddzial.objects.all()[:100]
    rentals = []
    for _ in range(amount):
        car = random.choice(cars)
        client = random.choice(clients)
        department = random.choice(departments)
        data_wynajecia = faker.date_between(start_date='-30d', end_date='today')
        data_zwrotu = data_wynajecia + timedelta(days=random.randint(1, 14))
        rentals.append(
            Wypozyczenie(
                id_klienta=client,
                numer_rejestracyjny=car,
                id_oddzialu=department,
                data_wynajecia=data_wynajecia,
                data_zwrotu=data_zwrotu
            )
        )
    Wypozyczenie.objects.bulk_create(rentals)
    logger.info(f'{amount} {Wypozyczenie.__name__} instances created successfully')
