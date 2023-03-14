import json
import requests

from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Загрузка данных о новом месте'

    def add_arguments(self, parser):
        parser.add_argument(
            'file_path',
            action='store',
            type=str
            )

    def handle(self, *args, **options):
        url = options['file_path']
        try:
            response = requests.get(url)
            response.raise_for_status()
            place_content = response.json()
            place = Place.objects.filter(
                title=place_content['title'],
                lat=place_content['coordinates']['lat'],
                lng=place_content['coordinates']['lng'],
                ).first()
            if not place:
                place = Place.objects.create()
                place.fill_from_dict(place_content)
            else:
                print(f'place {place_content["title"]} allready exist')
        except:
            raise CommandError('File "%s" does not exist' % url)
