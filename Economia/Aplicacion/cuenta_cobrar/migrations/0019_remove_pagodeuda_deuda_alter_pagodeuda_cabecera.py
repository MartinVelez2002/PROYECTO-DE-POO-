# Generated by Django 4.1.1 on 2022-09-24 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta_cobrar', '0018_alter_pagodeuda_cabecera'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagodeuda',
            name='deuda',
        ),
        migrations.AlterField(
            model_name='pagodeuda',
            name='cabecera',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cuenta_cobrar.cabecera', verbose_name='Cliente'),
        ),
    ]
