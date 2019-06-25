from rest_framework import viewsets
from reservations.serializers import ReservationSerializer
from reservations.models import Reservation


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
