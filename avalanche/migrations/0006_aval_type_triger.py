# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0005_activity_db_aspect'),
    ]

    operations = [
        migrations.CreateModel(
            name='aval_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2, verbose_name='\u0422\u0438\u043f')),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f',
            },
        ),
        migrations.CreateModel(
            name='triger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('triger', models.CharField(max_length=2, verbose_name='\u043d\u0430\u043f\u0440\u044f\u043c')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u0438\u0447\u0438\u043d\u0430',
            },
        ),
    ]
