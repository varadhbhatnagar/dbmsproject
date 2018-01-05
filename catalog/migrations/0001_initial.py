# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('product_name', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('img_link', models.CharField(max_length=2000)),
            ],
        ),
    ]
