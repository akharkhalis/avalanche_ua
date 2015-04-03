# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avalanche', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u041d\u0430\u0437\u0432\u0430')),
                ('location_coor_x', models.CharField(max_length=256, verbose_name='X')),
                ('location_coor_y', models.CharField(max_length=256, verbose_name='Y')),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
            ],
            options={
                'verbose_name': '\u041b\u043e\u043a\u0430\u0446\u0456\u044f',
                'verbose_name_plural': '\u041b\u043e\u043a\u0430\u0446\u0456\u0457',
            },
        ),
        migrations.AlterField(
            model_name='activity_db',
            name='rel_volume',
            field=models.CharField(default=b'', max_length=256, verbose_name='\u0412\u0456\u0434\u043d\u043e\u0441\u043d\u0438\u0439 \u043e\u0431`\u0454\u043c', blank=True),
        ),
    ]
