# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-06 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0014_reader_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='get_started_email_sent',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
