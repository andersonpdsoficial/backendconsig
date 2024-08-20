import django_filters
from .models import ConsultaMargemAthenas

class ConsultaMargemAthenasFilter(django_filters.FilterSet):
    matricula = django_filters.CharFilter(field_name='servidor__matricula', lookup_expr='iexact')

    class Meta:
        model = ConsultaMargemAthenas
        fields = ['matricula']

