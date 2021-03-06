# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-12-05 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_remove_default_on_nuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='registration_type',
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='registration_type',
            field=models.CharField(blank=True, choices=[('person', 'Attend in Person'), ('remote', 'Attend via Remote')], default='person', max_length=20),
        ),
    ]
