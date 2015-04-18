# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0015_auto_20150403_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beer',
            name='beer_pic',
            field=models.ImageField(upload_to=b'', verbose_name=b''),
            preserve_default=True,
        ),
    ]
