# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-12-05 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_eventregistration_dietery_requirements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventregistration',
            name='dietary_requirements',
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='comments',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
