# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0026_auto_20150405_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='zoom',
            field=models.IntegerField(default=10, choices=[(0, 4), (1, 8), (2, 10)]),
            preserve_default=True,
        ),
    ]
