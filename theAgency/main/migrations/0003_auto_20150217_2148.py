# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_campaign_giveaway_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='giveaway',
            name='image',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
