# Generated by Django 4.1.1 on 2022-09-27 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0023_cliente_alter_cabecera_fecha_cobro_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='estado',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección'),
        ),
    ]
