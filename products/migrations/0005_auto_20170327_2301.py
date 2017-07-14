# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-27 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0004_auto_20170327_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='categories.Category'),
        ),
    ]
