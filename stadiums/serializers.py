from stadiums.models import Stadium
from rest_framework import serializers


class StadiumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stadium
        fields = ('id', 'type', 'rating', 'photo', 'description', 'cost',
                  'opening','closing','establishment')
