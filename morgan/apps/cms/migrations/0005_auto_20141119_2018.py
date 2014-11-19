# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20141119_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='email',
            field=models.CharField(help_text=b'(Optional)', max_length=255, null=True, verbose_name='Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='office',
            name='fax',
            field=models.CharField(help_text=b'(Optional)', max_length=15, null=True, verbose_name='Fax', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='formpage',
            name='body',
            field=models.TextField(verbose_name='Introduction'),
            preserve_default=True,
        ),
    ]
