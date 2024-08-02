# contrib/views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Consignataria, Servidor, ConsultaMargemAthenas, Reserva
from .serializers import ConsignatariaSerializer, ServidorSerializer, ConsultaMargemAthenasSerializer, ReservaSerializer
import requests
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated  

class ConsignatariaViewSet(viewsets.ModelViewSet):
    queryset = Consignataria.objects.all()
    serializer_class = ConsignatariaSerializer


class ServidorViewSet(viewsets.ModelViewSet):
    queryset = Servidor.objects.all()
    serializer_class = ServidorSerializer


class ConsultaMargemAthenasViewSet(viewsets.ModelViewSet):
    queryset = ConsultaMargemAthenas.objects.all()
    serializer_class = ConsultaMargemAthenasSerializer

    def create(self, request, *args, **kwargs):
        matricula = request.data.get('matricula')
        id_consignataria = request.data.get('id_consignataria')

        headers = {
            "Authorization": "Token E3B8B8F271BF233A0A8D2657A1D3FA06"
        }

        response = requests.get(
            f"https://athenas.defensoria.ro.def.br/api/consignado/?matricula={matricula}&id={id_consignataria}",
            headers=headers
        )

        if response.status_code == 200:
            data = response.json()
            if data['count'] > 0:
                resultado = data['results'][0]
                margem_total = resultado['margem_consignada_total']
                margem_disponivel = resultado['margem_consignada_livre']

                servidor = Servidor.objects.get(matricula=matricula)
                consignataria = Consignataria.objects.get(id=id_consignataria)

                consulta = ConsultaMargemAthenas.objects.create(
                    margem_total=margem_total,
                    margem_disponivel=margem_disponivel,
                    servidor=servidor,
                    consignataria=consignataria,
                    cadastrado_por=request.user  # Usando o usuário autenticado
                )

                serializer = self.get_serializer(consulta)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Nenhum resultado encontrado."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Erro ao consultar a API externa"}, status=response.status_code)

    def retrieve(self, request, *args, **kwargs):
        matricula = request.query_params.get('matricula', None)
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
                    return Response(data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Nenhum resultado encontrado."}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Erro ao consultar a API externa"}, status=response.status_code)

        return Response({"error": "Matrícula não fornecida."}, status=status.HTTP_400_BAD_REQUEST)


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]  # Adiciona proteção de visualização

    def create(self, request, *args, **kwargs):
        usuario_atual = request.user  # Obtém o usuário atual
        reserva = Reserva(**request.data, cadastrado_por=usuario_atual)  # Usando o usuário autenticado
        reserva.save()
        serializer = self.get_serializer(reserva)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        usuario_atual = request.user  # Obtém o usuário atual
        reserva = self.get_object()
        reserva.modificado_por = usuario_atual  # Usando o usuário autenticado
        for attr, value in request.data.items():
            setattr(reserva, attr, value)
        reserva.save()
        serializer = self.get_serializer(reserva)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        usuario_atual = request.user  # Obtém o usuário atual
        reserva = self.get_object()
        reserva.desativar(usuario_atual)  # Usando o usuário autenticado
        return Response(status=status.HTTP_204_NO_CONTENT)
