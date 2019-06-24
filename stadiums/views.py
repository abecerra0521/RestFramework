from rest_framework import viewsets
from stadiums.serializers import StadiumSerializer
from stadiums.models import Stadium


# Create your views here.
class StadiumViewSet(viewsets.ModelViewSet):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer