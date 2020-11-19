from django.db import models


class Timestamp(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)

    class Meta:
        abstract = True
