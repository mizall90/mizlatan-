# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-04 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20190430_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='junkiri',
            name='post',
        ),
        migrations.AddField(
            model_name='junkiri',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, upload_to='Junkiri/%Y/%m', verbose_name='Junkiri Post'),
        ),
    ]
