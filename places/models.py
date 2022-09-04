from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    coordinate_lng = models.FloatField(blank=True)
    coordinate_lat = models.FloatField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(blank=True)
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.place.title}'
