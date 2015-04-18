# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150311_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='pics',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
