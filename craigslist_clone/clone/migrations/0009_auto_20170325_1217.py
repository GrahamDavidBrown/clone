# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 12:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clone', '0008_auto_20170325_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clone.Sub_Category'),
        ),
    ]
