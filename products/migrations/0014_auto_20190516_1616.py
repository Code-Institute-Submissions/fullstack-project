# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20190516_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='products.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(related_name='posts', to='products.Review'),
        ),
    ]
