# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-15 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0036_auto_20160615_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='voip1_rule1_pattern',
            field=models.CharField(blank=True, default='_0X.', max_length=12, null=True),
        ),
    ]