# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150218_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='color',
            field=models.CharField(default=b'White', max_length=1, choices=[(b'W', b'White'), (b'G', b'Gray'), (b'B', b'Black')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shirt',
            name='cut',
            field=models.CharField(default=b'Unisex', max_length=1, choices=[(b'M', b'Unisex'), (b'F', b'Womens')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shirt',
            name='shirt_size',
            field=models.CharField(default=b'M', max_length=5, choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')]),
            preserve_default=True,
        ),
    ]
