# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('subject', models.CharField(max_length=128)),
                ('sender', models.EmailField(max_length=254)),
                ('created', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created'],
                'db_table': 'email_message',
            },
        ),
    ]
