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
        print(response)

        try:
            obj, created = Place.objects.get_or_create(
                title=response['title'],
                defaults={
                    'description_short': response['description_short'],
                    'description_long': response['description_long'],
                    'lon': response['coordinates']['lng'],
                    'lat': response['coordinates']['lat']
                }
            )

            if created:
                for url in response['imgs']:
                    response = requests.get(url)
                    response.raise_for_status()
                    Image.objects.create(place=obj).picture.save('new_place', ContentFile(response.content), save=True)

        except Place.MultipleObjectsReturned:
            print('Такая достопримечательность уже имеется в бд')
