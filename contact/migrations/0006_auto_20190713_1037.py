# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-13 05:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20190713_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 13, 10, 37, 15, 892876)),
        ),
    ]
