from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=20, decimal_places=15, default=0)
    lng = models.DecimalField(max_digits=20, decimal_places=15, default=0)
    description_short = HTMLField()
    descripton_long = HTMLField()

    def __str__(self) -> str:
        return self.title

    def get_images_list(self):
        images_list = []
        for image in Image.objects.filter(place=self):
            images_list.append(image.image.url)
        return images_list

    def get_lat(self, round="1.000000"):
        return self.lat.quantize(Decimal(round), ROUND_HALF_UP)

    def get_lng(self, round="1.00"):
        return self.lng.quantize(Decimal(round), ROUND_HALF_UP)

    def get_place_feature(self):
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    float(self.get_lng()),
                    float(self.get_lat())
                    ]
            },
            "properties": {
                "title": self.title,
                "placeId": f"key_{self.pk}",
                "detailsUrl": f"/places/{self.pk}/",
            }
        }
        return feature

    def get_place_json(self):
        return {
                    "title": self.title,
                    "imgs": self.get_images_list(),
                    "description_short": self.description_short,
                    "description_long": self.descripton_long,
                    "coordinates": {
                        "lng": float(self.lng),
                        "lat": float(self.lat),
                    }
                }


class Image(models.Model):
    image = models.ImageField()
    position = models.PositiveSmallIntegerField(default=0)
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)

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
