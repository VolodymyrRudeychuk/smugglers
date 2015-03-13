# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0003_auto_20150312_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='pictures',
            field=models.ImageField(upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
