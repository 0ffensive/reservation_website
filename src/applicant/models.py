from django.db import models
from country.models import Country, Center


class SlovakiaApplicant(models.Model):
    username = models.CharField(max_length=100)
    passport = models.CharField(max_length=100)
    applicant_type = models.CharField(max_length=30, default='fake')
    priority = models.IntegerField(default=0)
    date_reserved = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class BRTAApplicant(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    applicant_type = models.CharField(max_length=30, default='fake')
    priority = models.IntegerField(default=0)
    date_reserved = models.BooleanField(default=False)
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class DateOpen(models.Model):
    date_open = models.BooleanField(default=False)
    month = models.IntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country.name} ({self.center.name})'


class SlovakiaProcess(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    month = models.IntegerField()
    process_type = models.IntegerField()

    def __str__(self):
        return f'{self.center.name} ({self.status})'
