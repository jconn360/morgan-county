# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20141119_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='success',
            field=models.CharField(help_text=b'This message is shown after the form is submitted.', max_length=255, verbose_name='Success Message'),
            preserve_default=True,
        ),
    ]
