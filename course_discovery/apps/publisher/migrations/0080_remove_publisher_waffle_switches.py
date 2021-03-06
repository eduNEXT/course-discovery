# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-13 09:18
from __future__ import unicode_literals

from django.db import migrations

WAFFLES = ('publisher_hide_features_for_pilot', 'publisher_add_instructor_feature',
           'publisher_comment_widget_feature', 'publisher_approval_widget_feature',
           'publisher_history_widget_feature')


def delete_switches(apps, schema_editor):
    """Delete the publisher switches."""
    Switch = apps.get_model('waffle', 'Switch')
    Switch.objects.filter(name__in=WAFFLES).delete()


def create_switches(apps, schema_editor):
    """Create the publisher switches if they do not already exist."""
    Switch = apps.get_model('waffle', 'Switch')
    for waffle in WAFFLES:
        Switch.objects.get_or_create(name=waffle, defaults={'active': False})


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0079_course_url_slug'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(delete_switches, create_switches),
    ]
