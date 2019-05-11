# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_delete_show_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='junkiri',
            name='author_name',
            field=models.CharField(max_length=50, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='batch',
            field=models.CharField(max_length=50, verbose_name='Batch'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='is_starring',
            field=models.BooleanField(default=False, help_text='Star Post will be shown on home page.', verbose_name='Star Post'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='photo',
            field=models.ImageField(blank=True, max_length=255, upload_to='Junkiri/%Y/%m', verbose_name='Junkiri Image'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='post_dt',
            field=models.DateTimeField(blank=True, verbose_name='Post Date'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='post_title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='publish',
            field=models.BooleanField(default=False, help_text='Latest 6 post that are marked publish will be shown on Junikiri list page.', verbose_name='Publish'),
        ),
        migrations.AlterField(
            model_name='junkiri',
            name='quote',
            field=models.TextField(blank=True, null=True, verbose_name='Post Discription'),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(blank=True, choices=[('president', 'President'), ('vice president', 'Vice President'), ('outreach', 'Outreach'), ('Treasurer', 'Treasurer'), ('secretary', 'Secretary'), ('joint secretary', 'Joint Secretary')], max_length=50, null=True),
        ),
    ]
