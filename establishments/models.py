import uuid
from django.db import models


class Establishment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    logo = models.CharField(max_length=300)

    class Meta:
        verbose_name = ("Establishment")
        verbose_name_plural = ("Establishments")

    def __str__(self):
        return self.name
    