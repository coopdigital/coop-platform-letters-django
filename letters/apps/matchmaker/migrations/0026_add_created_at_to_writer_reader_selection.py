# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-10 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0025_rename_pairing'),
    ]

    operations = [
        migrations.AddField(
            model_name='writerreaderselection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
