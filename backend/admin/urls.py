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
        description="API para consulta de margem de crédito e reservas. Esta API requer autenticação para acessar os endpoints.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@exemplo.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,  # Swagger não é acessível publicamente
    permission_classes=(permissions.IsAuthenticated,),  # Requer autenticação para acessar o Swagger
)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL do Django Admin
    path('api/', include('contrib.urls')),  # Inclui suas URLs do aplicativo 'contrib' para a API
    
    # URLs do Swagger e Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
