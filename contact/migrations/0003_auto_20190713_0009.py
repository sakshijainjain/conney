# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-12 18:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20190712_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 13, 0, 9, 12, 797767)),
        ),
    ]