# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#应用宝
class AppItem(scrapy.Item):
    # define the fields for your item here like:
    appName = scrapy.Field()
    iconUrl = scrapy.Field()
    apkUrl = scrapy.Field()
    desc = scrapy.Field()
    authorName = scrapy.Field()
    categoryName = scrapy.Field()
    source = scrapy.Field()


