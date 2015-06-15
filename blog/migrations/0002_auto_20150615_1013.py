# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['-fecha'], 'verbose_name': 'Mi Entrada', 'verbose_name_plural': 'Todas mis entradas'},
        ),
        migrations.AddField(
            model_name='entrada',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Publicado?'),
        ),
    ]
