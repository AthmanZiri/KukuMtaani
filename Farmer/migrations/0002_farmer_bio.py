# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-12 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='bio',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
