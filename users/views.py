from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from users.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from reservations.models import Reservation
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)


    @action(methods=['get'], detail=True)
    def getUserByToken(self, request, pk=None):
        user = Token.objects.filter(key=pk).values().first()
        return Response(user)

    
    @action(methods=['get'], detail=True)
    def reservations(self, request, pk=None):
        reservations = Reservation.objects.filter(user_id=pk).values()
        return Response(reservations)