# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='time',
            field=models.DateTimeField(default=1, verbose_name='\u65f6\u95f4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='pr1',
            field=models.CharField(max_length=10, verbose_name='\u4e58\u6570'),
        ),
        migrations.AlterField(
            model_name='data',
            name='pr2',
            field=models.CharField(max_length=10, verbose_name='\u88ab\u4e58\u6570'),
        ),
    ]
