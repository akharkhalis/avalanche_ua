# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0004_auto_20150403_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_db',
            name='aspect',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u044f\u043c', blank=True, to='avalanche.direction', null=True),
        ),
    ]
