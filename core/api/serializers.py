from rest_framework import serializers
from atracoes.api.serializers import AtracaoSerializer
from atracoes.models import Atracao
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentario.api.serializers import ComentarioSerializer
from enderecos.api.serializers import EnderecoSerializer
from core.models import PontoTuristico
from enderecos.models import Endereco


class PontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)
    avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
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
        read_only_fields = ["comentarios", "avaliacoes"]

    def cria_atracoes(self, atracoes, ponto_turistico):
        for atracao in atracoes:
            nova_atracao = Atracao.objects.create(**atracao)
            ponto_turistico.atracoes.add(nova_atracao)

    def create(self, validated_data):
        atracoes = validated_data["atracoes"]
        enderecos = validated_data["enderecos"]

        del validated_data["atracoes"]
        del validated_data["enderecos"]

        ponto_turistico = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto_turistico)

        endereco = Endereco.objects.create(**enderecos)
        ponto_turistico.endereco = endereco
        ponto_turistico.save()

        return ponto_turistico

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)

    def get_aprovado(self, obj):
        return "Sim" if obj.aprovado == True else "Não"
