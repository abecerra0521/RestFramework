from establishments.models import Establishment
from rest_framework import serializers
from django.core.serializers.json import Serializer


class EstablishmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Establishment
        fields = ('id', 'name', 'address', 'lat', 'lon', 'logo',)