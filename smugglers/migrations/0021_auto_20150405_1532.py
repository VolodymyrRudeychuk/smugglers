# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0020_firm'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Firm',
            new_name='Map',
        ),
    ]
