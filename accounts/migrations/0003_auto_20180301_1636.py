# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-01 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='token',
            name='uid',
            field=models.CharField(default=uuid.uuid4, max_length=40),
        ),
    ]
