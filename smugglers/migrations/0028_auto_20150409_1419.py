# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0027_auto_20150405_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='zoom',
            field=models.IntegerField(default=10, choices=[(1, 4), (2, 8), (3, 10)]),
            preserve_default=True,
        ),
    ]
