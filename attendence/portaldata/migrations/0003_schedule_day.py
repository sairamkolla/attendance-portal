# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portaldata', '0002_auto_20151114_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='day',
            field=models.IntegerField(default=0),
        ),
    ]
