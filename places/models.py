from django.db import models


# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    coordinate_lng = models.FloatField(blank=True)
    coordinate_lat = models.FloatField(blank=True)
