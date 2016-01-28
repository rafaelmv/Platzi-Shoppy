from __future__ import unicode_literals

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)