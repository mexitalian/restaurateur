# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 05:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170125_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='specials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.MenuSection'),
        ),
    ]
