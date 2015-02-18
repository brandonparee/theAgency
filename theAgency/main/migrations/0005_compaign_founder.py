# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150218_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='compaign',
            name='founder',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
