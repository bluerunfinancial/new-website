# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-06 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160706_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 7, 6, 9, 13, 8, 831861, tzinfo=utc)),
        ),
    ]