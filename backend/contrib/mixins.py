# contrib/mixins.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class AuditoriaAbstractMixin(models.Model):
    """
    Classe mixin para auditoria das operações de cadastro e modificação.
    """
    cadastrado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(app_label)s_%(class)s_cadastrado_por",
    )
    cadastrado_em = models.DateTimeField(auto_now_add=True, null=True)
    modificado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(app_label)s_%(class)s_modificado_por",
    )
    modificado_em = models.DateTimeField(auto_now=True, null=True)
    desativado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="%(app_label)s_%(class)s_desativado_por",
        blank=True,
    )
    desativado_em = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    @property
    def ativo(self):
        """Verifica se o objeto está ativo."""
        return self.desativado_em is None

    def desativar(self, usuario, data_hora=None):
        """Desativa o objeto e registra quem desativou."""
        if not data_hora:
            data_hora = timezone.now()

        self.modificado_por = usuario
        self.modificado_em = data_hora

        self.desativado_por = usuario
        self.desativado_em = data_hora
        self.save()

    def reativar(self, usuario, data_hora=None):
        """Reativa o objeto e registra quem reativou."""
        if not data_hora:
            data_hora = timezone.now()

        self.modificado_por = usuario
        self.modificado_em = data_hora

        self.desativado_por = None
        self.desativado_em = None
        self.save()
