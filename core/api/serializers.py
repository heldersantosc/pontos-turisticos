from rest_framework import serializers
from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentario.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    enderecos = EnderecoSerializer()
    descricao_completa = serializers.SerializerMethodField()
    aprovado = serializers.SerializerMethodField(method_name="get_aprovado")

    class Meta:
        model = PontoTuristico
        fields = (
            "nome",
            "descricao",
            "aprovado",
            "atracoes",
            "comentarios",
            "avaliacoes",
            "enderecos",
            "foto",
            "descricao_completa",
            "nome_descricao",
        )

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)

    def get_aprovado(self, obj):
        return "Sim" if obj.aprovado == True else "Não"
