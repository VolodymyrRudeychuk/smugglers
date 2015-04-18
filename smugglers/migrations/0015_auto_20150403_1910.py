# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0014_beer_beer_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='beer_pic',
            field=models.ImageField(width_field=10, upload_to=b''),
            preserve_default=True,
        ),
    ]
