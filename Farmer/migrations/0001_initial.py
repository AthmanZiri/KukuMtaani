# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-11-11 23:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=13)),
                ('location', models.CharField(max_length=255)),
                ('produce', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
