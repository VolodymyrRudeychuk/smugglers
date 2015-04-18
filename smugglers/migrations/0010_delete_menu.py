# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0009_menu'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
