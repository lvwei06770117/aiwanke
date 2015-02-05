# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
__author__ = 'wei'

import scrapy
from aiwankecrawl.items import AppItem
from django.contrib.auth.models import User

import json
import re


def removeUnicodes(strData):
    if(strData):
        strData = strData.encode('utf-8').strip()
        strData = re.sub(r'[\n\r\t]',r' ',strData.strip())
    return strData

class MyAppSpider(scrapy.Spider):
    name = "MyApp"
    allowed_domains = ["qq.com"]
    start_urls = ['http://sj.qq.com/myapp/cate/appList.htm?orgame=2&categoryId=0&pageSize=20&pageContext=%s' %
                  (pageIndex*20) for pageIndex in xrange(1,26)]

    def parse(self, response):
        #log.msg(response.encoding,level=log.INFO)
        #log.msg(response.body_as_unicode().encode('utf-8'),level=log.INFO)
        #log.msg(response.body.encode('utf-8'),level=log.INFO)
        dictData = json.loads(response.body,encoding="utf-8")
        appList = dictData["obj"]
        for app in appList:
            item = AppItem()
            #log.msg("unicode" if isinstance(app["appName"], unicode) else "str",level=log.INFO)
            # item["appName"] = app["appName"].encode("utf-8") if app["appName"] else ""
            # item["iconUrl"] = app["iconUrl"].encode("utf-8") if app["iconUrl"] else ""
            # item["apkUrl"] = app["apkUrl"].encode("utf-8") if app["apkUrl"] else ""
            # item["desc"] = app["description"].encode("utf-8") if app["description"] else ""
            # item["authorName"] = app["authorName"].encode("utf-8") if app["authorName"] else ""
            # item["categoryName"] = app["categoryName"].encode("utf-8") if app["categoryName"] else ""

            item["appName"] = app["appName"]
            item["iconUrl"] = app["iconUrl"]
            item["apkUrl"] = app["apkUrl"]
            item["desc"] = app["editorIntro"]
            item["author_name"] = app["authorName"]
            item["category_name"] = app["categoryName"]
            item["source"] = 5 # 5:应用宝
            item["editor"] = User.objects.get(username='lvwei')
            yield item
    #http://sj.qq.com/myapp/cate/appList.htm?orgame=2&categoryId=0&pageSize=20&pageContext=40

