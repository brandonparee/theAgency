# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150218_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('birth', models.DateField()),
                ('zipcode', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('birth', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('shirt_size', models.CharField(default=b'Other', max_length=5, choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL'), (b'Other', b'Other')])),
                ('color', models.CharField(default=b'White', max_length=5, choices=[(b'White', b'W'), (b'Gray', b'G'), (b'Black', b'B')])),
                ('cut', models.CharField(default=b'Unisex', max_length=1, choices=[(b'Unisex', b'M'), (b'Women', b'F')])),
                ('zipcode', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='CaptureEmail',
            new_name='Email',
        ),
        migrations.DeleteModel(
            name='CampaignEmail',
        ),
        migrations.DeleteModel(
            name='Personal',
        ),
    ]
