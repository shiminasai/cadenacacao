# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-29 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20190618_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='acerca',
            field=models.TextField(blank=True, editable=False, null=True, verbose_name='Texto Cadena cacao'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='politica_condicines',
            field=models.TextField(blank=True, null=True, verbose_name='politicas y condiciones'),
        ),
    ]
