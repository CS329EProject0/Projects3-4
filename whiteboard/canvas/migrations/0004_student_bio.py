# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canvas', '0003_student_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bio',
            field=models.CharField(default='No bio', max_length=100),
        ),
    ]