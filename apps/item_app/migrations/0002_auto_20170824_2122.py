# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-24 21:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_item', to='login_app.User'),
        ),
    ]