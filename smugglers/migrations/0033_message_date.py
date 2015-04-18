# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0032_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 12, 23, 5, 49, 249857), auto_now_add=True),
            preserve_default=False,
        ),
    ]
