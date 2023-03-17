from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    description_short = models.TextField(blank=True)
    description_long = HTMLField(blank=True)

    def __str__(self) -> str:
        return self.title


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

    class Meta:
        ordering = ['position']
