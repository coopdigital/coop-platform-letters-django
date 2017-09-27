# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-27 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sender',
            name='age',
            field=models.IntegerField(help_text='This will help people who want to receive a letter make a decision about who writes to them.'),
        ),
        migrations.AlterField(
            model_name='sender',
            name='first_name',
            field=models.CharField(help_text='We only ask for your first name so that your identity is protected.', max_length=128),
        ),
        migrations.AlterField(
            model_name='sender',
            name='profile_story',
            field=models.TextField(help_text='Write a couple of sentences to help readers understand how you got into debt. This will help them pick somebody they can relate to.'),
        ),
    ]
