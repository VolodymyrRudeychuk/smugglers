# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0016_auto_20150403_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100, blank=True)),
                ('street', models.CharField(max_length=100, blank=True)),
                ('house_number', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
