# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
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
                ('language', models.CharField(default=b'English', max_length=10, choices=[(b'English', b'English'), (b'Mandarin', b'Mandarin'), (b'Spanish', b'Spanish'), (b'Hindi', b'Hindi'), (b'Arabic', b'Arabic'), (b'Portuguese', b'Portuguese'), (b'Bengali', b'Bengali'), (b'Russian', b'Russian'), (b'Japanese', b'Japanese'), (b'Punjabi', b'Punjabi')])),
                ('race', models.CharField(default=b'English', max_length=16, choices=[(b'Caucasian', b'Caucasian'), (b'African American', b'African American'), (b'Hispanic', b'Hispanic'), (b'Asian', b'Asian'), (b'Middle Eastern', b'Middle Eastern'), (b'Pacific Islander', b'Pacific Islander'), (b'Native American', b'Native American'), (b'Other', b'Other'), (b'Japanese', b'Japanese'), (b'Punjabi', b'Punjabi')])),
                ('birth', models.DateField()),
                ('zipcode', models.EmailField(max_length=5)),
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
                ('shirt_size', models.CharField(default=b'M', max_length=3, choices=[(b'XS', b'XS'), (b'S', b'S'), (b'M', b'M'), (b'L', b'L'), (b'XL', b'XL'), (b'XXL', b'XXL')])),
                ('color', models.CharField(default=b'White', max_length=1, choices=[(b'W', b'White'), (b'G', b'Gray'), (b'B', b'Black')])),
                ('cut', models.CharField(default=b'Unisex', max_length=1, choices=[(b'M', b'Unisex'), (b'F', b'Womens')])),
                ('zipcode', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
