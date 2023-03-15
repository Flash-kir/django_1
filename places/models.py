import requests

from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)

    def __str__(self) -> str:
        return self.title

    def get_images_list(self):
        return [image.image.url for image in self.images.all()]


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
