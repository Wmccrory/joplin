# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-23 15:53
from __future__ import unicode_literals

import base.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_department_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='base.Location')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='servicepage',
            name='extra_content',
            field=wagtail.core.fields.StreamField((('content', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'link', 'ul', 'ol'], help_text='Write any additional content describing the service')), ('application_block', base.blocks.SnippetChooserBlockWithAPIGoodness('base.ApplicationBlock', icon='site')), ('map_block', base.blocks.SnippetChooserBlockWithAPIGoodness('base.Map', icon='site')), ('what_do_i_do_with_block', base.blocks.WhatDoIDoWithBlock()), ('collection_schedule_block', base.blocks.CollectionScheduleBlock())), verbose_name='Add any forms, maps, apps, or content that will help the resident use the service'),
        ),
    ]
