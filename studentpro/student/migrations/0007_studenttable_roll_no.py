# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20170926_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttable',
            name='roll_no',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]