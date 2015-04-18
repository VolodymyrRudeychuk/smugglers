# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0035_auto_20150413_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sociallinks',
            old_name='gplus',
            new_name='gpl',
        ),
    ]
