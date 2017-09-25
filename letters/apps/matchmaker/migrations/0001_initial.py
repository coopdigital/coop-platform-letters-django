# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-25 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('profile_story', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
