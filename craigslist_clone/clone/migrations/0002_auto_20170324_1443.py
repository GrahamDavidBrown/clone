# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 14:20
from __future__ import unicode_literals
from django.contrib.auth.models import User
from clone.models import City
from django.db import migrations


def create_a_city(apps, schema_editor):
    city = City.objects.create(name="durham", region="southeast")
    city.save()


class Migration(migrations.Migration):
    dependencies = [
        ('clone', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_a_city)
    ]
