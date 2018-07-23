# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-21 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(verbose_name=models.TextField()),
        ),
    ]