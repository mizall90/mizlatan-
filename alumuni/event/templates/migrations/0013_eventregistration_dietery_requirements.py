# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-12-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0012_add_registration_type_on_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='dietery_requirements',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
