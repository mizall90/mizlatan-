# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-11-29 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_registration_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='department',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='dietary_requirements',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='email_address',
            field=models.EmailField(blank=True, help_text='email address of attendee', max_length=254, verbose_name='attendee email'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='is_hotel',
            field=models.BooleanField(default=False, help_text='will be registering for hotel'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='mobile_phone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='name',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='region',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
