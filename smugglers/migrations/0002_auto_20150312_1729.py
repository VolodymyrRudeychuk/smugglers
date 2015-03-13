# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='history',
            name='slug',
            field=models.SlugField(max_length=150, blank=True),
            preserve_default=True,
        ),
    ]
