# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 22:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='completed',
        ),
    ]
