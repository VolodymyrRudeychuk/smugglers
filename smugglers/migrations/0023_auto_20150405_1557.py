# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0022_auto_20150405_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='lang',
            field=models.IntegerField(default=None, null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='long',
            field=models.IntegerField(default=None, null=True, editable=False),
            preserve_default=True,
        ),
    ]
