# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shark',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('name_slug', models.SlugField()),
                ('scientific_name', models.CharField(max_length=255)),
                ('nonfatal', models.IntegerField()),
                ('fatal', models.IntegerField()),
                ('total', models.IntegerField()),
                ('photo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
    ]
