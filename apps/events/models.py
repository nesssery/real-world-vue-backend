from django.db import models
from apps.utils.models import Timestamp


class Categorie(Timestamp, models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Event(Timestamp, models.Model):
    category = models.ForeignKey(Categorie, to_field="title", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} {self.category}'
