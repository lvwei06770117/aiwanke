# -*- coding: utf-8 -*-
__author__ = 'wei'

import scrapy
from scrapy.http.request import Request
from aiwankecrawl.items import AppItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class HiApkSpider(scrapy.Spider):
    name = "HiApk"
    allowed_domains = ["hiapk.com"]
    start_urls = ['http://apk.hiapk.com/games?sort=5&pi=%s'% pageIndex for pageIndex in xrange(1,51) ]

    def parse(self, response):
        #print(response.url)
        #response.xpath('//div[contains(@id,"softListBox")]/div[contains(@class,"soft_list_box")]/')
        liItems = response.xpath('//ul[contains(@id,"appSoftListBox")]/li[contains(@class,"list_item")]')
        for liItem in liItems:
            item = AppItem()
            self.get_name(item,liItem)
            self.get_icon(item,liItem)
            self.get_apk_url(item,liItem)
            self.get_desc(item,liItem)
            # item["appName"] = liItem.xpath('div/dl[contains(@class,"list_content")]/dt/span[contains(@class,"list_title")]/a/text()').extract()
            # item["iconUrl"] = liItem.xpath('div/div[contains(@class,"left")]/a/img/@src').extract()
            # item["apkUrl"] = liItem.xpath('div/div[contains(@class,"right_mt")]/a/@href').extract()
            # item["desc"] = liItem.xpath('div/dl[contains(@class,"list_content")]/dd/div[contains(@class,"list_description")]/text()').extract()
            item["author_name"]=''
            item["category_name"]=''
            item["source"] = 2 #2:安卓市场
            item["editor"] = 1
            yield item

        #下一页
        #print "下一页".decode("utf-8").encode("utf-8")
        # next_links = response.xpath('//div[contains(@class,"page_box")]/a[contains(.,"下一页".decode("utf-8"))]/@href')
        # for link in next_links:
        #     yield Request(link.extract(),self.parse)

    def get_name(self,item,selector):
        name=selector.xpath('div/dl[contains(@class,"list_content")]/dt/span[contains(@class,"list_title")]/a/text()').extract()
        if name:
            item['appName'] = name[0]

    def get_icon(self,item,selector):
        icon = selector.xpath('div/div[contains(@class,"left")]/a/img/@src').extract()
        if icon:
            item["iconUrl"] = icon[0]

    def get_apk_url(self,item,selector):
        apk_url = selector.xpath('div/div[contains(@class,"right_mt")]/a/@href').extract()
        if apk_url:
            item["apkUrl"] = 'http://apk.hiapk.com'+ apk_url[0]

    def get_desc(self,item,selector):
        desc = selector.xpath('div/dl[contains(@class,"list_content")]/dd/div[contains(@class,"list_description")]/text()').extract()
        if desc:
            item["desc"] = desc[0]










