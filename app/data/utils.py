import pickle
from typing import Collection, List

from app.settings import BACKUP_DIR
from .models import Pracownik, Samochod, Klient, Oddzial, Wypozyczenie
from django.db.models import Model
import logging

logger = logging.getLogger(__name__)


def get_default_models():
    return [Oddzial, Pracownik, Samochod, Klient, Wypozyczenie]


def remove(model_class: Model):
    amount = model_class.objects.count()
    model_class.objects.all().delete()
    logger.info(f'{amount} {model_class.__name__} instances removed successfully')


def bulk_create(model_class: Model, instances: List[Model]) -> None:
    print(instances)
    model_class.objects.bulk_create(instances)
    logger.info(f'{model_class.__name__} instances created successfully')


def clear_models(*models):
    if not models:
        models = get_default_models()
    for model in models:
        remove(model)


def create_backup(*models):
    if not models:
        models = get_default_models()
    for model in models:
        filename = f'{model.__name__.lower()}_backup.pkl'
        backup_path = BACKUP_DIR / filename
        backup = model.objects.all()
        with open(backup_path, 'wb') as file:
            pickle.dump(backup, file)


def load_backup(*models):
    if not models:
        models = get_default_models()
    for model in models:
        filename = f'{model.__name__.lower()}_backup.pkl'
        backup_path = BACKUP_DIR / filename
        with open(backup_path, 'rb') as file:
            backup = pickle.load(file)

        model.objects.bulk_create([obj for obj in backup])
