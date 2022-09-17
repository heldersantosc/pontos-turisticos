from rest_framework import viewsets
from comentario.api.serializers import ComentarioSerializer
from comentario.models import Comentario
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["comentario"]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
