# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-22 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20180718_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(null=True, upload_to=profiles.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='membership_no',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
