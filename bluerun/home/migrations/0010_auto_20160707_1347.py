# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-07 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20160706_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.CharField(default=' ', max_length=15),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
