# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingest_configs',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('data_source_name', models.CharField(max_length=60)),
                ('data_source_descr', models.CharField(max_length=254)),
                ('ingest_url', models.URLField()),
                ('ingest_type', models.IntegerField()),
                ('access_key_label', models.CharField(max_length=30)),
                ('access_key_value', models.CharField(max_length=254)),
                ('ingest_format', models.IntegerField()),
            ],
        ),
    ]
