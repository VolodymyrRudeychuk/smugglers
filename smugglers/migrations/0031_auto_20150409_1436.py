# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0030_auto_20150409_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='mini_title',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='map',
            name='title',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
