# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='portrait',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Portrait', to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
    ]
