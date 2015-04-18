# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0034_auto_20150413_1833'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Social',
            new_name='SocialLinks',
        ),
    ]
