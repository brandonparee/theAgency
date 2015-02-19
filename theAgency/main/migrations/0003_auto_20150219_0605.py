# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150218_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='race',
            field=models.CharField(default=b'Other', max_length=3, choices=[(b'Caucasian', b'Caucasian'), (b'Hispanic', b'Hispanic'), (b'Asian', b'Asian'), (b'African American', b'African American'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='personal',
            name='shirt_size',
            field=models.CharField(default=b'Other', max_length=3, choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'Other', b'Other')]),
            preserve_default=True,
        ),
    ]
