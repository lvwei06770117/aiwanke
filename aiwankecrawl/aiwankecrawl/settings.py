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
    'aiwankecrawl.pipelines.DjangoPipeline': 100,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'aiwankecrawl (+http://www.yourdomain.com)'

# Setting up django's project full path.
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
AIWANKE_DIR = os.path.join(BASE_DIR, os.pardir)
sys.path.insert(0,os.path.join(AIWANKE_DIR,'aiwankeweb'))
# Setting up django's settings module name.
# This module is located at aiwanke/aiwankeweb/aiwankeweb/settings.py.
os.environ['DJANGO_SETTINGS_MODULE'] = 'aiwankeweb.settings'
