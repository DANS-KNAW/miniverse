# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datafiles', '0004_auto_20160802_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('label', models.CharField(max_length=255)),
                ('restricted', models.NullBooleanField()),
                ('version', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'filemetadata',
                'managed': False,
            },
        ),
    ]
