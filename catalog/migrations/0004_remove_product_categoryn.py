# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_categoryn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categoryn',
        ),
    ]
