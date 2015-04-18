# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0018_auto_20150404_1906'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Firm',
        ),
    ]
