from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Наименование')
    short_description = HTMLField(blank=True, verbose_name='Краткое описание достопримечательности')
    long_description = HTMLField(blank=True, verbose_name='Развернутое описание достопримечательности')
    lon = models.FloatField(verbose_name='Долгота')
    lat = models.FloatField(verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    picture = models.ImageField(verbose_name='Файл изображения')
    position = models.IntegerField(verbose_name='Позиция', blank=True, db_index=True, default=0)

    class Meta:
        ordering = ['position', ]

    def __str__(self):
        return f'{self.id} {self.place.title}'
