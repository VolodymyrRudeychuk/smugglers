# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_entry_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='pics',
            field=models.ImageField(height_field=200, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
