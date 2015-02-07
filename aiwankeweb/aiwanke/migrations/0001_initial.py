# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GameApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appName', models.CharField(max_length=50, db_column=b'name')),
                ('iconUrl', models.CharField(max_length=200, db_column=b'icon')),
                ('apkUrl', models.CharField(max_length=200, db_column=b'apkfile')),
                ('desc', models.TextField(max_length=4000, null=True, db_column=b'memo', blank=True)),
                ('author_name', models.CharField(max_length=100, null=True, db_column=b'developer', blank=True)),
                ('category_name', models.CharField(max_length=50, null=True, db_column=b'categoryname', blank=True)),
                ('source', models.PositiveIntegerField(db_column=b'gamesource')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_column=b'createtime')),
                ('lastupdatetime', models.DateTimeField(auto_now=True, db_column=b'lastupdatetime')),
                ('download_cnt', models.PositiveIntegerField(default=0, db_column=b'downcnt')),
                ('view_cnt', models.PositiveIntegerField(default=0, db_column=b'views')),
                ('rates', models.PositiveIntegerField(default=0, db_column=b'rates')),
                ('editor', models.ForeignKey(related_name='games', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
