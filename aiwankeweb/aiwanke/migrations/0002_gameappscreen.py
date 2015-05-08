# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiwanke', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameAppScreen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.CharField(max_length=200, db_column=b'pic')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'createtime')),
                ('game', models.ForeignKey(to='aiwanke.GameApp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
