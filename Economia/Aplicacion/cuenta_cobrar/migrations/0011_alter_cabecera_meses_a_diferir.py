# Generated by Django 4.1.1 on 2022-09-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0010_cabecera_cuota_mensual_alter_cabecera_deuda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabecera',
            name='meses_a_diferir',
            field=models.CharField(choices=[('3 meses', 1), ('6 meses', 2), ('9 meses', '9 meses'), ('12 meses', '12 meses'), ('24 meses', '5')], default='3 meses', max_length=200),
        ),
    ]
