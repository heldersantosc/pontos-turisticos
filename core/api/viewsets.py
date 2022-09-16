from rest_framework import viewsets
from rest_framework.response import Response
from core.models import PontoTuristico
from core.api.serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    # sobrescreve método GET quando por id
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=False)

    # sobrescreve método GET quando em lista
    def list(self, request, *args, **kwargs):
        response = PontoTuristico.objects.filter(aprovado=False)
        serializer = PontoTuristicoSerializer(response, many=True)
        return Response(serializer.data)

    # sobrescreve método POST
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({"msg": "Criado com sucesso"})

    # sobrescreve método DELETE
    def destroy(self, request, *args, **kwargs):
        return Response({"msg": "Evitando deletar"})
        