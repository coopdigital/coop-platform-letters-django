# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-10 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0022_rename_baseline_wellbeing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reader',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ('-created_at',)},
        ),
    ]