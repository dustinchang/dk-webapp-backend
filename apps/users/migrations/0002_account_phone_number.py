# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
