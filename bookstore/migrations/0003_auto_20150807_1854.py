# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20150806_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='pubdate',
            field=models.DateField(),
        ),
    ]
