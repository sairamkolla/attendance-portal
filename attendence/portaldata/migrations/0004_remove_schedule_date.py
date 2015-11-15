# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portaldata', '0003_schedule_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='date',
        ),
    ]
