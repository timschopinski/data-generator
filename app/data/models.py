from django.db import models


class Samochod(models.Model):
    numer_rejestracyjny = models.CharField(primary_key=True, max_length=20)
    id_oddzialu = models.ForeignKey('Oddzial', on_delete=models.CASCADE)
    typ = models.CharField(max_length=50)
    producent = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    cena = models.IntegerField()
    skrzynia_biegow = models.CharField(max_length=50)
    naped = models.CharField(max_length=50)
    rok_dodania = models.IntegerField()
    stan = models.CharField(max_length=50)


class Klient(models.Model):
    id_klienta = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    wiek = models.IntegerField()


class Wypozyczenie(models.Model):
    id_wypozyczenia = models.AutoField(primary_key=True)
    id_klienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
    numer_rejestracyjny = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    id_oddzialu = models.ForeignKey('Oddzial', on_delete=models.CASCADE)
    data_wynajecia = models.DateField()
    data_zwrotu = models.DateField()


class Oddzial(models.Model):
    id_oddzialu = models.AutoField(primary_key=True)
    lokalizacja = models.CharField(max_length=50)


class Pracownik(models.Model):
    id_pracownika = models.AutoField(primary_key=True)
    id_oddzialu = models.ForeignKey(Oddzial, on_delete=models.CASCADE)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    wiek = models.IntegerField()
    staz_pracy = models.IntegerField()
