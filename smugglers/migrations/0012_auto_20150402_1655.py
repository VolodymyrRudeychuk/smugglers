# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smugglers', '0011_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beers',
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
            name='Beer',
        ),
    ]
