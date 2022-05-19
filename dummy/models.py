from unicodedata import name
from django.db import models
from django_countries.fields import CountryField
# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self):
        return self.country