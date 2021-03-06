# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trading', '0002_auto_20160617_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('stock_name', models.CharField(max_length=100)),
                ('entry_price', models.IntegerField()),
                ('target', models.IntegerField()),
                ('stop_loss', models.IntegerField()),
                ('time_frame', models.CharField(max_length=100)),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('cash_intra', models.BooleanField(default=False)),
                ('cash_positional', models.BooleanField(default=False)),
                ('stock_future', models.BooleanField(default=False)),
                ('option_calls_covered', models.BooleanField(default=False)),
                ('multi_beggar', models.BooleanField(default=False)),
            ],
        ),
    ]
