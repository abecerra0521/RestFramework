import uuid
from django.db import models
from django.contrib.auth.models import User

from stadiums.models import Stadium


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    rating = models.IntegerField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Reservation")
        verbose_name_plural = ("Reservations")
