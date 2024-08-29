
# Bibliotecas de terceiros
from django.db.models import QuerySet, Manager


class AuditoriaBaseQuerySet(QuerySet):
    def ativos(self):
        return self.filter(desativado_por=None)

    def inativos(self):
        return self.exclude(desativado_por=None)


class AuditoriaBaseManager(Manager.from_queryset(AuditoriaBaseQuerySet)):
    pass
