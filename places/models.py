import requests

from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.core.files.base import ContentFile


class Place(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    description_short = HTMLField()
    description_long = HTMLField()

    def __str__(self) -> str:
        return self.title

    def get_images_list(self):
        return [image.image.url for image in self.images.all()]

    def get_place_feature(self):
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [
                    round(self.lng, 2),
                    round(self.lat, 6)
                    ]
            },
            'properties': {
                'title': self.title,
                'placeId': f'key_{self.pk}',
                'detailsUrl': f'/places/{self.pk}/',
            }
        }
        return feature

    def get_place_json(self):
        return {
                    'title': self.title,
                    'imgs': self.get_images_list(),
                    'description_short': self.description_short,
                    'description_long': self.description_long,
                    'coordinates': {
                        'lng': self.lng,
                        'lat': self.lat,
                    }
                }

    def load_image(self, image_path, position):
        response = requests.get(image_path)
        response.raise_for_status()
        image_type = image_path.split('.')[-1]
        image = Image.objects.create()
        image.place = self
        image.position = position
        image.image.save(
            f'image_{self.pk}_{image.pk}.{image_type}',
            ContentFile(response.content),
            save=True,
            )
        image.save()

    def fill_from_dict(self, place_content):
        self.title = place_content['title']
        self.lat = place_content['coordinates']['lat']
        self.lng = place_content['coordinates']['lng']
        self.description_short = place_content['description_short']
        self.description_long = place_content['description_long']
        self.save()
        for position, image_path in enumerate(place_content['imgs']):
            self.load_image(image_path, position)


class Image(models.Model):
    image = models.ImageField()
    position = models.PositiveSmallIntegerField(default=0)
    place = models.ForeignKey(
        'Place',
        on_delete=models.SET_NULL,
        null=True,
        related_name='images',
        )

    def __str__(self) -> str:
        return f'{self.pk} {self.place}'

    def preview_image(obj):
        return format_html(
            '<img src="{url}" width={width} />'.format(
                url=obj.image.url,
                width=200,
            )
        )

    class Meta:
        ordering = ['position']
