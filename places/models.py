from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, blank=True, unique=True)
    description_short = HTMLField()
    description_long = HTMLField()
    coordinate_lng = models.FloatField(blank=True)
    coordinate_lat = models.FloatField(blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(blank=True)
    position = models.IntegerField(verbose_name='Позиция', blank=True, null=True, db_index=True, default=0)

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return f'{self.id} {self.place.title}'
