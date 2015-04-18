# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0013_auto_20150403_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='beer_text',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
