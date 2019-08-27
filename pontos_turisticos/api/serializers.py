from rest_framework.serializers import ModelSerializer
from pontos_turisticos.core.models import PontoTuristico


class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['nome', 'descricao','atracoes','comentarios','enderecos']