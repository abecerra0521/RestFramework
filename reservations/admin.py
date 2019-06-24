from django.contrib import admin
from reservations.models import Reservation

# Register your models here.
@admin.register(Reservation)
class ReservationsAdmin(admin.ModelAdmin):
    list_display = ['user','date','stadium',]

