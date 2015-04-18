# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0012_auto_20150402_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('beer_title', models.CharField(max_length=20, blank=True)),
                ('beer_slug', models.CharField(max_length=20, blank=True)),
                ('beer_pic', models.ImageField(upload_to=b'', verbose_name=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Beers',
        ),
    ]
