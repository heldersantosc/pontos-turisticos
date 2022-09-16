from rest_framework import viewsets
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer