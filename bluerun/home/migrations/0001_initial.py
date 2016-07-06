# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-05 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=100)),
                ('contact_email', models.CharField(max_length=100)),
                ('contact_subject', models.CharField(max_length=200)),
            ],
        ),
    ]
