# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_remove_homepage_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageslideshow',
            name='attribution',
            field=models.CharField(max_length=255, null=True, verbose_name='Attribution Link', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imageslideshow',
            name='author',
            field=models.CharField(max_length=50, null=True, verbose_name='Author', blank=True),
            preserve_default=True,
        ),
    ]
