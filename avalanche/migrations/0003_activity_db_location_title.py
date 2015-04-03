# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0002_auto_20150403_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity_db',
            name='location_title',
            field=models.ForeignKey(verbose_name='\u041b\u043e\u043a\u0430\u0446\u0456\u044f', to='avalanche.locations', null=True),
        ),
    ]
