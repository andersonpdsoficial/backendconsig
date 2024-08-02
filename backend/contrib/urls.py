# contrib/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConsignatariaViewSet, ServidorViewSet, ConsultaMargemAthenasViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'consignatarias', ConsignatariaViewSet)
router.register(r'servidores', ServidorViewSet)
router.register(r'consultas-margem-athenas', ConsultaMargemAthenasViewSet)  # Nome alterado para ser mais consistente
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
