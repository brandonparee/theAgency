# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default=b'Secret', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Secret', b'Secret'), (b'Both', b'Both'), (b'Alpha', b'Alpha Male'), (b'Dog', b'My gender is: Dog'), (b'Cow', b'Cow because cows are the best.')])),
                ('email', models.EmailField(max_length=75)),
                ('birth', models.DateField()),
                ('questions', models.TextField(max_length=2000)),
                ('comments', models.TextField(max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('image', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CaptureEmail',
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
            name='Giveaway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('campaign_fk', models.ForeignKey(to='main.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='campaign_fk',
            field=models.ForeignKey(to='main.Campaign'),
            preserve_default=True,
        ),
    ]
