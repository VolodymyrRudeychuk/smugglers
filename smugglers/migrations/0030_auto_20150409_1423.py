# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0029_auto_20150409_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='zoom',
            field=models.IntegerField(blank=True),
            preserve_default=True,
        ),
    ]
