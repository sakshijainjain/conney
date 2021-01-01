# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-12 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmgmt', '0002_roombooking_number_of_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('extra_instructions', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='roombooking',
            name='food_type',
        ),
    ]