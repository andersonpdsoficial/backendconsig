import django_filters

from .models import Servidor


#Filtrar matricula do servidor para pesquisa no frontend
class ServidorFilter(django_filters.FilterSet):
    matricula = django_filters.CharFilter(field_name='matricula', lookup_expr='icontains')
    
    class Meta:
        model = Servidor
        fields = ['matricula']
