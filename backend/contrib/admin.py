from django.contrib import admin
from .models import Consignataria, Servidor, ConsultaMargemAthenas, Reserva

@admin.register(Consignataria)
class ConsignatariaAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf_cnpj")  # Campos exibidos na lista
    search_fields = ("nome", "cpf_cnpj")  # Campos pesquisáveis


@admin.register(Servidor)
class ServidorAdmin(admin.ModelAdmin):
    list_display = ("nome", "matricula")  # Campos exibidos na lista
    search_fields = ("nome", "matricula")  # Campos pesquisáveis


@admin.register(ConsultaMargemAthenas)
class ConsultaMargemAthenasAdmin(admin.ModelAdmin):
    list_display = (
        "servidor",
        "consignataria",
        "margem_total",
        "margem_disponivel",
    )  # Campos exibidos na lista
    search_fields = (
        "servidor__nome",
        "consignataria__nome",
    )  # Campos pesquisáveis (acessando relacionamentos)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        "contrato",
        "valor",
        "situacao",
        "prazo_inicial",
        "prazo_final",
        "cadastrado_por",
        "email",
    )  # Campos exibidos na lista
    search_fields = ("contrato",)  # Campos pesquisáveis
    list_filter = ("situacao",)  # Filtros disponíveis
    readonly_fields = (
        "cadastrado_por",
        "cadastrado_em",
        "modificado_por",
        "modificado_em",
    )  # Campos somente leitura
