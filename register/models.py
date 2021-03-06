from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    organisation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)

    def __unicode__(self):
        return self.email

