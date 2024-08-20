from rest_framework import serializers
from .models import Consignataria, Servidor, ConsultaMargemAthenas, Reserva
import requests

class ConsignatariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = [
            'id', 'nome', 'cpf_cnpj'
        ]

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = [
            'id', 'nome', 'matricula'
        ]

class ConsultaMargemAthenasSerializer(serializers.ModelSerializer):
    margem_total = serializers.CharField(required=True)
    margem_disponivel = serializers.CharField(required=True)

    class Meta:
        model = ConsultaMargemAthenas
        fields = ['id', 'margem_total', 'margem_disponivel', 'servidor', 'consignataria']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

# Serializadores para a versão 2

class ConsignatariaSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Consignataria
        fields = 'id', 'nome', 'cpf_cnpj'

class ServidorSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class ConsultaMargemAthenasSerializerV2(serializers.ModelSerializer):
    matricula = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'

    def create(self, validated_data):
        matricula = validated_data.pop('matricula', None)
        
        if matricula:
            headers = {
                "Authorization": "Token 682770e6bbe57c2736138619840a564bd0775486"
            }

            response = requests.get(
                f"https://athenas.defensoria.ro.def.br/api/consignado/?matricula={matricula}",
                headers=headers
            )

            if response.status_code == 200:
                data = response.json()
                if data['count'] > 0:
                    resultado = data['results'][0]
                    validated_data['margem_total'] = resultado['margem_consignada_total']
                    validated_data['margem_disponivel'] = resultado['margem_consignada_livre']
                else:
                    raise serializers.ValidationError("Nenhum resultado encontrado para a matrícula fornecida.")
            else:
                raise serializers.ValidationError("Erro ao consultar a API externa")

        consulta = ConsultaMargemAthenas.objects.create(**validated_data)
        return consulta

class ReservaSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
