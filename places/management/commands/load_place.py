from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
import requests

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('json_url', nargs='+', type=str)

    def handle(self, *args, **options):

        url = options['json_url'][0]
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()

        try:
            obj, created = Place.objects.update_or_create(
                title=response['title'],
                defaults={
                    'short_description': response['description_short'],
                    'long_description': response['description_long'],
                    'lon': response['coordinates']['lng'],
                    'lat': response['coordinates']['lat']
                }
            )

            if not created and obj:
                obj.images.all().delete()

            for url in response['imgs']:
                response = requests.get(url)
                response.raise_for_status()
                Image.objects.create(
                    place=obj,
                    picture=ContentFile(response.content, 'new_place')
                )

        except Place.MultipleObjectsReturned:
            print('Такая достопримечательность уже имеется в бд')
