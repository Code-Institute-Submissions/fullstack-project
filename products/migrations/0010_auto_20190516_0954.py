# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_product_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='products.Brand'),
        ),
    ]
