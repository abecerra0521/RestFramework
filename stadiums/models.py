import uuid
from django.db import models
from establishments.models import Establishment


# Create your models here.
class Stadium(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50)
    rating = models.IntegerField()
    photo = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    opening = models.TimeField()
    closing = models.TimeField()
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Stadium")
        verbose_name_plural = ("Stadiums")

    def __str__(self):
        return self.description
