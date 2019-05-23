# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 16:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20190516_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='products.Review'),
        ),
    ]