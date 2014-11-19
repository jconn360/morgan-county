# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0004_make_focal_point_key_not_nullable'),
        ('cms', '0005_auto_20141119_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSlideshow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attribution', models.CharField(max_length=255, verbose_name='Attribution Link')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HomePageImageSlideshow',
            fields=[
                ('imageslideshow_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.ImageSlideshow')),
                ('page', modelcluster.fields.ParentalKey(related_name='image_slideshow', to='cms.HomePage')),
            ],
            options={
            },
            bases=('cms.imageslideshow',),
        ),
        migrations.AddField(
            model_name='imageslideshow',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Image', to='wagtailimages.Image', null=True),
            preserve_default=True,
        ),
    ]
