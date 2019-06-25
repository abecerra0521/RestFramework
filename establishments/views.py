from rest_framework import viewsets
from establishments.serializers import EstablishmentSerializer
from establishments.models import Establishment
from stadiums.serializers import StadiumSerializer
from stadiums.models import Stadium
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer

    @action(methods=['get'], detail=True)
    def stadiums(self, request, pk=None):
        stadiums = Stadium.objects.filter(establishment_id=pk).values()
        return Response(stadiums)