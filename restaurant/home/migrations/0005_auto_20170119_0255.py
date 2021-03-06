# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_menupage'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPageSectionPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'verbose_name': 'section placement',
                'verbose_name_plural': 'section placements',
            },
        ),
        migrations.RemoveField(
            model_name='menupage',
            name='section',
        ),
        migrations.AddField(
            model_name='menupagesectionplacement',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='section_placements', to='home.MenuPage'),
        ),
        migrations.AddField(
            model_name='menupagesectionplacement',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='home.MenuSection'),
        ),
    ]
