# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-07 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0029_auto_20160607_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='sip_msg_password',
            field=models.CharField(default='65tk9kvAJ2', max_length=12),
        ),
    ]