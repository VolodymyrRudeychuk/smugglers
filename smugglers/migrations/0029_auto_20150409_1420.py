# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0028_auto_20150409_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='zoom',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
