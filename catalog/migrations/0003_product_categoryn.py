# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20171226_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categoryn',
            field=models.ForeignKey(to='catalog.Category', default='1'),
        ),
    ]
