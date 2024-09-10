# Generated by Django 5.0.8 on 2024-09-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contrib", "0003_alter_reserva_situacao"),
    ]

    operations = [
        migrations.AddField(
            model_name="reserva",
            name="carencia_dias",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="cet",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="cpf",
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="folha_desconto",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="juros_mensal",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="liberacao_credito",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="liquido_liberado",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="margem_antes",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="margem_apos",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="margem_disponivel",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="margem_total",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="matricula",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="nome",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="observacoes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="quantidade_parcelas",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="total_financiado",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="valor_carencia",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="valor_iof",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="valor_parcelas",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AddField(
            model_name="reserva",
            name="vencimento_parcela",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="reserva",
            name="vinculo",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
