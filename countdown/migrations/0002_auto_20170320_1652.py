# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 16:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countdown', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_slug', models.CharField(max_length=50)),
                ('management_slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='countdown',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='countdown.Countdown'),
            preserve_default=False,
        ),
    ]
