# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 22:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectSection', '0002_remove_projects_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
