# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20141119_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='video',
        ),
    ]
