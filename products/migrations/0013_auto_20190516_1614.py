# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20190516_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.ManyToManyField(related_name='products', to='products.Review'),
        ),
    ]
