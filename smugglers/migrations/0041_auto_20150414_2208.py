# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0040_auto_20150414_2202'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Soc',
            new_name='Social',
        ),
    ]
