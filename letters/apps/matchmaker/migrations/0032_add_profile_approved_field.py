# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-18 08:35
from __future__ import unicode_literals

from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version

    Writer = apps.get_model("matchmaker", "Writer")
    db_alias = schema_editor.connection.alias

    set_profile_approved_for_writers_available_to_pick(Writer, db_alias)
    set_profile_approved_for_writers_with_an_allocation(Writer, db_alias)


def set_profile_approved_for_writers_available_to_pick(Writer, db_alias):
    for writer in Writer.objects.using(db_alias).filter(
            available_to_pick=True):
        writer.profile_approved = True
        writer.save()


def set_profile_approved_for_writers_with_an_allocation(Writer, db_alias):
    for writer in Writer.objects.using(db_alias).filter(
            allocations__isnull=False,
            available_to_pick=False):
        writer.profile_approved = True
        writer.save()


def reverse_func(apps, schema_editor):
    # forwards_func() sets the values for the new field `profile_approved`.
    # In reverse, this field will be deleted so there's no need to change
    # them back.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('matchmaker', '0031_add_allocations_related_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='profile_approved',
            field=models.BooleanField(default=False, help_text="This indicates that we've approved the content of a profile. See also `available_to_pick`"),
        ),
        migrations.AlterField(
            model_name='writer',
            name='available_to_pick',
            field=models.BooleanField(default=False, help_text='This controls whether this writer is visible for readers to to pick. We set it when we first approve a profile and unset it when we allocate them to reader. If they want to write another letter we could set it again.'),
        ),
        migrations.RunPython(forwards_func, reverse_func),

    ]
