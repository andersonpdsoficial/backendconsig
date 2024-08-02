# admin/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuração do esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Margem de Crédito e Reservas",
        default_version='v1',
        description="Documentação da API para consulta de margem de crédito e reservas.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,  # Agora, o Swagger não é acessível publicamente
    permission_classes=(permissions.IsAuthenticated,),  # Exige autenticação para acessar o Swagger
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('contrib.urls')),  # Inclui suas URLs do aplicativo 'contrib'
    
    # URLs do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
