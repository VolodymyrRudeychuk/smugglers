# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0007_auto_20150313_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Story',
            new_name='TitleHistory',
        ),
    ]
