# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-30 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0043_auto_20160630_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='api_key',
            field=models.CharField(default='**autogeneration**', max_length=30),
        ),
    ]