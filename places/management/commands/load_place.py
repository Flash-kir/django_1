import json
import requests

from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
from django.core.files.base import ContentFile


def load_image(place, image_path, position):
    response = requests.get(image_path)
    response.raise_for_status()
    image_type = image_path.split('.')[-1]
    image = Image.objects.create()
    image.place = place
    image.position = position
    image.image.save(
        f'image_{place.pk}_{image.pk}.{image_type}',
        ContentFile(response.content),
        save=True,
    )
    image.save()


def fill_from_dict(place, place_content):
    place.title = place_content['title']
    place.lat = place_content['coordinates']['lat']
    place.lng = place_content['coordinates']['lng']
    place.description_short = place_content['description_short']
    place.description_long = place_content['description_long']
    place.save()
    for position, image_path in enumerate(place_content['imgs']):
        load_image(place, image_path, position)


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
