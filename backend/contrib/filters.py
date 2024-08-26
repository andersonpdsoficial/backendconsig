import django_filters
from .models import ConsultaMargemAthenas


#Filtrar matricula do servidor para pesquisa no frontend
class ConsultaMargemAthenasFilter(django_filters.FilterSet):
    servidor__matricula = django_filters.CharFilter(field_name='servidor__matricula', lookup_expr='iexact')
    
    class Meta:
        model = ConsultaMargemAthenas
        fields = '__all__'
