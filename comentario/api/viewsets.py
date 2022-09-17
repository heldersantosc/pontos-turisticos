from rest_framework import viewsets
from comentario.api.serializers import ComentarioSerializer
from comentario.models import Comentario
from rest_framework import filters


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["comentario"]
