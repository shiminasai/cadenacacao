# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-06-18 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0010_productosservicios_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizacion',
            name='cobertura',
        ),
    ]
