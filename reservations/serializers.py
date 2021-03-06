from reservations.models import Reservation
from rest_framework import serializers


class ReservationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reservation
        fields = ('id', 'user_id', 'date', 'rating', 'stadium_id') 