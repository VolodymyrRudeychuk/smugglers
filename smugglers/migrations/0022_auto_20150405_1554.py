# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0021_auto_20150405_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='lang',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='long',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
