from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from .views import ConsignatariaViewSet, ServidorViewSet, ConsultaMargemAthenasViewSet, ReservaViewSet

# Cria um router padrão para registrar os viewsets
router = DefaultRouter()
router.register(r'consignatarias', ConsignatariaViewSet)
router.register(r'servidores', ServidorViewSet)
router.register(r'consultas-margem-athenas', ConsultaMargemAthenasViewSet)  # Corrigido nome para ser mais consistente
router.register(r'reservas', ReservaViewSet)

# Define as URLs do aplicativo 'contrib'
urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs geradas pelo router
]
