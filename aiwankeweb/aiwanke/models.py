# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class GameApp(models.Model):
    # define the fields for your item here like:
    appName = models.CharField(max_length=50,db_column='name')
    iconUrl = models.CharField(max_length=200,db_column='icon')
    apkUrl = models.CharField(max_length=200,db_column='apkfile')
    desc = models.TextField(db_column='memo',max_length=4000,blank=True,null=True)
    author_name = models.CharField(max_length=100,db_column='developer',blank=True,null=True)
    category_name = models.CharField(max_length=50,db_column='categoryname',blank=True,null=True)
    source = models.PositiveIntegerField(db_column='gamesource')
    create_time = models.DateTimeField(auto_now_add=True,db_column='createtime')
    lastupdatetime = models.DateTimeField(auto_now=True,db_column='lastupdatetime')
    editor = models.ForeignKey(User,related_name='games')
    download_cnt = models.PositiveIntegerField(db_column='downcnt',default=0)
    view_cnt = models.PositiveIntegerField(db_column='views',default=0)
    rates = models.PositiveIntegerField(db_column='rates',default=0)




