# Generated by Django 2.2.1 on 2019-07-24 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20190713_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 7, 24, 11, 59, 38, 900410)),
        ),
    ]
