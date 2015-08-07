# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('pubdate', models.DateTimeField()),
                ('publisher', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('price', models.FloatField()),
                ('buylink', models.URLField()),
                ('coverimg', models.ImageField(upload_to='')),
            ],
        ),
    ]
