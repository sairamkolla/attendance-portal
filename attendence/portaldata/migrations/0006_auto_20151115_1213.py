# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portaldata', '0005_defaults_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conducted_classes',
            name='date',
            field=models.DateField(default=datetime.date(2015, 11, 15)),
        ),
    ]
