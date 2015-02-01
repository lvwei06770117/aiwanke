# -*- coding: utf-8 -*-

# Scrapy settings for aiwankecrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'aiwankecrawl'

SPIDER_MODULES = ['aiwankecrawl.spiders']
NEWSPIDER_MODULE = 'aiwankecrawl.spiders'

ITEM_PIPELINES = {
    #'aiwankecrawl.pipelines.JsonWriterPipeline': 300,
    'aiwankecrawl.pipelines.MySQLStorePipeline': 200,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aiwankecrawl (+http://www.yourdomain.com)'
