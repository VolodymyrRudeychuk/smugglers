# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0004_history_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='pictures',
            field=models.ImageField(upload_to=b''),
            preserve_default=True,
        ),
    ]
