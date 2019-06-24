from django.contrib import admin
from stadiums.models import Stadium

# Register your models here.
@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['description','rating','establishment',]
