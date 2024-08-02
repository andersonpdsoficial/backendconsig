# contrib/serializers.py

from rest_framework import serializers
from .models import Consignataria, Servidor, ConsultaMargemAthenas, Reserva
import requests

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = '__all__'

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    # Adicionando um campo para a matrícula
    matricula = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'

    def create(self, validated_data):
        matricula = validated_data.pop('matricula', None)
        
        # Fazendo a chamada à API externa se a matrícula for fornecida
        if matricula:
            headers = {
                "Authorization": "Token E3B8B8F271BF233A0A8D2657A1D3FA06"
            }

            response = requests.get(
                f"https://athenas.defensoria.ro.def.br/api/consignado/?matricula={matricula}",
                headers=headers
            )

            if response.status_code == 200:
                data = response.json()
                if data['count'] > 0:
                    resultado = data['results'][0]
                    # Adiciona os dados da API externa ao validated_data
                    validated_data['margem_total'] = resultado['margem_consignada_total']
                    validated_data['margem_disponivel'] = resultado['margem_consignada_livre']
                else:
                    raise serializers.ValidationError("Nenhum resultado encontrado para a matrícula fornecida.")
            else:
                raise serializers.ValidationError("Erro ao consultar a API externa")

        # Cria a instância do modelo com os dados validados
        consulta = ConsultaMargemAthenas.objects.create(**validated_data)
        return consulta

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
