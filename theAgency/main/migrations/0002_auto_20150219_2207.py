# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thanks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='beer',
            name='zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='language',
            name='zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shirt',
            name='zipcode',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(regex=b'^\\d{5}(?:[-\\s]\\d{4})?$')]),
            preserve_default=True,
        ),
    ]
