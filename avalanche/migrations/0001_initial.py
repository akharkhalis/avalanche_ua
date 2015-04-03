# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activity_db',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430')),
                ('time', models.TimeField(null=True, verbose_name='\u0427\u0430\u0441')),
                ('coordinat_x', models.CharField(default=b'', max_length=256, verbose_name='\u0414\u043e\u0432\u0433\u043e\u0442\u0430', blank=True)),
                ('coordinat_y', models.CharField(default=b'', max_length=256, verbose_name='\u0428\u0438\u0440\u043e\u0442\u0430', blank=True)),
                ('altitude', models.CharField(default=b'', max_length=256, verbose_name='\u0412\u0438\u0441\u043e\u0442\u0430', blank=True)),
                ('victims', models.CharField(default=b'', max_length=256, verbose_name='\u041f\u043e\u0442\u0435\u0440\u043f\u0456\u043b\u0456', blank=True)),
                ('rel_volume', models.CharField(default=b'', max_length=256, verbose_name='\u0412\u0456\u0434\u043d\u043e\u0441\u043d\u0438\u0439\u043e\u0431\u0454\u043c', blank=True)),
                ('notes', models.TextField(verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438', blank=True)),
                ('photo', models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True)),
                ('obs_first_name', models.CharField(max_length=256, verbose_name="\u0406\u043c'\u044f")),
                ('obs_last_name', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('obs_phone', models.CharField(max_length=256, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('obs_mail', models.EmailField(max_length=256, verbose_name='\u0415\u043c\u0435\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u041b\u0430\u0432\u0438\u043d\u0430',
                'verbose_name_plural': '\u041b\u0430\u0432\u0438\u043d\u0438',
            },
        ),
    ]
