from django.db import models

# Create your models here.


class Items(models.Model):
    api_well_number = models.CharField(max_length=255, unique=True)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()
