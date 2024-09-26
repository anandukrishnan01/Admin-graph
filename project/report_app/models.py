from django.db import models

# Create your models here.

class DataEntry(models.Model):
    category = models.CharField(max_length=100)
    value = models.FloatField()