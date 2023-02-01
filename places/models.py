from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description_short = HTMLField(blank=True)
    description_long = HTMLField(blank=True)
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    picture = models.ImageField()
    position = models.IntegerField(verbose_name='Позиция', blank=True, db_index=True, default=0)

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return f'{self.id} {self.place.title}'
