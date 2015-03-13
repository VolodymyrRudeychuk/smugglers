# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0005_auto_20150313_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='head_slug',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='history',
            name='head_title',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='history',
            name='pictures',
            field=models.ImageField(upload_to=b'', verbose_name=b''),
            preserve_default=True,
        ),
    ]
