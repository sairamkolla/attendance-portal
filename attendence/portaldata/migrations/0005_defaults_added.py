# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portaldata', '0004_remove_schedule_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='defaults_added',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
