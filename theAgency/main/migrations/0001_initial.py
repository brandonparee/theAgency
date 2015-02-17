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
                ('gender', models.CharField(default=b'None', max_length=6, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'None', b'I choose not to say'), (b'Both', b'Both'), (b'Alpha', b'Alpha Male')])),
                ('email', models.EmailField(max_length=75)),
                ('birth', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Compaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('founddate', models.DateField()),
                ('image', models.URLField()),
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
                ('image', models.URLField()),
                ('description', models.CharField(max_length=2000)),
                ('compaign_fk', models.ForeignKey(to='main.Compaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='compaign',
            name='giveaway_fk',
            field=models.ForeignKey(to='main.Giveaway'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='compaign_fk',
            field=models.ForeignKey(to='main.Compaign'),
            preserve_default=True,
        ),
    ]
