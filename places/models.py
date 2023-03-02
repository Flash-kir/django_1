from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.title
