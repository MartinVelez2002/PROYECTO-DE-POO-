# Generated by Django 4.1.1 on 2022-09-27 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0021_cabecera_saldo_interes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='saldo_interes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Deuda (+10% interés)'),
        ),
    ]
