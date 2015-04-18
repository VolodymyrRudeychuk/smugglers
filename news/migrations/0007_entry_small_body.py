# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150410_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='small_body',
            field=models.TextField(max_length=167, blank=True),
            preserve_default=True,
        ),
    ]
