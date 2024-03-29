# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-26 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=250)),
                ('sector_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Sectors'),
        ),
    ]
