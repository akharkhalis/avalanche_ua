# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0003_activity_db_location_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.CharField(max_length=2, verbose_name='\u043d\u0430\u043f\u0440\u044f\u043c')),
                ('degrees', models.CharField(max_length=3, verbose_name='\u0410\u0437\u0438\u043c\u0443\u0442')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u043f\u0440\u044f\u043c',
            },
        ),
        migrations.AlterField(
            model_name='activity_db',
            name='location_title',
            field=models.ForeignKey(verbose_name='\u041b\u043e\u043a\u0430\u0446\u0456\u044f', blank=True, to='avalanche.locations', null=True),
        ),
    ]
