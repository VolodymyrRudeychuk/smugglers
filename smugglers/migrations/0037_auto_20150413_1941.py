# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0036_auto_20150413_1930'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SocialLinks',
            new_name='Soc',
        ),
    ]
