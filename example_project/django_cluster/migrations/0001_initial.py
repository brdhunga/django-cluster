# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 04:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_json', models.TextField(blank=True, default='')),
            ],
        ),
    ]
