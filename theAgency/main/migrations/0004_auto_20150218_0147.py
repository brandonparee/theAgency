# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150217_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='comments',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='questions',
            field=models.TextField(default='', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='gender',
            field=models.CharField(default=b'Secret', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Secret', b'Secret'), (b'Both', b'Both'), (b'Alpha', b'Alpha Male'), (b'Dog', b'My gender is: Dog'), (b'Cow', b'Cow because cows are the best.')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='compaign',
            name='description',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
    ]
