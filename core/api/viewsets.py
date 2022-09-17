from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer
from core.api.pagination import PontosTuristicosSetPagination


class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    pagination_class = PontosTuristicosSetPagination

    # sobrescreve método GET por padrão
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=False)

    # sobrescreve método GET quando em ID <pk>
    def retrieve(self, request, *args, **kwargs):
        response = PontoTuristico.objects.filter(aprovado=False).first()
        serializer = PontoTuristicoSerializer(response)
        return Response(serializer.data)

    # sobrescreve método GET quando em lista
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    # sobrescreve método POST
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"msg": "Criado com sucesso"})

    # sobrescreve método DELETE
    def destroy(self, request, *args, **kwargs):
        return Response({"msg": "Evitando deletar"})

    @action(methods=["post"], detail=True)
    def denunciar(self, request, **kwargs):
        return Response({"msg": "Denunciado: {id}".format(id=kwargs["pk"])})
