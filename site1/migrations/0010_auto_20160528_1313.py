# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site1', '0009_ata_box_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ata_box',
            name='customer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]