from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import NumberFilter, FilterSet
from reservations.serializers import ReservationSerializer
from reservations.models import Reservation
from rest_framework.response import Response
from rest_framework.decorators import detail_route, action


class ReservationFilter(FilterSet):
    month = NumberFilter(field_name='date', lookup_expr='month')
    year = NumberFilter(field_name='date', lookup_expr='year')
    day = NumberFilter(field_name='date', lookup_expr='day')

    class Meta:
        model = Reservation
        fields = ['user_id', 'month', 'year', 'day']


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_class = ReservationFilter