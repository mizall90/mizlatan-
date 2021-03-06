# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-12-01 09:42
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_update_event_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/static/img/bg.jpg', help_text='Image thumbnail for event.', upload_to='event'),
        ),
        migrations.AddField(
            model_name='eventregistration',
            name='nuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
