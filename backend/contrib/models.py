from django.db import models
from .mixins import AuditoriaAbstractMixin  # Importando o mixin de auditoria

class Consignataria(AuditoriaAbstractMixin):
    nome = models.CharField(max_length=256, null=False, blank=False)
    cpf_cnpj = models.CharField(max_length=14, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class Servidor(AuditoriaAbstractMixin):
    nome = models.CharField(max_length=255, null=False, blank=False)
    matricula = models.CharField(max_length=9, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome

class ConsultaMargemAthenas(AuditoriaAbstractMixin):
    margem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    servidor = models.ForeignKey(Servidor, on_delete=models.PROTECT, null=False, blank=False)
    consignataria = models.ForeignKey(Consignataria, on_delete=models.PROTECT, null=False, blank=False)

    def __str__(self):
        return f"Consulta {self.servidor} - {self.consignataria}"

class Reserva(AuditoriaAbstractMixin):
    """
    Modelo para armazenar as reservas.
    """
    EM_ANALISE = 0
    DEFERIDO = 1
    INDEFERIDO = 2
    EXPIRADO = 3

    SITUACOES = (
        (EM_ANALISE, "EM ANÁLISE"),
        (DEFERIDO, "DEFERIDO"),
        (INDEFERIDO, "INDEFERIDO"),
        (EXPIRADO, "EXPIRADO"),
    )

    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    consulta = models.ForeignKey(ConsultaMargemAthenas, on_delete=models.PROTECT, null=False, blank=False)
    prazo_inicial = models.DateTimeField()
    prazo_final = models.DateTimeField()
    situacao = models.SmallIntegerField(choices=SITUACOES, blank=False, null=False, default=EM_ANALISE)
    contrato = models.CharField(max_length=255, unique=True, null=False, blank=False)
    matricula = models.CharField(max_length=9, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    margem_disponivel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    margem_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vencimento_parcela = models.DateField(null=True, blank=True)
    folha_desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_financiado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    liquido_liberado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    liberacao_credito = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cet = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    quantidade_parcelas = models.IntegerField(null=True, blank=True)
    valor_parcelas = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    juros_mensal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valor_iof = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    carencia_dias = models.IntegerField(null=True, blank=True)
    valor_carencia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    vinculo = models.CharField(max_length=255, null=True, blank=True)
    margem_antes = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    margem_apos = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)  # Novo campo de e-mail

    def __str__(self):
        return f"Reserva {self.contrato} - {self.valor}"
