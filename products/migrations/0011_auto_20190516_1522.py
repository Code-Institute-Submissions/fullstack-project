# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190516_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_name',
        ),
        migrations.AddField(
            model_name='brand',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='products.Product'),
        ),
    ]