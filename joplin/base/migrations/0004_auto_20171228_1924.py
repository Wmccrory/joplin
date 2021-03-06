# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20171215_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactDayAndDuration',
            fields=[
                ('dayandduration_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.DayAndDuration')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('base.dayandduration', models.Model),
        ),
        migrations.RemoveField(
            model_name='locationdayandduration',
            name='dayandduration_ptr',
        ),
        migrations.RemoveField(
            model_name='locationdayandduration',
            name='location',
        ),
        migrations.RemoveField(
            model_name='servicepagelocation',
            name='location',
        ),
        migrations.RemoveField(
            model_name='servicepagelocation',
            name='page',
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='base.Location'),
        ),
        migrations.DeleteModel(
            name='LocationDayAndDuration',
        ),
        migrations.DeleteModel(
            name='ServicePageLocation',
        ),
        migrations.AddField(
            model_name='contactdayandduration',
            name='contact',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='hours', to='base.Contact'),
        ),
    ]
