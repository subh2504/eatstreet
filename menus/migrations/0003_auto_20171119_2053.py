# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_item_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='contents',
            field=models.TextField(blank=True, help_text='Seprate each items by comma', null=True),
        ),
    ]
