from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Center(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country.name} - {self.name}'
