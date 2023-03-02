from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title


class Image(models.Model):
    image = models.ImageField()
    place = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.pk} {self.place}'
