from django.db import models


class Free_Proxy(models.Model):
    address = models.CharField(max_length=20)
    port = models.IntegerField()
    taken = models.BooleanField(default=False)

    def __str__(self):
        return self.address + ':' + self.port


class Authenticated_Proxy(models.Model):
    address = models.CharField(max_length=20)
    port = models.IntegerField()
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, default='Random')

    def __str__(self):
        return f'{self.address}:{self.port}'
