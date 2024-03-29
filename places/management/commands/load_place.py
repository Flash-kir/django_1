import requests

from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
from django.core.files.base import ContentFile


def load_image(place, image_path, position):
    response = requests.get(image_path)
    response.raise_for_status()
    image_type = image_path.split('.')[-1]
    Image.objects.create(
        place=place,
        position=position,
        image=ContentFile(
            response.content,
            f'image_{place.pk}_{position}.{image_type}'
        )
    )


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

            title = place_content['title']
            lat = place_content['coordinates']['lat']
            lng = place_content['coordinates']['lng']

            description_short = place_content.get('description_short', '')
            description_long = place_content.get('description_long', '')

            place, created = Place.objects.get_or_create(
                title=title,
                lat=lat,
                lng=lng,
                defaults={
                    'description_short': description_short,
                    'description_long': description_long,
                }
            )
            image_urls = place_content.get('imgs', default=[])
            if created:
                for position, image_path in enumerate(image_urls):
                    load_image(place, image_path, position)
            else:
                print(f'place {place_content["title"]} allready exist')
        except FileExistsError:
            raise CommandError(f'File {url} does not exist')
        except Exception as err:
            print(f'Exception: {err}')
