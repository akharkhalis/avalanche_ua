# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0006_aval_type_triger'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_db',
            name='a_type',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u044f\u043c', blank=True, to='avalanche.aval_type', null=True),
        ),
        migrations.AddField(
            model_name='activity_db',
            name='triger',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u044f\u043c', blank=True, to='avalanche.triger', null=True),
        ),
    ]
