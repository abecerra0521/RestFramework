from rest_framework import viewsets
from establishments.serializers import EstablishmentSerializer
from establishments.models import Establishment

# Create your views here.
class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    